"""Read and exercise the actual bounded Clausewitz tier scripts, without running HOI4."""
from pathlib import Path
from decimal import Decimal
import re

ROOT = Path(__file__).resolve().parents[2]


def parse(path):
    tokens = iter(re.findall(r'\{|\}|=|[^\s{}=]+', re.sub(r'#[^\n]*', '', path.read_text(encoding='utf-8-sig'))))

    def block():
        result = []
        for key in tokens:
            if key == '}':
                break
            assert next(tokens) == '='
            value = next(tokens)
            result.append((key, block() if value == '{' else value))
        return result
    return block()


effects = dict(parse(ROOT / 'common/scripted_effects/rhenish_resistance.txt'))
triggers = dict(parse(ROOT / 'common/scripted_triggers/rhenish_resistance.txt'))
modifiers = dict(parse(ROOT / 'common/dynamic_modifiers/rhenish_resistance.txt'))
constants = dict(dict(parse(ROOT / 'common/script_constants/rhenish_resistance.txt'))['rhenish_resistance'])


def condition(block, state, parameter=None):
    answers = []
    for key, value in block:
        if value == '$MODIFIER$':
            value = parameter
        if key in ('NOT', 'OR'):
            answer = not condition(value, state, parameter) if key == 'NOT' else any(condition([item], state, parameter) for item in value)
        elif key in triggers:
            answer = condition(triggers[key], state, parameter)
        elif key == 'check_variable':
            args = dict(value)
            assert args['var'] == 'resistance' and args['compare'] == 'greater_than'
            answer = state['resistance'] > Decimal(constants[args['value'].split('.')[-1]])
        elif key == 'has_dynamic_modifier':
            answer = value in state['mods']
        elif key == 'state':
            answer = state['id'] == int(value)
        elif key in ('is_owned_by', 'is_controlled_by'):
            answer = state[key] == value
        elif key == 'is_core_of':
            answer = value in state['cores']
        else:
            raise AssertionError(key)
        answers.append(answer)
    return all(answers)


def execute(block, state, parameter=None):
    taken = False
    for key, value in block:
        if key in ('if', 'else_if', 'else'):
            if key == 'if':
                taken = False
            if not taken and (key == 'else' or condition(dict(value)['limit'], state, parameter)):
                execute([(k, v) for k, v in value if k != 'limit'], state, parameter)
                taken = True
        elif key in effects:
            execute(effects[key], state, dict(value)['MODIFIER'] if isinstance(value, list) else parameter)
        elif key in ('add_dynamic_modifier', 'remove_dynamic_modifier'):
            name = dict(value)['modifier']
            name = parameter if name == '$MODIFIER$' else name
            state['operations'] += 1
            state['mods'].add(name) if key.startswith('add') else state['mods'].discard(name)
        else:
            raise AssertionError(key)


samples = ['0', '20', '20.01', '40', '40.01', '60', '60.01', '80', '80.01', '100']
expected = ['light', 'light', 'general', 'general', 'sabotage', 'sabotage', 'armed', 'armed', 'uprisings', 'uprisings']
count = 0
for state_id in (42, 1082, 1083, 1084):
    for start in [None, *modifiers]:
        for resistance, tier in zip(samples, expected):
            state = dict(id=state_id, resistance=Decimal(resistance), is_owned_by='FRA', is_controlled_by='FRA', cores=set(), mods={'unrelated'}, operations=0)
            if start:
                state['mods'].add(start)
            execute(effects['rhenish_resistance_update_state'], state)
            assert state['mods'] == {'unrelated', 'rhenish_resistance_' + tier}
            operations = state['operations']
            execute(effects['rhenish_resistance_update_state'], state)
            assert state['operations'] == operations
            for field, invalid in [('is_owned_by', 'GER'), ('is_controlled_by', 'GER'), ('cores', {'FRA'})]:
                old = state[field]
                state[field] = invalid
                assert all(condition(dict(m)['remove_trigger'], state) for m in modifiers.values())
                execute(effects['rhenish_resistance_update_state'], state)
                assert state['mods'] == {'unrelated'}
                state[field] = old
                execute(effects['rhenish_resistance_update_state'], state)
                assert state['mods'] == {'unrelated', 'rhenish_resistance_' + tier}
            count += 1
for state_id in (51, 55, 1085):
    state['id'] = state_id
    assert not condition(triggers['rhenish_resistance_eligible'], state)
assert {int(k) for k, _ in effects['rhenish_resistance_update']} == {42, 1082, 1083, 1084}
hooks = dict(dict(parse(ROOT / 'common/on_actions/rhenish_resistance.txt'))['on_actions'])
assert set(hooks) == {'on_startup', 'on_daily_FRA'}
for hook in hooks.values():
    assert dict(dict(hook)['effect']) == {'rhenish_resistance_update': 'yes'}
for modifier in modifiers.values():
    for key, value in modifier:
        if key not in ('enable', 'remove_trigger', 'icon'):
            assert value.startswith('constant:rhenish_resistance.')
            Decimal(constants[value.split('.')[-1]])
for tier, duration, penalty, garrison, damage, sabotage in zip(
    ['light', 'general', 'sabotage', 'armed', 'uprisings'],
    ['0.1', '0.25', '0.5', '1', '2'],
    ['-0.1', '-0.25', '-0.5', '-0.75', '-1'],
    ['0', '0.1', '0.5', '1', '3'],
    ['0', '0', '0', '0.5', '2'],
    ['0', '0', '0.1', '0.25', '1'],
):
    assert abs(Decimal(constants[tier + '_construction']) - (1 / (1 + Decimal(duration)) - 1)) < Decimal('0.000001')
    assert dict(modifiers['rhenish_resistance_' + tier])['local_factory_sabotage'] == 'constant:rhenish_resistance.' + tier + '_factory_sabotage'
    assert Decimal(constants[tier + '_factory_sabotage']) == Decimal(sabotage)
    assert 'resistance_activity' not in dict(modifiers['rhenish_resistance_' + tier])
    for suffix, expected_value in [('resources', penalty), ('compliance', penalty), ('garrison', garrison), ('damage', damage)]:
        assert Decimal(constants[tier + '_' + suffix]) == Decimal(expected_value)
print(f'{count} source-driven threshold/transition cases passed; cleanup, reapplication, no replacement at stable tier, unrelated modifier preservation and hook allowlist passed.')
