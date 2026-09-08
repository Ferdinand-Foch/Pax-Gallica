"""Exercise actual national selector, idea callbacks and directed token definitions.

This bounded script interpreter is not the HOI4 engine or its intel UI.
"""
from decimal import Decimal
import re
from test_rhenish_resistance import ROOT, parse, effects, triggers, constants, modifiers

idea_file = dict(parse(ROOT / 'common/ideas/rhenish_resistance.txt'))
ideas = dict(dict(idea_file['ideas'])['country'])
token_file = dict(parse(ROOT / 'common/operation_tokens/rhenish_resistance.txt'))
tokens = {k: dict(v) for k, v in token_file.items() if not k.startswith('@')}
tiers = ['occupation', 'concern', 'crisis', 'insurrection', 'uprising']
domains = {'civilian', 'army', 'navy', 'airforce'}
points = [5, 10, 20, 30, 50]
stability = [Decimal(v) for v in ('0', '-0.05', '-0.10', '-0.15', '-0.25')]
state_ids = (42, 1082, 1083, 1084)


class World:
    def __init__(self):
        self.states = {n: dict(resistance=Decimal(0), owner='FRA', controller='FRA', cores=set(), mods={'unrelated'}) for n in (*state_ids, 51)}
        self.ideas = {'FRA': {'unrelated_spirit', 'economic_law'}, 'GER': {'unrelated_german_spirit'}}
        self.tokens = {('GER', 'FRA', 'token_army'), ('ENG', 'FRA', 'rhenish_concern_army_intel'), ('GER', 'ENG', 'rhenish_concern_army_intel')}
        self.preserved_tokens = self.tokens.copy()
        self.temp = {}
        self.operations = []

    def number(self, value, scope):
        if value.startswith('constant:'):
            return Decimal(constants[value.split('.')[-1]])
        if value == 'resistance':
            return self.states[scope]['resistance']
        if value in self.temp:
            return self.temp[value]
        return Decimal(value)

    def condition(self, block, scope):
        answers = []
        for key, value in block:
            if key == 'NOT':
                answer = not self.condition(value, scope)
            elif key == 'OR':
                answer = any(self.condition([item], scope) for item in value)
            elif key in triggers:
                answer = self.condition(triggers[key], scope)
            elif key == 'check_variable':
                args = dict(value)
                left, right = self.number(args['var'], scope), self.number(args['value'], scope)
                assert args['compare'] in ('equals', 'greater_than')
                answer = left == right if args['compare'] == 'equals' else left > right
            elif key == 'has_idea':
                answer = value in self.ideas[scope]
            elif key == 'has_dynamic_modifier':
                answer = value in self.states[scope]['mods']
            elif key == 'state':
                answer = scope == int(value)
            elif key in ('is_owned_by', 'is_controlled_by'):
                answer = self.states[scope]['owner' if key == 'is_owned_by' else 'controller'] == value
            elif key == 'is_core_of':
                answer = value in self.states[scope]['cores']
            elif key == 'any_owned_state':
                answer = any(s['owner'] == scope and self.condition(value, n) for n, s in self.states.items())
            else:
                raise AssertionError(('unsupported condition', key))
            answers.append(answer)
        return all(answers)

    def execute(self, block, scope='FRA'):
        taken = False
        for key, value in block:
            if key in ('if', 'else_if', 'else'):
                if key == 'if':
                    taken = False
                if not taken and (key == 'else' or self.condition(dict(value)['limit'], scope)):
                    self.execute([(k, v) for k, v in value if k != 'limit'], scope)
                    taken = True
            elif key in effects:
                assert value == 'yes'
                self.execute(effects[key], scope)
            elif key.isdigit() or key in ('GER', 'FRA'):
                self.execute(value, int(key) if key.isdigit() else key)
            elif key == 'set_temp_variable':
                name, source = value[0]
                self.temp[name] = self.number(source, scope)
            elif key in ('add_ideas', 'remove_ideas'):
                assert scope == 'FRA' and value in ideas
                adding = key == 'add_ideas'
                assert (value not in self.ideas[scope]) if adding else (value in self.ideas[scope])
                self.ideas[scope].add(value) if adding else self.ideas[scope].remove(value)
                self.operations.append((scope, key, value))
                self.execute(dict(ideas[value])['on_add' if adding else 'on_remove'], scope)
            elif key in ('add_operation_token', 'remove_operation_token'):
                args = dict(value)
                assert scope == 'GER' and args['tag'] == 'FRA' and args['token'] in tokens
                token = (scope, args['tag'], args['token'])
                self.tokens.add(token) if key.startswith('add') else self.tokens.discard(token)
                self.operations.append((scope, key, token))
            elif key in ('add_dynamic_modifier', 'remove_dynamic_modifier'):
                name = dict(value)['modifier']
                assert scope in state_ids and name in modifiers
                self.states[scope]['mods'].add(name) if key.startswith('add') else self.states[scope]['mods'].discard(name)
            else:
                raise AssertionError(('unsupported effect', key))

    def update(self):
        native_before = {n: s['resistance'] for n, s in self.states.items()}
        self.execute(effects['rhenish_resistance_update'])
        assert native_before == {n: s['resistance'] for n, s in self.states.items()}

    def check(self, tier):
        expected = set() if tier is None else {'rhenish_' + tiers[tier]}
        assert self.ideas['FRA'] == {'unrelated_spirit', 'economic_law'} | expected
        assert self.ideas['GER'] == {'unrelated_german_spirit'}
        expected_tokens = set() if tier is None else {('GER', 'FRA', f'rhenish_{tiers[tier]}_{d}_intel') for d in domains}
        assert self.tokens == self.preserved_tokens | expected_tokens
        gains = {d: Decimal(0) for d in domains}
        for _, _, token in expected_tokens:
            definition = tokens[token]
            gains[definition['intel_source']] += Decimal(token_file[definition['intel_gain']])
        assert set(gains.values()) == {Decimal(0 if tier is None else points[tier])}
        if tier is not None:
            modifier = dict(dict(ideas[next(iter(expected))])['modifier'])
            assert set(modifier) == {'stability_factor', 'custom_modifier_tooltip'}
            assert Decimal(idea_file[modifier['stability_factor']]) == stability[tier]


# Cross product of four possible winning states, all prior tiers, exact boundaries
# and a one-thousandth of a point above each boundary (no rounding allowed).
samples = ('0', '20', '20.001', '40', '40.001', '60', '60.001', '80', '80.001', '100')
expected_tiers = (0, 0, 1, 1, 2, 2, 3, 3, 4, 4)
count = 0
for winner in state_ids:
    for previous in (None, *range(5)):
        for value, expected in zip(samples, expected_tiers):
            world = World()
            if previous is not None:
                world.execute([('add_ideas', 'rhenish_' + tiers[previous])])
            world.states[winner]['resistance'] = Decimal(value)
            world.states[51]['resistance'] = Decimal(100)  # Never eligible, even French-owned.
            world.update()
            world.check(expected)
            operation_count = len(world.operations)
            for _ in range(3):
                world.update()
                world.check(expected)
            assert len(world.operations) == operation_count, 'Stable tier replaced or intel regranted'
            count += 1

# Highest state's fall or exclusion must reveal the runner-up, not a stale maximum.
for exclusion in ('fall', 'owner', 'controller', 'cores'):
    world = World()
    world.states[42]['resistance'] = Decimal(100)
    world.states[1082]['resistance'] = Decimal(30)
    world.update()
    world.check(4)
    if exclusion == 'fall':
        world.states[42]['resistance'] = Decimal(10)
    elif exclusion == 'cores':
        world.states[42]['cores'] = {'FRA'}
    else:
        world.states[42][exclusion] = 'GER'
    world.update()
    world.check(1)
    assert Decimal(15) + Decimal(token_file[tokens['rhenish_concern_civilian_intel']['intel_gain']]) == 25

# No eligible state, cancellation callback, return to occupation, and tied maxima.
for native_cancel in (False, True):
    world = World()
    world.states[42]['resistance'] = Decimal(90)
    world.update()
    for n in state_ids:
        world.states[n]['owner'] = 'GER'
    if native_cancel:
        assert world.condition(dict(ideas['rhenish_uprising'])['cancel'], 'FRA')
        world.execute([('remove_ideas', 'rhenish_uprising')])
    else:
        world.update()
    world.check(None)
    operation_count = len(world.operations)
    world.update()
    assert len(world.operations) == operation_count
    world.states[1084]['owner'] = 'FRA'
    world.update()
    world.check(0)
    world.states[1084]['resistance'] = Decimal(60)
    world.states[42]['owner'] = 'FRA'
    world.states[42]['resistance'] = Decimal(60)
    world.update()
    world.check(2)

assert len(ideas) == 5 and len(tokens) == 20
for definition in ideas.values():
    assert dict(definition)['picture'] == 'DEN_occupation_laws'
    assert dict(dict(definition)['allowed_civil_war']) == {'always': 'no'}
for definition in modifiers.values():
    assert not any('intel' in key for key, _ in definition), 'Local intel duplicates national bonus'
for filename in ('common/ideas/rhenish_resistance.txt', 'common/scripted_effects/rhenish_resistance.txt'):
    source = (ROOT / filename).read_text(encoding='utf-8-sig')
    assert not any(forbidden in source for forbidden in ('add_stability', 'add_intel', 'intel_to_others', 'intel_factor'))
for language in ('french', 'english'):
    ledger_path = ROOT / f'localisation/{language}/replace/rhenish_intel_ledger_l_{language}.yml'
    assert ledger_path.read_bytes().startswith(b'\xef\xbb\xbf')
    ledger = dict(re.findall(r'^([^\s:]+): "(.*)"$', ledger_path.read_text(encoding='utf-8-sig'), re.M))
    assert set(ledger) == {'INTEL_STATIC_SOURCE_OperationTokens', 'INTEL_STATIC_INFO'}
    assert ledger['INTEL_STATIC_SOURCE_OperationTokens'].count('$AMOUNT|.1+%%$') == 1
    assert len(re.findall(r'\$[^$]+\$', ledger['INTEL_STATIC_SOURCE_OperationTokens'])) == 1, 'Ledger must retain its native aggregate amount'
    assert ('réseaux de résistance' if language == 'french' else 'resistance networks') in ledger['INTEL_STATIC_SOURCE_OperationTokens']
    assert 'fixe' not in ledger['INTEL_STATIC_INFO'] and 'Static' not in ledger['INTEL_STATIC_INFO']
    source = (ROOT / f'localisation/{language}/rhenish_resistance_l_{language}.yml').read_text(encoding='utf-8-sig')
    entries = re.findall(r'^([^\s:]+): "(.*)"$', source, re.M)
    localisation = dict(entries)
    assert len(entries) == len(localisation), 'Duplicate localisation key'

    def expand(key, trail=()):
        assert key not in trail, 'Recursive localisation reference'
        assert key in localisation, f'Missing localisation: {key}'
        return re.sub(r'\$([\w]+)\$', lambda m: expand(m[1], (*trail, key)), localisation[key])

    for key in ideas:
        assert f'\n{key}: ' in source and f'\n{key}_desc: ' in source
    for definition in tokens.values():
        assert f'\n{definition["name"]}: ' in source and f'\n{definition["desc"]}: ' in source
    for tier in tiers:
        amount = token_file[f'@{tier}_intel']
        assert localisation[f'rhenish_{tier}_intel_points'] == amount, 'Displayed points differ from runtime tuning'
        tooltip_key = dict(dict(ideas[f'rhenish_{tier}'])['modifier'])['custom_modifier_tooltip']
        assert tooltip_key == f'rhenish_{tier}_intel_tt'
        tooltip = expand(tooltip_key)
        assert tooltip.count(f'§R+{amount} points§!') == 4, 'French spirit must quantify all four domains'
        assert ('Allemagne' if language == 'french' else 'German') in tooltip and 'France' in tooltip
        assert ('chaque jour' if language == 'french' else 'each day') in tooltip
        for domain in domains:
            definition = tokens[f'rhenish_{tier}_{domain}_intel']
            assert definition['icon'] == 'GFX_contact_resistance_bg'
            title, description = expand(definition['name']), expand(definition['desc'])
            assert f'+{amount} pts' in title and expand(f'rhenish_intel_{domain}') in title
            assert expand(f'rhenish_{tier}') in description
            assert ('Allemagne' if language == 'french' else 'Germany') in description and 'France' in description
            assert ('Apport continu' if language == 'french' else 'Continuing intelligence') in description
            assert ('chaque jour' if language == 'french' else 'each day') in description
print(f'{count} national threshold/transition cases passed, each followed by three stable updates; maximum exclusions, cancellation, four directed intel domains, unrelated tokens and local-effect preservation passed.')
print('French/English tooltips and twenty resistance source names resolve; all displayed point values match runtime tokens and describe daily rises, falls and withdrawal.')
print('Native ledger replacements are registered for both languages; aggregate amount formatting is preserved and the fixed-source label is clarified.')
