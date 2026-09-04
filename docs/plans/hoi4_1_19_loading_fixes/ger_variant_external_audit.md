# HOI4 1.19 Loading Fixes: Germany Variant and Italian Entity External Audit

Audit date: 2026-09-04.

Repository: `E:\pax_franca`.

Target installed game: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.

Target game revision: `1.19.2.0/develop`, attested by `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\hoi4_branch.txt:1`.

## Executive classification

| Reported issue | Classification | Pax Franca attribution | Safe Pax Franca change from this audit |
| --- | --- | --- | --- |
| `history/countries/GER - Germany.txt:1547` reports invalid icon `GFX_GER_cv_fighter1_medium` for `Hs 123` | Vanilla source | Not attributed to Pax Franca | No source correction is warranted without an explicit compatibility-workaround decision. |
| `Failed to find entity ITA_mechanized_vehicle_1_entity` | Vanilla DLC source | Not attributed to Pax Franca | No entity patch is warranted in this bounded audit because it would invent or select an Italian vehicle asset. |
| Workshop IDs `2076426030` and `78668637` | External or unclassified outside Pax Franca | No Pax Franca file or reference | No action in Pax Franca and no modification of Workshop or user-content paths. |

The two reported identifiers are present in the installed vanilla source or DLC source, not in Pax Franca source.

No gameplay, interface, entity, Workshop, or vanilla file was changed by this audit.

## Audit method and authority

The required offline Paradox wiki references were consulted before reviewing repository or vanilla files, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, Entity modding, and Equipment modding.

The relevant offline guidance is `paradox_wiki\Entity modding - Hearts of Iron 4 Wiki.md:17-19,50,108-115`, which places entity definitions under `gfx/entities` and names them through `.asset` definitions, and `paradox_wiki\Modding - Hearts of Iron 4 Wiki.md:495-513`, which warns that `replace_path` is a broad unload-and-replace mechanism.

The vanilla documentation for the reported equipment effect is `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md:3069-3095`; it documents `create_equipment_variant` and states at line 3095 that `icon` accepts GFX names.

Repository searches used `rg -a -n --hidden --no-ignore` across `E:\pax_franca`, excluding only `.git` for the broad pass, then a source-only pass excluding `.git`, `.hoi4-mod-setup`, `.agents`, `.codex`, `.tools`, `.tmp`, `docs`, and `paradox_wiki`.

The broad pass also covered the setup lock area, and a separate exact-token pass over `.hoi4-mod-setup`, `.tmp`, `.codex`, and `.agents` found no matches.

No game launch, live save, runtime log, Workshop directory, or path outside the repository was inspected or modified.

## Issue 1: German Hs 123 invalid icon

### Vanilla source evidence

The reported block exists in the installed vanilla country history at `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\history\countries\GER - Germany.txt:1547-1557`:

```text
1547: create_equipment_variant = {
1548:     name = "Hs 123"
1549:     type = small_plane_cas_airframe_0
1550:     modules = {
1551:         fixed_main_weapon_slot = bomb_locks
1552:         engine_type_slot = engine_1_1x
1553:         special_type_slot_1 = empty
1554:     }
1555:     obsolete = yes
1556:     icon = GFX_GER_cv_fighter1_medium
1557: }
```

An exact search of the complete installed vanilla tree finds the invalid token only at `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\history\countries\GER - Germany.txt:1556`.

There is no installed vanilla `SpriteType` definition named `GFX_GER_cv_fighter1_medium`.

The same German file immediately provides a semantic precedent at `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\history\countries\GER - Germany.txt:1569-1579`, where the Ju 87 CAS variant uses `icon = "GFX_GER_CAS1_medium"` at line 1579.

Germany's equipment definition identifies `small_plane_cas_airframe` as a CAS type at `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\units\equipment\x_plane_airframes.txt:8-20`.

Germany's AI equipment data also identifies the Hs 123 as `cas_0` and targets `small_plane_cas_airframe_0` at `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\ai_equipment\GER_planes.txt:258-280`.

Vanilla country precedents use a country CAS icon for non-carrier `small_plane_cas_airframe_0` variants, including `GFX_FRA_CAS1_medium` at `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\history\countries\FRA - France.txt:633-642`, `GFX_JAP_CAS1_medium` at `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\history\countries\JAP - Japan.txt:1318-1327`, and `GFX_USA_CAS1_medium` at `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\history\countries\USA - USA.txt:681-691`.

### Attested valid German GFX candidates in installed vanilla 1.19

The following names are defined by `SpriteType` entries in `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\interface\Technologies.gfx` and are therefore valid installed-vanilla symbols for this revision.

| GFX name | Exact definition | Texture | Assessment for Hs 123 |
| --- | --- | --- | --- |
| `GFX_GER_CAS1_medium` | `interface\Technologies.gfx:4111-4112` | `gfx/interface/technologies/GER_CAS1.dds` | Best semantic candidate; German CAS family and already used by the following Ju 87 variant at `GER - Germany.txt:1579`. |
| `GFX_GER_CAS2_medium` | `interface\Technologies.gfx:4061-4062` | `gfx/interface/technologies/GER_CAS2.dds` | Valid German CAS icon, but represents a later CAS tier. |
| `GFX_GER_CAS3_medium` | `interface\Technologies.gfx:4066-4067` | `gfx/interface/technologies/GER_CAS3.dds` | Valid German CAS icon, but represents a later CAS tier. |
| `GFX_GER_cv_CAS3_medium` | `interface\Technologies.gfx:4071-4072` | `gfx/interface/technologies/GER_cv_CAS3.dds` | Valid symbol, but carrier CAS and therefore semantically wrong for the non-carrier Hs 123. |
| `GFX_GER_iw_small_airframe_medium` | `interface\Technologies.gfx:4211-4212` | `gfx/interface/technologies/GER_early_fighter.dds` | Valid interwar small-airframe icon, but the installed pool labels it as the German early fighter at `gfx\interface\equipmentdesigner\graphic_db\00_plane_icons.txt:449-454`. |

The German CAS pool at `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\gfx\interface\equipmentdesigner\graphic_db\00_plane_icons.txt:361-376` includes `GFX_GER_cv_CAS3_medium`, `GFX_GER_CAS1_medium`, `GFX_GER_CAS2_medium`, and `GFX_GER_CAS3_medium` at lines 366 and 368-370.

The per-level German CAS pools at the same file use `GFX_GER_CAS1_medium`, `GFX_GER_CAS2_medium`, and `GFX_GER_CAS3_medium` at lines 497-519.

The strongest attested replacement candidate is therefore `GFX_GER_CAS1_medium`, but this audit does not apply it.

### Pax Franca attribution and change decision

`E:\pax_franca\history\countries` is absent, so Pax Franca has no country-history file that could contain or override the reported block.

`E:\pax_franca\interface\Technologies.gfx` and `E:\pax_franca\gfx\entities` are also absent, and an exact repository-wide token search finds no `GFX_GER_cv_fighter1_medium` reference or definition.

`E:\pax_franca\descriptor.mod:1-5` contains no `replace_path` declaration, so Pax Franca does not declare a broad history replacement.

Adding `history/countries/GER - Germany.txt` would be a full vanilla country-history override rather than a narrow correction and is not authorized by this task.

A new interface file could technically define a compatibility alias named `GFX_GER_cv_fighter1_medium` and point it at an existing German CAS texture, avoiding a country-history override, but that would mask a vanilla typo with a globally named workaround and silently assign a non-carrier CAS image to a carrier-fighter-looking identifier.

That alias is legitimate only if the parent explicitly approves a version-scoped compatibility workaround and its documentation; it is not warranted by this attribution audit.

Classification: **VANILLA**, with no Pax Franca patch warranted at this time.

## Issue 2: missing `ITA_mechanized_vehicle_1_entity`

### Vanilla DLC source evidence

An exact search of the complete installed vanilla tree finds the reported entity identifier only at `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\dlc\dlc036_by_blood_alone\gfx\entities\BBA_units_vehicles.asset:75`:

```text
60: entity = {
61:     name = "ITA_mechanized_alt_0_entity"
62:     version = 1
63:     pdxmesh = "motorized_frame_mesh"
...
73:     scale = 1.0
75:     attach = { name = "vehicle" vehicle = "ITA_mechanized_vehicle_1_entity" }
76:     attach = { name = "infantry" infantry = "ITA_vehicle_infantry_rifle_bersaglieri_entity" }
77: }
```

The same DLC file defines the neighboring `ITA_motorized_alt_0_entity` at `BBA_units_vehicles.asset:42-58`, which attaches the valid `generic_motorized_vehicle_entity` at line 56 and the Bersaglieri infantry at line 57.

There is no `name = "ITA_mechanized_vehicle_1_entity"` declaration anywhere in the installed vanilla tree.

The base entity file has a distinct Italian frame entity named `ITA_mechanized_entity` at `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\gfx\entities\units_vehicles.asset:1944-1974`, but that block does not define the missing child identifier.

The base Italian motorized entity at `units_vehicles.asset:2014-2030` attaches `generic_motorized_vehicle_entity` at line 2028 and `ITA_vehicle_infantry_rifle_entity` at line 2029.

The generic entity is defined at `units_vehicles.asset:22-47`, while the shared `mechanized_entity` attaches `SOV_mechanized_vehicle_entity` at `units_vehicles.asset:49-65`; neither block defines the missing Italian child.

The available Italian base entity uses `GER_mechanized_mesh` at `units_vehicles.asset:1944-1946`, and the available vehicle mesh definitions at `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\gfx\entities\vehicles.gfx:29-44` cover German mechanized meshes rather than an Italian `ITA_mechanized_vehicle_1_mesh`.

This is an unresolved reference in the installed Blood Alone DLC asset, not a missing Pax Franca override.

### Pax Franca attribution and change decision

`E:\pax_franca\gfx\entities` and `E:\pax_franca\common\units` are absent.

An exact repository-wide token search finds no `ITA_mechanized_vehicle_1_entity` reference, declaration, override, or replacement in Pax Franca.

The source-only search also finds no `replace_path` declaration or related entity replacement in Pax Franca.

Defining a new entity under Pax Franca would require choosing a mesh and animation contract for the Italian mechanized vehicle, and substituting `generic_motorized_vehicle_entity` would be an unapproved visual and identity decision rather than a source-level correction.

No safe Pax Franca entity patch is warranted from this bounded evidence.

Classification: **VANILLA DLC**, external to Pax Franca, with no Pax Franca patch warranted at this time.

## Workshop ID verification

The exact strings `2076426030` and `78668637` have no matches in Pax Franca source, documentation, hidden files, setup lock content, or the currently present temporary/cache/generated-content locations.

The broad repository sweep covered `E:\pax_franca\.hoi4-mod-setup\install.lock.json` and other hidden files, while the setup/cache-specific pass covered `E:\pax_franca\.hoi4-mod-setup`, `E:\pax_franca\.tmp`, `E:\pax_franca\.codex`, and `E:\pax_franca\.agents`; all four exact identifiers were absent.

No Pax path or line can be cited for either Workshop ID because neither identifier exists in the repository.

The IDs are therefore classified as **EXTERNAL OR UNCLASSIFIED OUTSIDE PAX FRANCA**; their owner and runtime role cannot be established from this repository-only audit.

No Workshop `ugc` path or external user-content file was inspected or modified, and no change to either ID is proposed.

## Country-package coverage checklist

This report is a bounded loading-source audit, not a full GER or ITA country-package audit.

| Country-package surface | Result for these reports | Evidence or limitation |
| --- | --- | --- |
| Tag registration, country definition, country history, cosmetic names, party setup | Not implicated and not fully audited | Pax Franca has no `history\countries`, `common\countries`, or `common\country_tags` directory in this scope. |
| States, ownership, controllers, cores, capitals, ports, supply, railways, resources, and buildings | Not implicated | The reported identifiers are an equipment icon and an entity attachment; no related Pax state/map token was found. |
| Leaders, portraits, advisors, commanders, flags, and country assets | Not implicated | No reported identifier resolves to these surfaces; no portrait or flag audit was performed. |
| Focus trees, decisions, missions, ideas, national spirits, events, and scripted effects | Not implicated | No exact reported token was found in Pax source; no broad gameplay audit was performed. |
| Starting military, technologies, industry, production, supply, AI, and playability | Not implicated | Vanilla evidence ties the first issue to country equipment history and the second to a DLC entity asset; no Pax setup change was found. |
| Localisation and documentation | This report only | No player-facing localisation change is needed for either external source issue. |

## File-surface checklist

| Surface | Pax Franca status | Finding |
| --- | --- | --- |
| `history/countries` | Absent | No place in Pax Franca contains the GER history block. |
| `interface/Technologies.gfx` | Absent | No Pax GFX definition can be the source of the invalid German icon. |
| `gfx/entities` | Absent | No Pax entity definition can be the source of the missing Italian child. |
| `common/units` | Absent | No Pax equipment/entity support file is involved. |
| `descriptor.mod` | Present at `E:\pax_franca\descriptor.mod:1-5` | No `replace_path`; the descriptor separately declares `supported_version="1.17.*"` at line 3, which is a compatibility warning for 1.19 but not the cause established here. |
| Repository-wide exact references | None | No exact match for either error token or either Workshop ID. |

## Remaining risks and handoff

Pax Franca declares `supported_version="1.17.*"` at `E:\pax_franca\descriptor.mod:3` while this audit target is installed vanilla 1.19.2; this is a separate release-compatibility risk and should be handled by the parent as a version decision, not silently changed in this report-only task.

If the parent later authorizes a compatibility workaround for the German error, the least speculative candidate is an explicitly documented alias to `GFX_GER_CAS1_medium` from `interface\Technologies.gfx:4111-4112`; a full `history/countries/GER - Germany.txt` override remains broader and is not recommended.

If the parent later authorizes an Italian entity fix, it needs a reviewed asset/design decision for the missing vehicle entity and must not be implemented by editing the installed DLC or Workshop files.

No simplification or fallback was applied, no gameplay source was changed, and no separate plan handoff was created beyond this report at `docs/plans/hoi4_1_19_loading_fixes/ger_variant_external_audit.md`.
