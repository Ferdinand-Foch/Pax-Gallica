# Super-event helper syntax fix handoff

## Scope and outcome

This handoff covers the narrow HOI4 1.19 load-error fix for `common/scripted_effects/pf_super_events.txt`.

The invalid `SUPER_EVENT_ID` effect came from the ID argument block nested directly inside the `pf_show_example_super_event` scripted-effect definition.

The smoke-test call is now inside a vanilla-documented `meta_effect` text block, so the static scripted-effect parser sees only the valid `meta_effect` effect while runtime expansion still invokes the registered helper with ID `1`.

## Files changed

- `common/scripted_effects/pf_super_events.txt` contains the helper correction.
- `docs/plans/hoi4_1_19_loading_fixes/subagent_handoffs/super_event_helper_fix.md` is this required handoff.

`docs/super_events/README.md` was inspected and not changed because its caller contract already documents a reserved integer passed to `<mod_prefix>_show_super_event`.

No event, GUI, scripted GUI, scripted localisation, localisation, GFX, audio, descriptor, map, history, AGENTS, skill, or unrelated file was edited by this subagent.

## Helper map

### `pf_show_super_event`

- Scope: current effect scope, normally a country event or another country-scoped effect.
- Input: `SUPER_EVENT_ID`, supplied by callers as `pf_show_super_event = { SUPER_EVENT_ID = <integer> }`.
- Output: the global visibility flag `pf_super_event_visible` carries the supplied integer as its flag value.
- Side effects: sets or replaces the currently visible super-event registration value.
- Call sites: the public registration contract remains available to event, focus, decision, and other ordinary effect callers.

### `pf_show_example_super_event`

- Scope: current effect scope, matching the public helper.
- Input: none at its existing smoke-test call site.
- Output: executes `pf_show_super_event` with the existing registration ID `1`.
- Side effects: sets `pf_super_event_visible` to `1`, preserving the default smoke-test display.
- Call site: `events/pf_super_event_examples.txt` event `pf_super_event.1` invokes `pf_show_example_super_event = yes`.

## Before and after behavior

Before the patch, `pf_show_example_super_event` contained `pf_show_super_event = { SUPER_EVENT_ID = 1 }` directly in a scripted-effect definition.

HOI4 1.19 parsed that nested argument key as an ordinary effect, producing `Invalid effect 'SUPER_EVENT_ID'`, `Unknown effect type: SUPER_EVENT_ID`, and follow-on brace errors at the reported lines.

After the patch, the nested call is represented as the `text` payload of `meta_effect`.

The public `pf_show_super_event` definition still performs textual `$SUPER_EVENT_ID$` injection into the global flag value, and its required parameterized caller contract is unchanged.

The smoke-test registration ID `1` is unchanged.

The existing scripted-GUI close action still clears `pf_super_event_visible` through `clr_global_flag`; no close-cleanup code was moved or duplicated.

The current helper source contains no duplicate-suppression branch beyond replacing the visible global flag value, so no duplicate behavior was removed or altered.

## Constants and tuning

No script constants or tuning values were added or changed.

The only registration value is the existing smoke-test ID `1`, which remains in the helper text and is not replaced by a static per-ID public helper.

## Event targets, variables, flags, and cleanup

No event targets or variables are used by this helper.

`pf_super_event_visible` remains the global visibility and selected-ID carrier.

The close path remains owned by `common/scripted_guis/pf_super_events.txt` and clears the flag, preserving the existing lifecycle without adding stale state.

## Migration plan

Existing callers should continue to invoke the public helper as `pf_show_super_event = { SUPER_EVENT_ID = <integer> }`.

New registered IDs should be added to the project registry and passed through that same public helper contract.

Parameterized helper calls must not be placed as raw argument blocks inside another `common/scripted_effects` definition unless they are represented through a supported text-expansion route such as the `meta_effect` pattern used here.

## Validation evidence

- The parent-provided pre-change MCP event baseline is revision `1dcfa906fadd9245b32bd1ba88d2e644eace45caa7d6a04bd7ce80391a82edd1`.
- A post-change focused `hoi4.event_inspect` trace for `pf_super_event.1` completed at revision `886126ea4c9e5e03e47e0481f483e5471d68b00a83842683e2da0695065db03d` with `blockingDiagnostics: 0` in the focused result.
- A post-change `hoi4.event_render` overview for `pf_super_event.1` completed at the same revision and produced source-linked JSON, SVG, and PNG artifacts.
- Repository source search confirms the only smoke-test caller remains `pf_show_example_super_event = yes`, and the only `SUPER_EVENT_ID` argument block is now nested under `meta_effect.text`.
- The helper file has balanced effect blocks, and the diff is limited to the nested smoke-test invocation.

## Skipped validation

- No live HOI4 launch or game test was run because the parent task explicitly reserves live validation for the user and forbids launching the game during implementation.
- The MCP `hoi4.event_compare` attempt against the parent baseline timed out during the tool's workspace-wide comparison, so no compare artifact is claimed.
- The event MCP analyzer reports no helper projection for this scripted-effect file, so it cannot independently prove Clausewitz's runtime expansion of the `meta_effect` payload.
- No probability audit was applicable because this patch changes no weight, chance, MTTH, or random-selection logic.

## Risks and follow-up

The remaining runtime risk is that only the user's fresh HOI4 1.19 load can prove the engine accepts and executes the nested helper call emitted by `meta_effect.text`.

The focused MCP trace still reports unrelated workspace issues in its broader analysis, but it reports zero blocking diagnostics within the bounded trace and those diagnostics are outside this helper's allowed scope.

Parent integration should preserve the two changed files, review the helper diff, and perform the final user-owned load and smoke-test acceptance.
