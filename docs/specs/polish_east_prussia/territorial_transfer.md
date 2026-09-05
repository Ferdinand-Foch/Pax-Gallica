# Polish administration of East Prussia

## Scope

At the 1 January 1936 start, Poland owns and controls the two states that constitute German East Prussia in the installed Hearts of Iron IV 1.19 data.

- State 5 retains the localisation key `STATE_5` and the vanilla physical filename `history/states/5-Germany.txt`.
- State 763 retains the localisation key `STATE_763` and the vanilla physical filename `history/states/763-Konigsberg.txt`.

The physical filenames deliberately follow the installed vanilla files rather than the new owner or displayed state name.

## Territorial definition

| State | Installed vanilla name | Provinces | 1936 owner | 1936 controller | Cores |
| --- | --- | --- | --- | --- | --- |
| 5 | Ermland-Masuren | 266, 3351, 3380, 6375, 6402, 9327, 9346, 9372, 9398, 11245, 11386 | POL | POL | GER, PRE |
| 763 | Königsberg | 281, 348, 395, 3384, 6332, 11265 | POL | POL | GER, PRE |

Poland has neither a core nor a starting claim on either state. The retained German and Prussian cores make both states non-integrated Polish territory and leave resistance and collaboration to the normal occupation system.

State 188, Memel, remains Lithuanian. State 85, Danzig, is outside this change and remains unchanged.

## Preserved vanilla data

The state overrides are copies of the installed Hearts of Iron IV 1.19 files with only the 1936 owner changed from `GER` to `POL` and the controller made explicitly `POL`.

State 5 retains its population of 1,238,108, `town` category, eleven-province membership, Allenstein victory point, infrastructure level 3, and local supplies of 12.0.

State 763 retains its population of 2,140,234, `city` category, six-province membership, Königsberg victory point, infrastructure level 3, two civilian factories, two anti-air buildings in 1936, Königsberg bunker and naval base, air base level 6, the 1939 anti-air history, and local supplies of 0.0.

No province geometry, strategic region, resource entry, railway, supply node, adjacency, or map position changes. `map/buildings.txt`, `map/definition.csv`, `map/provinces.bmp`, and all network files remain untouched.

## MCP map evidence

The pre-change `hoi4.map_inspect` revision was `d84e377fad66155e0c80ab49aca8ca284a919b0ebf3f7f8008242acc082f64de`. It inspected all seventeen provinces in states 5 and 763 together with states 188 and 85, resolved 1,739 map pixels, and passed the geometry, state-membership, connection, supply, and railway checks.

The pre-change owner render has PNG SHA-256 `1627b856183ab61c324a7793d0574d523f5a5d88370fb4d5650741844e4ce52a`.

The declarative `hoi4.map_rewrite` call was attempted atomically for both state owners and controllers. The server returned `REWRITE_STRUCTURE_LIMIT` without changing a file. The user explicitly authorised the bounded source fallback, after which the exact vanilla physical state files were added with only the political ownership fields changed.

The post-change `hoi4.map_inspect` revision was `cf820cfe52dd8844000058a04a2d8c6f18d8f1c4395c4cf3b4cdd0cffcef5ee7`. It returned the same seventeen provinces, four states, 1,739 pixels, province memberships, geometry, connections, supply data, and railway data.

The post-change owner render has PNG SHA-256 `48d5275986b43df20de332a79dfb86ab6cf047a6ae79604064e17792925eeff9`.

The before-and-after owner layers differ only by the political colour of states 5 and 763, which changes from Germany to Poland. Memel and Danzig retain their prior owners, and the identical map diagnostics confirm that the territorial shapes and networks did not change.

The global building-position validator continues to report the installed vanilla `floating_harbor` locator limitation outside this feature. No affected entry belongs to states 5 or 763, and the unchanged `map/buildings.txt` confirms that this transfer did not introduce or alter it.

## Reference audit

The German and Polish focus trees were inspected with the HOI4 MCP focus workflow at revision `91c648a1aa958f0c721694505fdec1bed895b4da764d09c439df9996ef9` and rendered with their existing layouts. Germany's state checks and eastern-development content require German ownership or control before applying state effects, so they express a possible reconquest rather than an automatic 1936 restitution. Poland's vanilla `POL_the_old_borders`, `POL_pressure_for_the_west`, and `POL_claim_prussia` branches add claims or cores only after explicit focus choices and therefore do not grant starting integration.

The relevant event chains were inspected and rendered with the HOI4 MCP event workflow at revision `886126ea4c9e5e03e47e0481f483e5471d68b00a83842683e2da0695065db03d`. The `pavel_events.3` transfer path requires German ownership of the affected states, `poland.8` transfers state 5 from the Soviet Union to Poland only in its later-war context, and `germany.1190` and `germany.1191` are post-war settlement choices. None restores states 5 or 763 automatically to Germany at the 1936 start.

The audit also covered German development decisions, formable-nation decisions, achievements, German AI strategy entries, war-goal and territorial-claim effects, German-Soviet settlement paths, capitulation and treaty references, and direct `owns_state`, `controls_state`, `transfer_state`, and `set_state_owner` uses in the mod and active vanilla sources. Existing uses either require ownership or control, preserve an explicit player choice, or operate in a later conflict or settlement context. No directly incompatible source reference required modification, and no AI weight changed.

## Future work

This tranche deliberately does not add a bespoke resistance system, rewrite the Polish focus tree, or redesign German reconquest policy. Future Polish content may offer political choices about occupation, collaboration, or integration, but any route that grants Polish cores must remain an explicit gameplay outcome rather than a starting condition.

## Assets

This territorial ownership change requires no new icons, sprites, portraits, or other visual assets.
