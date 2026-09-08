# Esprits nationaux initiaux

## Portée et méthode

Départ du 1er janvier 1936, HOI4 local `Operation Postern v1.19.2.0.a729 (d245)`.
Les 364 pays non dynamiques enregistrés ont chacun une histoire effective vérifiée, y compris ARM, KUR et les pays libérables.
Les 75 tags dynamiques réservés aux guerres civiles ne possèdent pas d'histoire propre et héritent du pays source lors de leur création.
Les acquisitions normales après le départ restent autorisées.

Le chargement combine les fichiers vanilla et les remplacements homonymes du mod, sans `replace_path` dans `descriptor.mod`.
Les 78 histoires modifiées comprennent 76 remplacements vanilla et les deux fichiers existants ETH et ITA, dont les autres modifications sont conservées.
Les branches DLC alternatives ont toutes été examinées, pas seulement la configuration DLC active.
Les blocs historiques datés après le départ sont conservés.
La classification utilise les définitions effectives de `common/ideas`, `common/idea_tags`, `common/characters` et `common/dynamic_modifiers`.
`country` et `hidden_ideas` sont retirés, ainsi que les modificateurs dynamiques appliqués au pays qui constituent ses esprits nationaux, y compris `ETH_operative_modifier`, invisible.
Les portées d'État sont conservées.

## Comptage

342 attributions historiques sont supprimées dans 78 pays : 265 idées `country`, 8 idées `hidden_ideas` et 69 esprits dynamiques de pays.
L'attribution différée `CZE_army_readiness_4` porte ce total à 343.
Trois instructions communes de démarrage sont neutralisées, ainsi que les trois esprits grecs effectivement sélectionnés par les loyautés initiales, soit 349 attributions ou chemins d'attribution neutralisés avant expansion des boucles communes.
Ce décompte compte séparément les occurrences et variantes DLC, et ne prétend pas représenter le nombre d'esprits simultanément actifs dans une seule configuration.
Le retrait de l'infobulle tchécoslovaque ne compte pas comme une attribution supplémentaire.

## Initialisations complémentaires

| Fichier | Attribution neutralisée au départ | Effets conservés |
| --- | --- | --- |
| `common/on_actions/00_on_actions.txt` | `RAJ_agrarian_society_dynamic`, variante Together for Victory sans Graveyard of Empires | Variable agraire, autres effets et branches IA |
| `common/on_actions/08_bba_on_actions.txt` | `league_of_nations_member_idea`, idée cachée | Autres initialisations BBA et droits pétroliers italiens en Albanie |
| `common/on_actions/10_toa_on_actions.txt` | `USA_monroe_doctrine_idea`, pays existants des Amériques sauf USA | Autres effets de Trial of Allegiance |
| `common/on_actions/06_bftb_on_actions.txt` | Appel initial de `GRE_political_instability_update_effect`, qui sélectionnerait `GRE_loyal_monarchists`, `GRE_hostile_republicans` et `GRE_hostile_communists` | Drapeau de déverrouillage et quatre variables de loyauté, effets ultérieurs du helper |
| `events/MUN_Czechoslovakia.txt` | `MUN_czech_bop.1`, ajout réel de `CZE_army_readiness_4` et infobulle associée, initialisation programmée à J+8 par l'histoire | Équilibre politique, drapeau `CZE_cant_release_SLO_anymore_flag`, option et poids IA |

Les trois gardes `date > 1936.1.1` sont uniquement dans `on_startup` et préservent ces attributions dans les départs ultérieurs.
Elles ne constituent ni une purge, ni un contrôle périodique, ni une interdiction d'acquisition.
L'appel grec retiré ne comportait que des ajouts et retraits d'idées de factions, sans autre effet.
Aucun `remove_ideas` supplémentaire n'est utilisé, donc aucun `on_remove` n'est déclenché par cette suppression.
Les règles `can_join_factions = no` auparavant posées par les `on_add` de `SIK_battle_for_sinkiang` et `CZE_back_against_the_mountains_RUT` sont conservées explicitement dans les mêmes branches historiques.

Pays valides de la boucle initiale de la Société des Nations : AFG, ALB, ARG, AST, AUS, BEL, BOL, BUL, CAN, CHI, COL, COS, CUB, CZE, DEN, DOM, ECU, ENG, EST, ETH, FIN, FRA, GRE, HAI, HOL, HUN, IRE, IRQ, ITA, LAT, LIB, LIT, LUX, MEX, NOR, NZL, PAN, PER, POL, POR, PRU, RAJ, ROM, SAF, SIA, SOV, SPR, SWE, SWI, TUR, VEN, YUG.
La boucle Monroe conserve son sélecteur exact de pays existants à capitale nord-américaine ou sud-américaine, plus CUB, DOM et HAI.

## Inventaire des histoires modifiées

Les identifiants entre parenthèses `×2` indiquent plusieurs attributions alternatives dans le même pays.
Les nombres incluent les variantes DLC et les occurrences répétées.

| Pays | Nombre | Esprits retirés dans l'histoire |
| --- | ---: | --- |
| AFA | 1 | `bba_AFA_skilled_desert_warriors` |
| AFG | 5 | `AFG_mohammad_zahir_shah_ns`, `AFG_pashtunwali`, `AFG_turkish_military_mission`, `AFG_subsistence_economy_modifier`, `AFG_quami_modifier` |
| ARG | 4 | `SMB_MTG_naval_arms_race_legacy`, `ARG_infamous_decade_idea`, `ARG_roca_runciman_treaty_idea`, `ARG_political_corruption_modifier` |
| AST | 5 | `AST_poor_population_growth`, `AST_great_depression_1`, `AST_unratified_westminster_act_idea`, `AST_great_depression_taog_spirit`, `AST_citizen_army_spirit` |
| AUS | 5 | `AUS_widespread_unemployment`, `AUS_phonix_insurance`, `AUS_recovering_from_the_depression`, `AUS_treaty_of_saint_germain_en_laye`, `AUS_austrofascism` |
| BEL | 7 | `BEL_language_barriers_ns` ×2, `BEL_chasseurs_ardennais_ns`, `BEL_chasseurs_ardennais_ns_ncns`, `BEL_scars_of_ww1_dynamic_modifier`, `BEL_corruption_dynamic_modifier`, `BEL_economic_downturn_dynamic_modifier` |
| BOL | 2 | `BOL_toll_of_the_chaco_war`, `BOL_era_of_national_regression` |
| BRA | 5 | `SMB_MTG_naval_arms_race_legacy`, `BRA_separatism_idea`, `BRA_undiversified_economy_modifier`, `BRA_weak_government`, `BRA_aftermath_of_the_coup` |
| BUL | 4 | `BUL_army_restrictions_aat`, `BUL_army_restrictions`, `BUL_second_national_catastrophe`, `BUL_imro_01` |
| CAN | 2 | `CAN_great_depression_1`, `CAN_conscription_crisis` |
| CHI | 13 | `CHI_nine_power_treaty`, `CHI_army_corruption_1`, `CHI_ineffective_bureaucracy`, `CHI_incompetent_officers`, `CHI_hyper_inflation_1`, `german_advisors`, `CHI_corruption_in_the_administration`, `CHI_inefficient_economy`, `CHI_corruption_in_the_armed_forces`, `CHI_illicit_trade`, `CHI_ROCAF`, `CHI_neglected_countryside`, `CHI_nine_power_treaty_sea` |
| CHL | 6 | `CHL_the_mapuche_conflict`, `idea_CHL_the_Hacienda_inquilinaje_system`, `idea_CHL_near_anarchic_society`, `idea_CHL_repubican_guard`, `SMB_MTG_naval_arms_race_legacy`, `CHL_chilean_economy_dynamic_modifier` |
| COG | 3 | `COG_the_invisible_roof`, `COG_vast_decentralized_state_idea`, `COG_force_publique` |
| CSA | 1 | `home_of_the_free` |
| CZE | 10 | `CZE_skoda_works`, `CZE_divided_nation`, `CZE_fortification_focus`, `CZE_sudeten_german_quandary`, `CZE_taticek_of_czechoslovakia`, `CZE_industrialists_veto`, `CZE_agrarian_politics_1`, `CZE_a_divided_nation_fake_ns`, `CZE_a_divided_nation_dynamic_modifier`, `CZE_ceskoslovenska_armada_dynamic_modifier` |
| DEN | 3 | `DEN_neglected_military_dynamic_modifier`, `DEN_economic_crisis_dynamic_modifier`, `DEN_industrial_capability_dynamic_modifier` |
| ENG | 4 | `MTG_naval_treaty_adherent`, `stiff_upper_lip`, `ENG_the_war_to_end_all_wars`, `george_v` |
| EST | 2 | `democratic_opposition`, `EST_vaps_idea_1` |
| ETH | 12 | `ETH_conservative_high_command_idea`, `ETH_the_heroes_of_adwa_idea`, `ETH_christmas_offensive_idea`, `ETH_on_our_own_idea_aat`, `ETH_on_our_own_idea`, `ETH_corrupt_bureaucracy_dynamic_modifier`, `ETH_industrialization_dynamic_modifier`, `ETH_international_red_cross_dynamic_modifier`, `ETH_army_1_dynamic_modifier`, `ETH_navy_1_dynamic_modifier`, `ETH_airforce_1_dynamic_modifier`, `ETH_operative_modifier` |
| FIN | 1 | `FIN_sisu_2` |
| FRA | 7 | `MTG_naval_treaty_adherent`, `FRA_victors_of_wwi`, `FRA_disjointed_government`, `FRA_protected_by_the_maginot_line`, `FRA_full_employment`, `FRA_political_violence`, `FRA_inefficient_economy_2` |
| GDC | 5 | `GXC_uneasy_minds_idea`, `CHI_warlord_looting_idea`, `PRC_government_corruption`, `CHI_ineffective_bureaucracy_warlord`, `CHI_warlord_state_idea` |
| GER | 5 | `sour_loser`, `GER_mefo_bills_modifier`, `GER_army_modifier`, `GER_navy_fascist_modifier`, `GER_airforce_modifier` |
| GRE | 6 | `GRE_george_ii`, `GRE_debt_to_the_ifc`, `GRE_foreign_monopolies`, `GRE_schachtplan`, `GRE_political_instability`, `GRE_agrarian_society` |
| GSM | 5 | `CHI_warlord_looting_idea`, `PRC_government_corruption`, `CHI_ineffective_bureaucracy_warlord`, `CHI_warlord_state_idea`, `CHI_ma_clique_collective` |
| GXC | 5 | `GXC_uneasy_minds_idea`, `CHI_warlord_looting_idea`, `PRC_government_corruption`, `CHI_ineffective_bureaucracy_warlord`, `CHI_warlord_state_idea` |
| HBC | 4 | `CHI_warlord_looting_idea`, `PRC_government_corruption`, `CHI_ineffective_bureaucracy_warlord`, `CHI_warlord_state_idea` |
| HOL | 5 | `HOL_wilhelmina`, `HOL_aloof_neutrality`, `HOL_shell_shocked_spectator_5`, `HOL_de_crisisjaren_5`, `HOL_weak_government` |
| HUN | 7 | `HUN_treaty_of_triannon_aat`, `HUN_treaty_of_triannon`, `HUN_gombos_trade_treaty`, `HUN_hungarian_national_defense_association`, `HUN_levente_associations`, `HUN_treaty_of_triannon_aat_wuw`, `HUN_treaty_of_triannon_wuw` |
| ICE | 2 | `ICE_christian_x`, `ICE_the_icelandic_economy_modifier` |
| INS | 4 | `idea_INS_netherlands_most_precious_jewel`, `INS_dutch_east_indies`, `INS_royal_netherlands_east_indies_army`, `INS_great_depression` |
| IRQ | 4 | `IRQ_golden_square`, `IRQ_anglo_iraqi_treaty`, `IRQ_agrarian_society`, `IRQ_royal_army_modifier_IRQ` |
| ITA | 9 | `vittorio_emanuele`, `vittoria_mutilata`, `ITA_hidden_research_penalties_ns`, `MTG_naval_treaty_cheating`, `ITA_ricostruzione_industriale_dynamic_modifier`, `ITA_military_industry_dynamic_modifier`, `ITA_regio_esercito_dynamic_modifier`, `ITA_regia_aeronautica_dynamic_modifier`, `ITA_regia_marina_dynamic_modifier` |
| JAP | 14 | `JAP_militarism`, `JAP_army_faction_tier_2_equal_navy`, `JAP_naval_faction_tier_2_equal_army`, `JAP_zaibatsu_faction_tier_2`, `JAP_government_faction_tier_2`, `JAP_separate_air_services`, `JAP_japanese_armor_doctrine`, `MTG_naval_treaty_adherent`, `JAP_imperial_influence_dm`, `JAP_state_shinotism_dm`, `JAP_imperial_army_dm`, `JAP_imperial_navy_dm`, `JAP_army_and_naval_air_services_dm`, `JAP_early_industrialization_efforts_dm` |
| KHM | 7 | `SIK_battle_for_sinkiang`, `KHM_unrest`, `CHI_warlord_looting_idea`, `PRC_government_corruption`, `CHI_ineffective_bureaucracy_warlord`, `CHI_warlord_state_idea`, `CHI_ma_clique_collective` |
| KUM | 4 | `CHI_warlord_looting_idea`, `PRC_government_corruption`, `CHI_ineffective_bureaucracy_warlord`, `CHI_warlord_state_idea` |
| LAT | 2 | `LAT_perkonkrust_idea`, `democratic_opposition` |
| LIT | 4 | `LIT_iron_wolf_idea_bad_1`, `LIT_agrarian_society`, `LIT_military_idea_1`, `LIT_seimas_idea_1` |
| MAL | 2 | `MAL_ketuanan_melayu`, `MAL_colonial_administration_idea` |
| MAN | 4 | `MAN_banditry`, `MAN_kwantung_veto`, `MAN_low_legitimacy_5`, `MAN_the_kangde_emperor` |
| MEN | 7 | `MEN_pailingmiao_council_idea` ×2, `MEN_stretched_administration_idea` ×2, `MEN_mongol_banners_idea`, `MEN_communist_revolutionaries_idea`, `MEN_disorganized_army_idea` |
| MEX | 5 | `MEX_callistas`, `MEX_church_power_2`, `MEX_oil_concessions`, `MEX_politicised_army`, `MEX_cedillo_tension_2` |
| NEP | 1 | `NEP_royal_army` |
| NOR | 5 | `NOR_complacent_cabinet_ns`, `NOR_obsolete_armed_forces_ns_1`, `NOR_the_hard_thirties_ns`, `NOR_anti_communist_sentiment_ns`, `NOR_crumbling_fortifications_ns` |
| NXM | 5 | `CHI_warlord_looting_idea`, `PRC_government_corruption`, `CHI_ineffective_bureaucracy_warlord`, `CHI_warlord_state_idea`, `CHI_ma_clique_collective` |
| NZL | 3 | `NZL_railways_board`, `NZL_great_depression`, `NZL_commonwealth_loyalty` |
| PAR | 2 | `BOL_toll_of_the_chaco_war`, `idea_PAR_the_aftershock_of_the_tripple_alliance` |
| PER | 5 | `PER_anglo_iranian_oil_ns`, `PER_rural_feudalism_ns`, `PER_islamic_traditions_ns`, `PER_azerbaijan_resistance_idea`, `PER_kurdistan_resistance_idea` |
| PHI | 4 | `PHI_island_nation_dynamic_modifier`, `PHI_the_great_depression_dynamic_modifier`, `PHI_philippine_army_dynamic_modifier`, `PHI_american_interference_dynamic_modifier` |
| POL | 4 | `POL_april_constitution_1`, `POL_looming_peasants_strike`, `POL_sanation_left_opposition_1`, `POL_sanation_right_opposition_1` |
| POR | 2 | `POR_unreliable_army`, `POR_unstable_republic` |
| PRC | 8 | `PRC_defunct_state_bank`, `PRC_the_long_march_1`, `PRC_red_army_weakened`, `PRC_low_popular_support_3`, `PRC_power_struggles`, `PRC_central_committee`, `PRC_the_chinese_red_army`, `PRC_agrarian_society` |
| RAJ | 6 | `RAJ_agrarian_society`, `RAJ_princely_states`, `RAJ_marginalized_muslim_community`, `RAJ_risk_of_famine`, `idea_RAJ_great_depression_1`, `idea_RAJ_agrarian_society` |
| RNG | 5 | `CHI_nine_power_treaty`, `CHI_army_corruption_1`, `CHI_ineffective_bureaucracy`, `CHI_incompetent_officers`, `CHI_hyper_inflation_1` |
| ROM | 2 | `ROM_king_carol_ii_hedonist`, `neutrality_idea` |
| RUT | 1 | `CZE_back_against_the_mountains_RUT` |
| SAF | 2 | `SAF_ossewabrandwag`, `SAF_history_of_segregation` |
| SER | 1 | `anti_german_military` |
| SHX | 4 | `CHI_warlord_looting_idea`, `PRC_government_corruption`, `CHI_ineffective_bureaucracy_warlord`, `CHI_warlord_state_idea` |
| SIA | 1 | `idea_SIA_army_of_siam` |
| SIC | 5 | `SIC_a_loose_unity`, `CHI_warlord_looting_idea`, `PRC_government_corruption`, `CHI_ineffective_bureaucracy_warlord`, `CHI_warlord_state_idea` |
| SIK | 5 | `SIK_battle_for_sinkiang`, `CHI_warlord_looting_idea`, `PRC_government_corruption`, `CHI_ineffective_bureaucracy_warlord`, `CHI_warlord_state_idea` |
| SLO | 3 | `SLO_slovak_army`, `SLO_clerical_politics`, `SLO_rapid_brigades` |
| SND | 4 | `CHI_warlord_looting_idea`, `PRC_government_corruption`, `CHI_ineffective_bureaucracy_warlord`, `CHI_warlord_state_idea` |
| SOV | 6 | `home_of_revolution`, `trotskyite_plot_nsb`, `SOV_politicized_military`, `SOV_second_five_year_plan_dynamic_modifier`, `SOV_soviet_airforce_dynamic_modifier`, `SOV_the_red_army_dynamic_modifier` |
| SPR | 4 | `SPA_carlism_1`, `SPR_military_disloyalty`, `SPR_political_violence`, `SPR_national_strikes_3` |
| SWE | 7 | `SWE_hungershield`, `SWE_severe_lack_of_ammunition`, `SWE_gustaf_v_idea`, `en_svensk_tiger`, `neutrality_idea` ×2, `SWE_folkhemmet` |
| SWI | 2 | `SWI_swiss_neutrality`, `SWI_foreign_fascist_propaganda` |
| TIB | 2 | `TIB_tibetan_politics_idea`, `TIB_tibetan_army_idea` |
| TUR | 5 | `TUR_kemalist_army_officers_limited_power_loyal`, `TUR_sectarian_woes`, `TUR_disorganised_armed_forces`, `TUR_widespread_illiteracy_idea`, `TUR_first_five_year_plan` |
| URG | 1 | `idea_URG_low_amounts_of_external_debts` |
| USA | 4 | `MTG_naval_treaty_adherent`, `USA_monroe_doctrine_enforcer`, `great_depression`, `home_of_the_free` |
| USB | 2 | `home_of_the_free`, `neutrality_idea` |
| VEN | 1 | `idea_VEN_blockade_inactive` |
| XIC | 4 | `CHI_warlord_looting_idea`, `PRC_government_corruption`, `CHI_ineffective_bureaucracy_warlord`, `CHI_warlord_state_idea` |
| XSM | 5 | `CHI_warlord_looting_idea`, `PRC_government_corruption`, `CHI_ineffective_bureaucracy_warlord`, `CHI_warlord_state_idea`, `CHI_ma_clique_collective` |
| YUG | 5 | `YUG_idea_croatian_opposition`, `YUG_idea_macedonian_opposition`, `YUG_idea_slovene_nationalism`, `YUG_idea_serbian_general_staff`, `anti_german_military` |
| YUN | 4 | `PRC_government_corruption`, `CHI_ineffective_bureaucracy_warlord`, `CHI_warlord_state_idea`, `CHI_warlord_looting_idea` |

## Couverture et éléments préservés

Les 286 autres histoires ne contiennent aucune attribution initiale d'esprit national à retirer, après prise en compte des définitions et portées.
Leurs tags sont : ABK, ADU, ALB, ALG, ALT, ANG, ANU, AOI, ARM, ASY, ATJ, AZR, BAH, BAN, BAR, BAS, BAY, BEG, BHR, BHU, BIA, BLC, BLI, BLR, BLZ, BOS, BOT, BOU, BRD, BRI, BRM, BRN, BSK, BUK, BYA, CAM, CAR, CAT, CAY, CBV, CHA, CHM, CHR, CHU, CIN, CIP, CKK, CMR, COL, COR, COS, CPS, CRC, CRI, CRO, CUB, CYP, DAG, DAH, DDR, DIP, DJI, DNZ, DOM, DON, ECU, EGY, ELS, EQG, ERI, EVE, EZO, FER, FIJ, FOR, FSA, FSM, GAB, GAL, GAM, GAR, GBA, GDL, GEN, GEO, GHA, GLC, GNA, GNB, GOW, GRN, GUA, GUM, GYA, HAI, HAN, HAR, HAW, HES, HON, HRZ, HYD, IAS, IMO, INC, INU, IRE, ISR, ITZ, IVO, JAM, JAN, JOR, KAL, KAR, KAS, KAT, KAZ, KBK, KEN, KHA, KHI, KHL, KKP, KLT, KOL, KOM, KOR, KOS, KSH, KUB, KUR, KUW, KYR, LAO, LBA, LBV, LEB, LIB, LUX, MAC, MAD, MAY, MEK, MEL, MIS, MLD, MLI, MLT, MLW, MNT, MOL, MON, MOR, MPU, MRT, MYS, MZB, NAH, NAV, NEN, NGA, NGR, NIC, NIR, NMB, NOA, NWF, OCC, OKN, OMA, ORO, OVO, PAK, PAL, PAN, PAP, PLU, PNG, POK, PRE, PRU, PSH, PSR, PUE, QAT, QEM, QUE, RAA, RAN, RAP, RAR, RAS, RCG, RCO, RGB, RHD, RHI, RIF, RIG, RJP, RKA, RKB, RKC, RKG, RKH, RKI, RKK, RKL, RKM, RKN, RKO, RKT, RKU, RKV, RNA, ROA, RUS, RWA, SAB, SAM, SAR, SAU, SAX, SCO, SDL, SEN, SHL, SID, SIE, SIL, SIN, SKK, SLV, SMI, SNG, SOK, SOL, SOM, SPM, SRL, SSI, SUD, SUR, SYR, TAH, TAJ, TAN, TAT, TAY, THU, TIG, TML, TMS, TNE, TOG, TOS, TRA, TRI, TTS, TUN, TZN, UAE, UBD, UDM, UGA, UKR, UZB, VAN, VGE, VIN, VLA, VOL, WES, WGR, WIS, WLA, WLS, WPG, WUR, YAK, YAM, YEM, YUC, ZAM, ZIM.
Les boucles communes de démarrage décrites plus haut couvrent également leurs destinataires parmi ces pays.

La comparaison structurelle des 78 histoires confirme la conservation de tous les autres effets, conditions, personnages, frontières, unités, équipements, variables, dates et appels.
Elle confirme notamment 108 attributions explicites de lois, 13 attributions de conseillers ou responsables militaires, `TUR_debt_council` dans `industrial_concern`, et les trois esprits du corps des officiers `CHI_whampoa_military_academy_spirit`, `CZE_legacy_of_the_czechoslovak_legion_army_spirit` et `bureau_of_ordnance_spirit`.
Les lois par défaut restent également définies et aucun esprit national n'utilise `default = yes` dans les définitions effectives.
Les 73 attributions historiques de modificateurs dynamiques d'État sont inchangées, ainsi que les modificateurs de résistance coréenne posés au démarrage.
Les personnages, traits, concepteurs et organismes industriels restent inchangés.
Les droits de ressources français et italiens restent intégralement dans `common/on_actions/sevres_influence_zones.txt`, sans modification, ainsi que les autres concessions des blocs de démarrage.

## Dépendances de progression conservées

Les définitions des esprits et leurs références ultérieures sont conservées.
Un contenu qui exige `has_idea` ou `has_dynamic_modifier` pour un esprit retiré peut devenir indisponible, et une amélioration qui ne fait que modifier ses variables n'a plus d'effet sur ce modificateur absent.
Les remplacements conditionnés à un esprit existant ne sont pas convertis en acquisitions gratuites.
Cela concerne notamment :

- Les paliers de Sisu finlandais, la préparation militaire tchécoslovaque et le secrétaire général chinois, dont les équilibres politiques remplacent des esprits déjà présents.
- Les factions, dettes et monopoles grecs, les factions turques, l'Église mexicaine et les réformes des seigneurs de guerre chinois, qui utilisent les idées comme conditions ou paliers.
- La famine du Raj, conditionnée par `RAJ_risk_of_famine`, et les dépenses de Carol II via `DOD_romania.81`, conditionnées par `ROM_king_carol_ii_hedonist`.
- Les réformes de la dépression, les crises politiques françaises et espagnoles, et les oppositions nationales, dont les contrôles d'idées ou remplacements peuvent ne plus s'appliquer.
- Les chaînes du traité naval, de la Société des Nations et de la doctrine Monroe, qui utilisent leurs esprits comme marqueurs d'appartenance ou de protection.
- Les économies et armées dynamiques des pays de l'inventaire, dont GER, ITA, SOV, DEN, CHI, PRC, JAP, ETH, BRA, AFG, INS et PHI : les variables de progression restent présentes mais ne produisent plus les bonus des esprits initiaux absents.

Les missions initiales `GER_mefo_bills_mission` et `CZE_fate_of_the_ro` sont conservées avec leurs conséquences ultérieures.
Les événements programmés du Congrès américain, du Brésil, du Chili, du Japon et de Roumanie sont conservés : ils ne rétablissent pas un esprit initial sans progression ou condition distincte.
Les acquisitions déclenchées par des événements futurs, décisions, missions ou changements politiques restent autorisées.
Aucun arbre de priorités ni système de progression n'est refondu.

## Validation et limite MCP

Validation hors jeu : inventaire des 364 histoires effectives, classification de chaque attribution, comparaison structurelle avant/après des 78 histoires et des quatre fichiers `on_actions`, contrôle ciblé de l'événement tchécoslovaque et inspection des appels initiaux, missions et équilibres politiques.
Le résultat est zéro attribution historique initiale restante d'idée nationale ou cachée, et zéro modificateur dynamique initial de pays.
Les branches initiales des quatre `on_actions` ne réattribuent plus les esprits identifiés.
La comparaison directe de `MUN_czech_bop.1` confirme que seuls son ajout d'esprit et son infobulle ont disparu, avec les autres événements du fichier identiques.
Aucun lancement de HOI4, accès Internet ou subagent n'a été utilisé.

MCP : `event_inspect` scan/trace avant modification, lint après modification et `event_render` ont été exécutés.
Le scan avant les modifications de démarrage porte la révision `4a456db19bea8e2ee41c3d19986e6dd1ea1c0cb4aa915172040dedcc634af6ea`.
La référence avant modification de l'événement CZE est `a9b8343afbfe3085555f3e234d6e93bb5f0d3ef274c02a3ecaeea97f26242053`, la révision après est `39c1efc02fab96476a91f9f7ba42b0c13f8d18c74aed6a5bdf65714046a34bd5`.
`event_compare` a échoué avec `EVENT_GRAPH_ARTIFACT_INVALID`, indiquant un identifiant de nœud dupliqué `entry_41e58ad3649333af5328c3cc`.
Le contrôle des sources effectives ne trouve aucun identifiant d'événement dupliqué.
Une nouvelle tentative avec un périmètre réduit à huit nœuds a reproduit le défaut, et l'artefact trace ciblé CZE est également refusé pour version de schéma non prise en charge.
La comparaison directe ciblée préautorisée est donc utilisée pour cette étape.
Les résultats MCP sont partiels et ne constituent pas une validation globale réussie du graphe ni une preuve en jeu.

Aucune simplification fonctionnelle ni contenu de remplacement n'est introduit.
La seule limite de validation est la comparaison MCP indisponible, documentée ci-dessus et compensée par la comparaison ciblée autorisée.
Compétence utilisée : `hoi4-events`, sans création ni modification de compétence.
