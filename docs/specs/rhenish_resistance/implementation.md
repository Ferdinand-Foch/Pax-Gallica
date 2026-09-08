# Paliers de résistance rhénane

Tranche partielle pour HOI4 1.19.2.0, confirmé par le `launcher-settings.json` installé : construction, ressources, croissance de la compliance, besoins et dégâts de garnison.
Le renseignement allemand et le risque de sabotage restent non implémentés, sans substitution.

## Territoires et fonctionnement

La spécification `docs/specs/rhenish_departments/territorial_partition.md` et `hoi4.map_inspect` concordent : Sarre (42), Roer (1082), Rhin-et-Moselle (1083), Mont-Tonnerre (1084) sont possédés et contrôlés par FRA, avec cores GER/PRE/RHI et sans core FRA.
Rhénanie (51), Hesse (55) et Hesse-Rhénan (1085) appartiennent à GER et sont exclus, même si FRA les conquiert ensuite.
Le système lit directement la variable moteur `resistance` sur son échelle 0–100, sans copie persistante, arrondi, initialisation ni écriture de résistance/compliance.
Les comparaisons strictes descendantes `>80`, `>60`, `>40`, `>20`, puis le cas restant couvrent exactement les intervalles demandés.

`on_startup` et `on_daily_FRA` appellent uniquement les quatre scopes numériques, sans itération mondiale.
Chaque État doit rester possédé ET contrôlé par FRA et non-core FRA.
Le sélecteur ne retire/remplace rien lorsque le bon palier existe ; lors d'une transition il retire uniquement les cinq identifiants de ce système, puis ajoute le palier voulu.
Les blocs `enable` et `remove_trigger` neutralisent et nettoient aussi les modificateurs invalides lors de l'actualisation native des modificateurs, même si FRA disparaît et que son on_action quotidien ne s'exécute plus.
Le retour aux conditions réapplique le palier à l'actualisation suivante ; la réactivité est quotidienne, pas instantanée.
Aucun événement, insurrection scriptée, bâtiment, frontière, core ou droit de ressources n'est modifié.

## Valeurs et correspondance moteur

Les valeurs ci-dessous sont des contributions relatives aux facteurs moteur, jamais des points de résistance ou de compliance.
La définition commune est `common/script_constants/rhenish_resistance.txt` ; les modificateurs dynamiques lisent ses valeurs par leur interface de variables acceptant `constant:`.

| Intervalle | Palier | Durée nominale | Vitesse ajoutée | Ressources | Croissance compliance | Garnison requise | Dégâts garnison |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 0–20 inclus | Résistance civile légère | +10 % | −9,0909 % | −10 % | −10 % | 0 | 0 |
| >20–40 inclus | Résistance civile généralisée | +25 % | −20 % | −25 % | −25 % | +10 % | 0 |
| >40–60 inclus | Actes de sabotage | +50 % | −33,3333 % | −50 % | −50 % | +50 % | 0 |
| >60–80 inclus | Résistance armée | +100 % | −50 % | −75 % | −75 % | +100 % | +50 % |
| >80–100 inclus | Soulèvements | +200 % | −66,6667 % | −100 % | −100 % | +300 % | +200 % |

Chaque identifiant suivant figure dans `documentation/modifiers_documentation.md` de l'installation, catégorie `state`, et possède le précédent vanilla indiqué.

| Effet | Identifiant moteur | Précédent vanilla |
| --- | --- | --- |
| Vitesse de construction | `state_production_speed_buildings_factor` | `common/dynamic_modifiers/0_dynamic_modifiers.txt`, `autonomous_state` |
| Ressources de l'État | `state_resources_factor` | Même précédent |
| Croissance relative de compliance | `compliance_growth` | Même fichier, `kurdish_separatism` ; `compliance_gain` est plat et n'est pas utilisé |
| Besoin de garnison | `required_garrison_factor` | `common/occupation_laws/occupation_laws.txt`, contribution −0,40 à la ligne 153 |
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

## Limites restantes

- Renseignement : les +5/+10/+15/+20/+30 % réservés à GER contre FRA sont en attente.
  `local_intel_to_enemies` ne réserve pas l'avantage à GER ; les modificateurs de réseau concernent le réseau, pas un renseignement générique ciblé.
  Un traitement séparé devra préciser le domaine, le mode d'agrégation des quatre États, puis une correspondance moteur ciblant effectivement GER contre FRA, avant toute implémentation.
- Sabotage : les 0/0/+10/+25/+100 % sont en attente.
  `local_factory_sabotage` est nommé « Chance to Sabotage Constructions » dans la localisation officielle et utilisé par `FIN_anti_soviet_sentiment` ; `resistance_activity`, utilisé dans le même fichier vanilla, concerne toute l'activité de résistance.
  Ni un risque limité aux constructions ni une hausse générale incluant les attaques de garnisons ne sont retenus sans préciser le sens du sabotage demandé.
- Construction : la conversion réciproque est implémentée ; un allongement exact de la durée finale indépendamment des autres bonus reste une limite du facteur additif décrit ci-dessus.

## Contrôles et références

Le test `.tools/tests/test_rhenish_resistance.py` interprète le sous-ensemble utilisé des scripts réels : 240 cas couvrant les dix valeurs demandées, chaque État, chaque ancien palier et l'absence de palier.
Il vérifie montées/descentes, unicité, stabilité sans remplacement, nettoyage pour propriétaire/contrôleur/core, réapplication, exclusion des États allemands et conservation d'un modificateur tiers.
Il contrôle également le routage des deux on_actions et la résolution des constantes ; ce contrôle statique ne remplace pas l'exécution moteur, non réalisée conformément à la demande.
L'inspection cartographique est à la révision `7e2e8b443c429459ba85deb246c14f077909c402ddb0cc1f0fb26bd01c8104b4` ; l'artefact est `map-inspect.7e2e8b443c429459.json`, SHA-256 `ef3482c3e3f273e8bfbc46432cd62acc445d1eb18780e6e86e19294c1769dbdd`.
MCP valide les appartenances et réseaux ; sa validation globale des positions/ports échoue et n'est pas présentée comme validée ; aucun fichier cartographique n'est touché.
L'inspection probabilité ciblée identifie `no_weighted_surfaces` : ces facteurs ne sont pas un pool pondéré ou une chaîne événementielle prise en charge par ses onze adaptateurs.
Preuve MCP finale : `hoi4-agent://workspace/auto_pax_franca/artifact/b0c4b19b13feddff0b2cb2f001efd34223a3fc8ab0365f808d27aadf7a04c6fe/d93ae3414ac0240543451fc17cc7ade956c17e4b77f4be9c2c6430b3b6d0c347/probability-inspect-92bc021f4e61.json`.
Preuve cartographique : `hoi4-agent://workspace/auto_pax_franca/artifact/ef3482c3e3f273e8bfbc46432cd62acc445d1eb18780e6e86e19294c1769dbdd/018fbcbf27dd41605eb8019ed0ccfb336dd6bf1b549b8d19104bb7cd730984e5/map-inspect.7e2e8b443c429459.json`.
Aucune réécriture de carte, chaîne événementielle, technologie, focus ou GUI n'est concernée.
Sources locales complémentaires : wiki hors ligne, pages centrales imposées et sections variables/résistance, modificateurs dynamiques, effets scriptés et on_actions ; documentation officielle `dynamic_variables_documentation.md`, `triggers_documentation.md`, `effects_documentation.md`, `script_concept_documentation.md` et `common/script_constants/documentation.md`.

Icône finale réutilisée pour les cinq paliers : `GFX_modifiers_generic_resistance`, déjà définie dans le vanilla `interface/countrystateview.gfx` vers `gfx/interface/state_modifiers/modifiers_generic_resistance.dds` ; aucune image ni définition GFX supplémentaire.
Fichiers runtime : `common/{script_constants,dynamic_modifiers,scripted_effects,scripted_triggers,on_actions}/rhenish_resistance.txt` et `localisation/{french,english}/rhenish_resistance_l_<langue>.yml`.
Skills utilisés : `hoi4-events`, `hoi4-feature-assets` ; aucun skill modifié, aucune extension du mécanisme.
