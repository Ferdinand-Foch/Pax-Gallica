# Paliers de résistance rhénane

Paliers pour HOI4 1.19.2.0, confirmé par le `launcher-settings.json` installé : construction, ressources, croissance de la compliance, besoins et dégâts de garnison, sabotage local des constructions.
Le renseignement allemand est hors périmètre conformément au choix utilisateur ; les malus locaux de construction sont acceptés avec leur comportement additif.

## Territoires et fonctionnement

La spécification `docs/specs/rhenish_departments/territorial_partition.md` et `hoi4.map_inspect` concordent : Sarre (42), Roer (1082), Rhin-et-Moselle (1083), Mont-Tonnerre (1084) sont possédés et contrôlés par FRA, avec cores GER/PRE/RHI et sans core FRA.
Rhénanie (51), Hesse (55) et Hesse-Rhénan (1085) appartiennent à GER et sont exclus, même si FRA les conquiert ensuite.
Le système lit directement la variable moteur `resistance` sur son échelle 0–100, sans copie persistante, arrondi, initialisation ni écriture de résistance/compliance.
Les comparaisons strictes descendantes `>80`, `>60`, `>40`, `>20`, puis le cas restant couvrent exactement les intervalles demandés.

`on_startup` entre explicitement dans `FRA` avant d'appeler l'effet scripté ; `on_daily_FRA` possède déjà ce scope pays.
Les deux chemins appellent uniquement les quatre scopes numériques, sans itération mondiale.
Chaque État doit rester possédé ET contrôlé par FRA et non-core FRA.
Chaque branche du sélecteur utilise un identifiant de modificateur littéral et ne retire/remplace rien lorsque le bon palier existe ; lors d'une transition elle appelle le nettoyage partagé des cinq identifiants de ce système, puis ajoute le palier voulu.
Les blocs `enable` et `remove_trigger` neutralisent et nettoient aussi les modificateurs invalides lors de l'actualisation native des modificateurs, même si FRA disparaît et que son on_action quotidien ne s'exécute plus.
Le retour aux conditions réapplique le palier à l'actualisation suivante ; la réactivité est quotidienne, pas instantanée.
Aucun événement, insurrection scriptée, bâtiment, frontière, core ou droit de ressources n'est modifié.

## Valeurs et correspondance moteur

Les valeurs ci-dessous sont des contributions relatives aux facteurs moteur, jamais des points de résistance ou de compliance.
La définition commune est `common/script_constants/rhenish_resistance.txt` ; les modificateurs dynamiques lisent ses valeurs par leur interface de variables acceptant `constant:`.

| Intervalle | Palier | Durée nominale | Vitesse ajoutée | Ressources | Croissance compliance | Garnison requise | Dégâts garnison | Sabotage des constructions |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0–20 inclus | Résistance civile légère | +10 % | −9,0909 % | −10 % | −10 % | 0 | 0 | 0 |
| >20–40 inclus | Résistance civile généralisée | +25 % | −20 % | −25 % | −25 % | +10 % | 0 | 0 |
| >40–60 inclus | Actes de sabotage | +50 % | −33,3333 % | −50 % | −50 % | +50 % | 0 | +10 % |
| >60–80 inclus | Résistance armée | +100 % | −50 % | −75 % | −75 % | +100 % | +50 % | +25 % |
| >80–100 inclus | Soulèvements | +200 % | −66,6667 % | −100 % | −100 % | +300 % | +200 % | +100 % |

Chaque identifiant suivant figure dans `documentation/modifiers_documentation.md` de l'installation, catégorie `state`, et possède le précédent vanilla indiqué.

| Effet | Identifiant moteur | Précédent vanilla |
| --- | --- | --- |
| Vitesse de construction | `state_production_speed_buildings_factor` | `common/dynamic_modifiers/0_dynamic_modifiers.txt`, `autonomous_state` |
| Ressources de l'État | `state_resources_factor` | Même précédent |
| Croissance relative de compliance | `compliance_growth` | Même fichier, `kurdish_separatism` ; `compliance_gain` est plat et n'est pas utilisé |
| Besoin de garnison | `required_garrison_factor` | `common/occupation_laws/occupation_laws.txt`, contribution −0,40 à la ligne 153 |
| Sabotage des constructions | `local_factory_sabotage` | `common/dynamic_modifiers/aat_dynamic_modifiers.txt`, `FIN_anti_soviet_sentiment` (+0,1) |
| Dégâts aux garnisons | `resistance_damage_to_garrison` | `common/dynamic_modifiers/aat_dynamic_modifiers.txt`, `FIN_weapon_caches_modifier` |

Pour une augmentation de durée `d`, le facteur de vitesse est `1/(1+d)` et la contribution enregistrée vaut `1/(1+d)-1`.
Les fractions non finies sont écrites à six décimales ; leur précision effective reste celle du moteur, contrairement aux seuils qui ne subissent aucun arrondi dans le script.
Ces contributions sont additives aux autres contributions du même modificateur : si leur somme hors palier vaut `b` et notre contribution `c`, le rapport des durées vaut `(1+b)/(1+b+c)`, hors autres facteurs et limites moteur.
Exemple : avec +50 % préexistant dans le même facteur, le palier à −50 % fait passer 1,5 à 1,0, soit +50 % de durée, et non +100 %.
Les durées nominales du tableau supposent donc un facteur initial neutre ; une multiplication exacte de la durée finale tous bonus confondus n'est pas garantie.
De même, −100 % de ressources ou de croissance est une contribution au facteur concerné, pas une commande absolue de mise à zéro en présence d'autres bonus.
Les textes français et anglais décrivent les contributions réellement appliquées et affichent la vitesse de construction.

Les pénalités natives de résistance et les lois d'occupation restent actives : notamment pénétration des garnisons à 25, dégâts +100 % à 50, et effets militaires/logistiques à 75 dans `common/resistance_compliance_modifiers/resistance_modifiers.txt`, avec leurs propres marges natives.
Nos dégâts se cumulent avec le +100 % natif et les autres contributions de dégâts ; nos besoins s'ajoutent aux facteurs des lois d'occupation ; ressources et compliance conservent leurs autres facteurs natifs.
Le déclenchement natif à 90 n'est ni supprimé ni remplacé ; « Soulèvements » n'ajoute aucun déclenchement.

## Sabotage et limites moteur

`local_factory_sabotage` ajoute au facteur local de probabilité de sabotage des constructions les contributions 0/0/+0,10/+0,25/+1,00 selon le palier.
Ce facteur se combine au calcul natif associé à la résistance ; il ne remplace pas la résistance ni les dégâts natifs de sabotage.
Les contributions au même facteur se cumulent additivement, sous réserve des bornes internes du moteur ; +10 % n'est pas une addition de dix points de probabilité absolue.
`resistance_activity` et `resistance_garrison_penetration_chance` ne sont pas modifiés : le risque général d'activité et les attaques contre les garnisons ne sont pas amplifiés par ce nouveau facteur.
La construction conserve les valeurs locales converties du tableau ; l'allongement exact tous bonus confondus n'est pas un critère d'acceptation.
Aucune simplification ni omission dans ce périmètre accepté ; le renseignement n'en fait pas partie.

## Contrôles et références

Le test `.tools/tests/test_rhenish_resistance.py` interprète le sous-ensemble utilisé des scripts réels : 240 cas couvrant les dix valeurs demandées, chaque État, chaque ancien palier et l'absence de palier.
Il vérifie montées/descentes, unicité, stabilité sans remplacement, nettoyage pour propriétaire/contrôleur/core, réapplication, exclusion des États allemands et conservation d'un modificateur tiers.
Il contrôle les cinq valeurs et branchements de `local_factory_sabotage`, ainsi que l’absence de substitution par `resistance_activity`.
Il contrôle également le routage des deux on_actions et la résolution des constantes ; ce contrôle statique ne remplace pas l'exécution moteur, non réalisée conformément à la demande.
Les erreurs moteur fournies ont identifié deux défauts dans les scripts : la substitution `$MODIFIER$` dans un effet scripté ordinaire et l'appel d'un effet scripté depuis le scope vide de `on_startup`.
Les branches explicites et le scope FRA corrigent ces deux chemins ; les paramètres sont retirés du simulateur de test, qui rejetait insuffisamment cette syntaxe.
Les contrôles de non-régression rejettent explicitement les appels avec paramètres et les appels depuis un scope vide ; les 240 scénarios sont exécutés sur les branches corrigées.
Références de ces corrections : exemple d'effet appelé avec `= yes` dans le vanilla `common/scripted_effects/00_scripted_effects.txt`, scopes pays sous `on_startup` dans `common/on_actions/00_on_actions.txt`, et section `on_startup` du wiki hors ligne précisant son scope initial `none`.
L'inspection cartographique est à la révision `7e2e8b443c429459ba85deb246c14f077909c402ddb0cc1f0fb26bd01c8104b4` ; l'artefact est `map-inspect.7e2e8b443c429459.json`, SHA-256 `ef3482c3e3f273e8bfbc46432cd62acc445d1eb18780e6e86e19294c1769dbdd`.
MCP valide les appartenances et réseaux ; sa validation globale des positions/ports échoue et n'est pas présentée comme validée ; aucun fichier cartographique n'est touché.
L'inspection probabilité ciblée identifie `no_weighted_surfaces` : ces facteurs ne sont pas un pool pondéré ou une chaîne événementielle prise en charge par ses onze adaptateurs.
Preuve MCP avant sabotage : `hoi4-agent://workspace/auto_pax_franca/artifact/b0c4b19b13feddff0b2cb2f001efd34223a3fc8ab0365f808d27aadf7a04c6fe/d93ae3414ac0240543451fc17cc7ade956c17e4b77f4be9c2c6430b3b6d0c347/probability-inspect-92bc021f4e61.json`.
Preuve MCP finale : `hoi4-agent://workspace/auto_pax_franca/artifact/f3ac6af9f9c15add10855ad0d4d514067a333a64e8036e4df0b01b0497220840/cd8a4a602361bcfb070ea26eafeeb94cfd12b363d5cc086a64dc04260c0f8f30/probability-inspect-ab019d089ef4.json` ; aucun adaptateur disponible pour ce facteur natif, donc aucune simulation MCP de sa fréquence moteur n'est revendiquée.
Preuve cartographique : `hoi4-agent://workspace/auto_pax_franca/artifact/ef3482c3e3f273e8bfbc46432cd62acc445d1eb18780e6e86e19294c1769dbdd/018fbcbf27dd41605eb8019ed0ccfb336dd6bf1b549b8d19104bb7cd730984e5/map-inspect.7e2e8b443c429459.json`.
Aucune réécriture de carte, chaîne événementielle, technologie, focus ou GUI n'est concernée.
Sources locales complémentaires : wiki hors ligne, pages centrales imposées et sections variables/résistance, modificateurs dynamiques, effets scriptés et on_actions ; documentation officielle `dynamic_variables_documentation.md`, `triggers_documentation.md`, `effects_documentation.md`, `script_concept_documentation.md` et `common/script_constants/documentation.md`.

Icône finale réutilisée pour les cinq paliers : `GFX_modifiers_generic_resistance`, déjà définie dans le vanilla `interface/countrystateview.gfx` vers `gfx/interface/state_modifiers/modifiers_generic_resistance.dds` ; aucune image ni définition GFX supplémentaire.
Fichiers runtime : `common/{script_constants,dynamic_modifiers,scripted_effects,scripted_triggers,on_actions}/rhenish_resistance.txt` et `localisation/{french,english}/rhenish_resistance_l_<langue>.yml`.
Skills utilisés : `hoi4-events`, `hoi4-feature-assets` ; aucun skill modifié, aucune extension du mécanisme.
