# Generic focus reset — registre unique

## France — FRA

- Statut : conversion vérifiée statiquement ; contrôle direct autorisé en remplacement de la seule comparaison MCP défaillante.
- Cible : démarrage du 1er janvier 1936, HOI4 1.19.2.0, confirmé par le `launcher-settings.json` installé (Operation Postern, d245).
- Tag : `FRA`, défini par le fichier vanilla `common/country_tags/00_countries.txt`.
- Anciens arbres chargés : `french_focus` depuis la surcharge existante `common/national_focus/france.txt` ; `free_french_focus` et `vichy_french_focus` depuis vanilla avant ce changement.
- Variantes DLC : le même `french_focus` contient les conditions avec/sans La Resistance ; il ne s'agit pas de deux arbres distincts.
Les conditions No Step Back, Arms Against Tyranny, Death or Dishonor et Man the Guns portent sur son contenu, pas sur son sélecteur.
Les transitions France libre et Vichy sont également couvertes.
- Mécanisme antérieur : aucun reset générique ni registre trouvé dans ce checkout.
Le nouveau fichier partagé `common/on_actions/generic_focus_reset.txt` suit le patron `on_startup` et la borne de date déjà employés dans le dépôt.
Les prochains pays peuvent y être ajoutés sans copier le générique.
- Méthode : après la sélection initiale, `FRA = { load_focus_tree = { tree = generic_focus } }` au démarrage antérieur au 2 janvier 1936.
Aucune pondération de sélection, IA, récompense, icône ou localisation n'est modifiée.
La structure des arbres ne change pas ; `focus_rewrite` n'est donc pas utilisé.
- Histoire : le fichier vanilla `history/countries/FRA - France.txt` reste hérité intégralement.
Aucune attribution explicite ni priorité précomplétée pour 1936 ; les douze `complete_national_focus` des lignes 246–257 appartiennent au bloc 1939 et sont conservés.
- Périmètre : tag exact FRA ; les pays dynamiques et VIC conservent leurs réattributions.
Les gardes restent applicables à FRA au cours de la campagne.
Le démarrage 1939 n'est pas réattribué par le nouveau on_startup.

### Fichiers et réattributions

| Fichier ajouté au mod | Modification fonctionnelle |
| --- | --- |
| `common/on_actions/generic_focus_reset.txt` | Attribution 1936 de `generic_focus` à FRA. |
| `events/France.txt` | 3 appels protégés par `NOT = { tag = FRA }`. |
| `events/LaR_France.txt` | 4 appels protégés, événements `lar_end_the_occupation.2/.3/.5/.6`. |
| `common/on_actions/05_lar_on_actions.txt` | 2 retours à `french_focus` après guerre civile protégés. |
| `common/decisions/FRA.txt` | 2 attributions des décisions de test protégées. |
| `common/national_focus/free_france.txt` | Retour à `french_focus` protégé. |
| `docs/specs/generic_focus_reset/progress.md` | Présent registre. |

Les cinq surcharges reproduisent les fichiers vanilla effectivement hérités ; une comparaison inverse confirme que leur texte est identique à vanilla après retrait du commentaire d'en-tête et des douze gardes.
Les événements, autres effets, branches, pays et récompenses sont conservés.
Aucun replace_path, aucune copie du générique, aucun nouveau contenu national.
Les deux changements manuels déjà indexés dans les fichiers Sèvres sont laissés intacts.

### Preuve statique et MCP

- Avant : `french_focus` obtient 10 pour FRA ; générique, France libre et Vichy obtiennent chacun 1.
Le sélecteur français n'a pas de condition DLC.
- Après : ces scores restent identiques ; l'attribution explicite au `on_startup` charge ensuite `generic_focus`.
Cette preuve suit le script et la documentation de `load_focus_tree` ; le MCP focus inspecte les arbres mais ne simule pas l'exécution du démarrage.
- `hoi4.focus_inspect` ciblé du générique avant/après : 56 focus, 56 titres résolus, 14 focus continus, aucun diagnostic bloquant.
Empreinte de disposition identique : `ad2b3bb2de93a33b2152cd1e0a303ff29f29cec5c43123ba39d4a80a696e4716`.
- Source générique vanilla inchangée, SHA-256 : `DA7D2AD989FE174A904838D55481BCFD07D652940260466259CB27DD21893768`.
- `hoi4.focus_render` et `hoi4.focus_raster` réussis pour le générique ; rendu PNG 1670 × 419 : [artefact MCP](hoi4-agent://workspace/auto_pax_franca/artifact/26c68a38ca9f9b1af148323e5607f5f868f28dc9bc5b3886886edaadf45723d3/863c970556b5ed432359bd19bc00ea23c1530ab0c463d9ab30f7354f6bf220f4/generic_focus.focus.png).
Les avertissements de connecteurs et récompenses du générique sont conservés pour respecter sa réutilisation intégrale.
- Inspection France libre avant/après : 23 focus, deux diagnostics `FOCUS_PREREQUISITE_GROUP_MALFORMED` sur les groupes vides de `FRA_appeal_to_the_french_nation` et `FRA_refus_absurde`.
Ces groupes sont inchangés ; leur correction structurelle sort du reset demandé.
- Événements : inspection initiale, trace, lint et rendu ciblés exécutés.
Révision initiale : `c5fc36d69fb6b5a5c8e812e2fd680a54af5c800739e1ce72b66e0f120a64500f`.
Le lint reste une analyse partielle et ne vaut pas validation exhaustive.
- Blocage de comparaison : la révision initiale n'est pas retrouvée par `hoi4.event_compare` (`EVENT_REVISION_NOT_CACHED`).
L'utilisation de l'artefact initial via `before.artifactUri` échoue ensuite avec `EVENT_GRAPH_ARTIFACT_INVALID` : `event graph.nodes contains a duplicate identifier`, identifiant `entry_4b2e8aab856abda074c4f91c`.
La route existe mais son résultat obligatoire reste indisponible ; aucune comparaison réussie n'est revendiquée.
- Validation en jeu : non effectuée ; aucun lancement du jeu ni subagent.
- Commit : conversion française validée pour un commit séparé après application de la dérogation explicite de comparaison.

### Dépendances restantes et limites

Les esprits `FRA_victors_of_wwi`, `FRA_disjointed_government`, `FRA_full_employment` et `FRA_inefficient_economy_2` restent inchangés ; le générique ne fournit pas les anciennes réformes françaises.
Les conditions des décisions liées au Front populaire, à la contre-révolution, aux ligues et à la réorganisation aéronautique restent liées aux anciens focus.
Le succès Petite Entente dans `common/achievements.txt`, les vérifications de la ligne Maginot dans `common/decisions/GER.txt` et les conditions de résistance intérieure restent inchangés.
Les plans vanilla `FRA_historical_strategy_plan.txt` et `FRA_alternate_strategy_plan.txt` continuent de référencer les anciennes priorités ; ils ne sont pas rééquilibrés.
Les effets vanilla d'achèvement/déverrouillage accompagnant les transitions sont conservés : seule la réattribution d'arbre est neutralisée.
Les règles politiques, personnages, armées, industrie, frontières et modifications manuelles ne sont pas modifiés.

Aucune simplification du générique ni aucun remplacement d'actif.
La validation statique est terminée avec le contrôle de remplacement autorisé ; event_compare reste défaillant et aucune validation en jeu n'est revendiquée.
Les sept fichiers de cette conversion forment un commit séparé des changements Allemagne et Sèvres.
Compétences utilisées : `hoi4-focus-trees`, `hoi4-events`, `hoi4-decisions-missions` ; aucune compétence créée ou modifiée.

### Contrôle français de remplacement autorisé

La collision interne `entry_4b2e8aab856abda074c4f91c` correspond aux deux blocs vanilla `on_release_as_puppet` de `common/on_actions/13_goe_on_actions.txt`, lignes 171 et 1758 ; aucun de ces blocs n'est une définition d'événement.
L'analyse de l'instantané complet a établi cette collision de nœuds MCP pendant la validation allemande ; aucune réparation globale ni modification du serveur n'est effectuée.
Une paire d'instantanés a été régénérée après restitution temporaire du contenu vanilla des deux fichiers événementiels, puis restauration de leurs gardes, avec inspection ciblée sur `events/France.txt`.
L'unique nouvelle tentative event_compare échoue avec le même identifiant ; son succès n'est pas revendiqué.
Le contrôle direct couvre aussi intégralement `events/LaR_France.txt`.

L'inventaire chargé remplace chaque chemin événementiel vanilla par la surcharge mod de même chemin avant de compter les définitions.
Il trouve exactement une définition de chacun des cinq événements touchés : `france.14`, `lar_end_the_occupation.2`, `.3`, `.5` et `.6`.
Les cinq fichiers surchargés, après retrait inverse des douze gardes FRA et de leurs commentaires d'en-tête, sont identiques aux fichiers vanilla.
Les options, cibles, conditions DLC, effets, références et autres pays sont conservés.
Pour FRA les réattributions sont neutralisées ; pour les autres tags les conditions vanilla restent applicables.

Les inspections et rendus MCP du générique ont été répétés avec succès : 56 focus, disposition identique, aucun diagnostic bloquant sur l'arbre attribué.
Les diagnostics de groupes vides de France libre portent sur la structure vanilla conservée et ne constituent pas un doublon source ni une altération de structure causée par cette conversion.
La dérogation autorise uniquement le remplacement de la comparaison événementielle MCP, pas une revendication de test en jeu.
Aucune simplification du générique ni refonte des dépendances restantes.

## Allemagne — GER

- Statut : conversion vérifiée statiquement ; comparaison directe autorisée en remplacement de la seule comparaison MCP défaillante.
- Cible : 1936.1.1, version installée 1.19.2.0 (Operation Postern, d245).
- Tag : `GER`, définition vanilla `common/country_tags/00_countries.txt`.
- Ancien arbre : `german_focus`, surcharge existante `common/national_focus/germany.txt`, 438 focus inspectés par MCP.
Le fichier contient les variantes avec/sans `Gotterdammerung`, ainsi que les conditions héritées de `Waking the Tiger`.
Les autres conditions DLC du contenu ne changent pas son identifiant ni son sélecteur.
Aucun second fichier allemand n'a été trouvé dans les arbres nationaux vanilla installés.
- Méthode : ajout de GER au `on_startup` partagé de `common/on_actions/generic_focus_reset.txt`, après la sélection initiale, pour les démarrages antérieurs au 2 janvier 1936.
L'attribution française existante est conservée.
Aucune copie de `generic.txt`, aucune modification du contenu national ni des pondérations.
- Histoire : le fichier `history/countries/GER - Germany.txt` reste hérité de vanilla.
Aucune attribution explicite, priorité achevée ou déverrouillée en 1936.
Les achèvements et déverrouillages trouvés sont dans le bloc 1939 et restent intacts.
- Réattributions : les trois appels à `german_focus` sont entourés de `if = { limit = { NOT = { tag = GER } } ... }`.
Un appel concerne la victoire fasciste dans `common/on_actions/03_wtt_on_actions.txt`.
Deux appels concernent `mtg_netherlands.76` dans `events/MTG_Netherlands.txt`, avec et sans Götterdämmerung.
La sélection des pays, les événements et leurs autres effets sont préservés, y compris les déverrouillages et achèvements accompagnateurs.
Les pays dynamiques dont le tag exact n'est pas GER conservent leur comportement vanilla.

### Fichiers de cette intervention

| Fichier | Changement |
| --- | --- |
| `common/on_actions/generic_focus_reset.txt` | Ajout du seul bloc GER au mécanisme commun existant. |
| `common/on_actions/03_wtt_on_actions.txt` | Surcharge vanilla avec une garde GER. |
| `events/MTG_Netherlands.txt` | Surcharge vanilla avec deux gardes GER. |
| `docs/specs/generic_focus_reset/progress.md` | Ajout de cette section Allemagne ; section France conservée. |

Les différences des deux surcharges ont été examinées contre les fichiers vanilla.
Après retrait des gardes et du commentaire d'en-tête, leur texte est identique à vanilla.
Aucun arbre régional ou autre pays n'est modifié.
Les changements manuels déjà indexés et les modifications françaises non commitées restent intacts.

### Preuve et limites de validation

Avant : `german_focus` obtient 10 pour GER, contre 1 pour `generic_focus`, sans condition DLC dans son sélecteur.
Après : ces scores ne changent pas ; le nouveau bloc GER exécute explicitement `load_focus_tree = { tree = generic_focus }` au démarrage 1936.
Cette preuve de l'attribution repose sur le flux du script et la documentation vanilla de l'effet ; le MCP focus n'exécute pas le démarrage du moteur.
Le générique demeure celui de vanilla avec ses 56 focus, récompenses, icônes et localisations.
Les appels ciblés `hoi4.focus_inspect` et `hoi4.focus_render` passent avant et après, sans diagnostic bloquant sur le générique.
L'empreinte de disposition reste `ad2b3bb2de93a33b2152cd1e0a303ff29f29cec5c43123ba39d4a80a696e4716`.
[Rendu SVG MCP après modification](hoi4-agent://workspace/auto_pax_franca/artifact/df18b9231cb3f5fbea5137a9fb155756aada3a04c5dec20851ac827bec16e109/1e5889b6a998d44eecab553c0b8474626052fc578507c9a2f4acebedb4e84bb9/generic_focus.focus.svg).
Aucune structure de focus n'étant modifiée, `focus_rewrite` n'est pas utilisé.

Les inspections et rendus événementiels avant/après sont exécutés sur `mtg_netherlands.76`.
Le lint est partiel : le serveur diffère certaines analyses globales du grand workspace.
La comparaison obligatoire `hoi4.event_compare` a été tentée avant et après l'édition et échoue avec `EVENT_GRAPH_ARTIFACT_INVALID`, doublon `entry_4b2e8aab856abda074c4f91c` dans l'instantané produit par le serveur.
Révision initiale : `57a8119186349d1918e4b943b74470f8fe99d074bb47340a4b231e915522b575`.
La route existe mais sa preuve de comparaison reste bloquée.
La dérogation explicite de l'utilisateur autorise le contrôle direct documenté ci-dessous à remplacer cette seule comparaison MCP.
L'arbre allemand inchangé donne également des diagnostics MCP lors de l'inspection initiale ; aucune correction de ses 438 focus n'est incluse dans ce remplacement d'attribution.

Validation en jeu non effectuée ; aucun lancement du jeu et aucun subagent.
Aucune simplification du générique.
Le contrôle événementiel de remplacement est terminé ; aucune réussite de event_compare ni validation en jeu ne sont revendiquées.

### Dépendances conservées

Les factures MEFO, l'économie de conquête et le cercle intérieur restent configurés comme dans l'histoire vanilla ; leurs progressions liées aux anciens focus ne sont pas adaptées.
Les décisions allemandes continuent notamment de tester `GER_danzig_or_war`, `GER_war_with_the_ussr`, `GER_adopt_new_panzer_doctrine` et `GER_panzergrenadier`.
Les ratios navals de `common/ai_strategy/GER.txt` restent liés à `GER_trade_interdiction` et `GER_plan_z`.
Les plans d'IA, événements diplomatiques, objectifs territoriaux et autres conditions des anciens focus ne sont pas refondus.
Politique, idées, personnages, armée, industrie et frontières sont préservés.
Les effets d'achèvement des anciens focus dans les transitions restent présents conformément au périmètre limité aux réattributions.

Compétences utilisées : `hoi4-focus-trees` et `hoi4-events` ; aucune créée ou modifiée.
Le commit Allemagne contient uniquement cette section du registre, le bloc GER du mécanisme commun et les deux surcharges allemandes ; les changements français restent dans le répertoire de travail.
### Contrôle de remplacement autorisé

L'ID interne `entry_4b2e8aab856abda074c4f91c` correspond à deux nœuds de type `entry`, label `on_release_as_puppet`, du même fichier effectivement chargé `game:common/on_actions/13_goe_on_actions.txt`, aux lignes 171–203 et 1758–1790.
Il n'existe pas de surcharge mod de ce chemin.
Ces blocs on_action distincts ne sont pas des définitions d'événement concurrentes ; l'instantané leur attribue un identifiant identique malgré leurs emplacements distincts.
Le défaut est donc une collision d'identifiants de nœuds MCP, sans doublon d'événement créé par la conversion.
Aucune modification de ces blocs ni de hoi4-agent-tools n'est effectuée.

Le contrôle ciblé des événements vanilla et mod, en remplaçant chaque chemin vanilla par sa surcharge mod, trouve exactement une définition de `mtg_netherlands.76`, dans `events/MTG_Netherlands.txt:3047`.
La définition vanilla du même chemin est masquée, pas chargée une seconde fois.
Une seule paire valide d'instantanés a été régénérée avec le sélecteur `mtg_netherlands.76`, profondeur 1, direction downstream, limites de 4 nœuds et 4 arêtes, sans expansion des helpers.
L'instantané avant emploie temporairement le contenu vanilla de ce seul fichier ; le contenu modifié a été restauré avant l'instantané après.
L'unique nouvelle tentative event_compare échoue encore avec EVENT_GRAPH_ARTIFACT_INVALID et le même ID, malgré ce sélecteur ciblé.

En remplacement autorisé : comparaison des deux surcharges avec vanilla, puis retrait inverse des trois gardes GER et de leurs commentaires d'en-tête ; le contenu restant est exactement identique.
Le choix aléatoire de la cible, les conditions DLC, les événements, leurs options, les effets d'achèvement et toutes les références restent intacts.
Pour GER, les trois appels de réattribution sont bloqués ; pour les autres tags, ils sont exécutés sous les conditions vanilla.
Le on_startup charge explicitement generic_focus pour GER le 1er janvier 1936, indépendamment du DLC, et ne s'applique pas au démarrage 1939.
Les inspections et rendus MCP du générique ont été répétés avec succès : 56 focus inchangés, sans diagnostic bloquant.
Les dépendances anciennes énumérées ci-dessus restent préservées, sans refonte ni simplification.

## Lot de 50 pays — validation du démarrage 1936

Les entrées ci-dessous utilisent le même arbre vanilla `generic_focus` de HOI4 1.19.2, sans copie ni réécriture des 56 focus, de leurs récompenses, icônes, localisations ou poids IA.
Chaque tag exact est attribué par `common/on_actions/generic_focus_reset.txt`, dans le `on_startup` limité par `date < 1936.1.2`.
Les scores de sélection restent intacts ; l'effet explicite charge le générique après cette sélection, avec ou sans les DLC indiqués.
Quand le DLC national est absent, le générique déjà choisi par défaut reste le générique.
Les états initiaux, lois, idées, personnages, unités, industrie, territoires et modifications manuelles sont préservés.
Les achèvements et déverrouillages trouvés dans les histoires appartiennent aux blocs 1939 ; aucun n'est supprimé.
Les plans IA et mécaniques dépendant des anciens focus restent inchangés ; les références représentatives par pays sont indiquées sans prétendre que ces mécaniques ont été adaptées.

### Preuves communes

L'inspection MCP avant/après couvre 62 arbres pertinents, y compris le générique, les variantes DLC et les deux arbres chinois attribuables par script.
Le texte de leurs sélecteurs et leurs nombres de focus sont identiques avant/après ; les artefacts complets ont été lus localement pour dépasser la troncature de la réponse MCP.
Le plan MCP complet du générique est identique avant/après, avec 56 focus et l'empreinte de disposition `ad2b3bb2de93a33b2152cd1e0a303ff29f29cec5c43123ba39d4a80a696e4716`.
L'inspection ciblée et le rendu du générique passent sans diagnostic bloquant.
Les fichiers d'arbres contenant des gardes de réattribution ont aussi été rendus avant/après ; leur disposition et leur contenu hors de ces gardes sont conservés.
Les diagnostics des anciens arbres ne sont pas présentés comme résolus par cette conversion.
La sélection au démarrage est une preuve statique du flux d'effets, pas une exécution du moteur par MCP.

Inspection avant : `hoi4-agent://workspace/auto_pax_franca/artifact/dd0777cb3d4c20183d200051ee5fdba9fc22e6c145359c52d40bfa30e94b23d8/9b9e3559b26be7b37209a6da177d09fbdac512f418c1072021b693d37a75e007/focus-inspect.c7c916727c3a8a2b.json`.
Inspection après : `hoi4-agent://workspace/auto_pax_franca/artifact/619a28fc460fa118802a4a4d257c53b2f08c495f680ef7f9f7a189cdfca18b4c/ba218682bd2681f53256b8955ee53aa07d6c158a39c4d71cb3cd84118a145516/focus-inspect.21f9d1f03abd82a8.json`.

La paire d'instantanés événementiels avant/après a été générée avec le sélecteur du fichier modifié `events/MTG_Britain.txt`, profondeur 1, sans expansion des helpers.
L'unique comparaison de cette paire échoue avec `EVENT_GRAPH_ARTIFACT_INVALID`, identifiant `entry_4b2e8aab856abda074c4f91c`.
Le défaut établi correspond aux deux blocs vanilla `on_release_as_puppet` de `common/on_actions/13_goe_on_actions.txt`, lignes 171 et 1758, auxquels le graphe attribue le même identifiant interne.
Ce n'est pas un doublon d'événement ajouté par le mod ; aucune modification du serveur ni réparation globale n'est effectuée.
La réponse ciblée contient encore ce nœud hors périmètre, ce qui empêche cette seule comparaison MCP.

La dérogation explicite de l'utilisateur est appliquée : comparaison directe exhaustive de chaque fichier surchargé à son état initial, après retrait inverse des seules gardes ajoutées.
Le reste du texte est identique, y compris les autres effets et références.
L'inventaire des événements effectivement chargés masque les fichiers vanilla remplacés au même chemin par le mod.
Il confirme une définition unique pour chacun des événements modifiés : `NSB_poland_royal_election.4`, `mtg_britain.113`, `mtg_usa_civil_war_democrats.20`, `wtt_warlord_vs_prc.2` et `bftb_greece.34`.
La vérification directe couvre les cinq fichiers de ces événements, pas seulement le sélecteur du rapport MCP.
Pour les pays sans événement modifié, aucune comparaison événementielle supplémentaire n'est requise.
Les gardes utilisent le tag exact : elles ne changent ni les pays dynamiques ni les autres utilisateurs d'un fichier régional.
Les appels espagnols dans les scopes explicites SPA/SPB/SPC/SPD et les appels présents uniquement dans des `effect_tooltip` sont conservés.

Aucun nouveau contenu national, aucune simplification du générique, aucun replace_path et aucune suppression globale.
Les dépendances nationales restantes sont conservées volontairement conformément au périmètre demandé.
Validation statique uniquement ; aucun lancement du jeu, aucun subagent.
Compétences utilisées : `hoi4-focus-trees`, `hoi4-events`, `hoi4-decisions-missions` ; aucune compétence créée ou modifiée.

### Registre pays par pays

#### Autriche — AUS

- Arbres antérieurs effectivement chargés : `austria_focus_tree` (214 focus, `common/national_focus/austria.txt`).
- Sélection DLC avant attribution : `austria_focus_tree` : Gotterdammerung, score 50.
- Résultat 1936 : `generic_focus`, 56 focus vanilla ; bloc du tag ajouté au on_startup commun.
- Histoire : `history/countries/AUS - Austria.txt` conservée ; aucune attribution ou priorité précomplétée incompatible en 1936.
- Réattributions : aucun appel non générique visant potentiellement ce tag dans les scripts inspectés ; les appels visant explicitement un autre tag restent intacts.
- Dépendances représentatives conservées : `AUS_heimwehr_support` dans `common/decisions/AUS.txt:539`; `AUS_sturmscharen_support` dans `common/decisions/AUS.txt:571`; `AUS_schutzbund_support` dans `common/decisions/AUS.txt:602`.
- Fichiers de ce commit : `common/on_actions/generic_focus_reset.txt`, `docs/specs/generic_focus_reset/progress.md`.
- Validation : preuve statique commune ci-dessus, garde exacte du tag, contenu extérieur aux gardes inchangé ; pas de validation en jeu.

#### Belgique — BEL

- Arbres antérieurs effectivement chargés : `belgium_focus` (173 focus, `common/national_focus/belgium.txt`).
- Sélection DLC avant attribution : `belgium_focus` : Gotterdammerung, score 10.
- Résultat 1936 : `generic_focus`, 56 focus vanilla ; bloc du tag ajouté au on_startup commun.
- Histoire : `history/countries/BEL - Belgium.txt` conservée ; aucune attribution ou priorité précomplétée incompatible en 1936.
- Réattributions : aucun appel non générique visant potentiellement ce tag dans les scripts inspectés ; les appels visant explicitement un autre tag restent intacts.
- Dépendances représentatives conservées : `BEL_unity_makes_strength` dans `common/decisions/BEL.txt:323`; `BEL_gold_reserves` dans `common/decisions/categories/BEL_decision_categories.txt:11`; `BEL_government_in_exile` dans `common/decisions/categories/BEL_decision_categories.txt:43`.
- Fichiers de ce commit : `common/on_actions/generic_focus_reset.txt`, `docs/specs/generic_focus_reset/progress.md`.
- Validation : preuve statique commune ci-dessus, garde exacte du tag, contenu extérieur aux gardes inchangé ; pas de validation en jeu.

#### France — FRA

- Arbres antérieurs effectivement chargés : `french_focus` (185 focus, `common/national_focus/france.txt`); `free_french_focus` (23 focus, `common/national_focus/free_france.txt`); `vichy_french_focus` (24 focus, `common/national_focus/vichy_france.txt`).
- Sélection DLC avant attribution : `french_focus` : sans condition DLC, score 10 ; `free_french_focus` : sans condition DLC, score 1 ; `vichy_french_focus` : sans condition DLC, score 1.
- Résultat 1936 : `generic_focus`, 56 focus vanilla ; conversion française existante revérifiée sans nouvelle modification de gameplay.
- Histoire : `history/countries/FRA - France.txt` conservée ; aucune attribution ou priorité précomplétée incompatible en 1936.
- Réattributions : gardes FRA déjà vérifiées dans la section France précédente.
- Dépendances représentatives conservées : `FRA_form_the_popular_front` dans `common/decisions/FRA.txt:13`; `FRA_destroy_the_counter_revolution` dans `common/decisions/FRA.txt:77`; `FRA_reorganize_the_aviation_industry` dans `common/decisions/FRA.txt:1336`.
- Fichiers de ce commit : `docs/specs/generic_focus_reset/progress.md`.
- Validation : preuve statique commune ci-dessus, garde exacte du tag, contenu extérieur aux gardes inchangé ; pas de validation en jeu.

#### Pays-Bas — HOL

- Arbres antérieurs effectivement chargés : `netherlands_focus` (152 focus, `common/national_focus/netherlands.txt`).
- Sélection DLC avant attribution : `netherlands_focus` : Man the Guns, score 10.
- Résultat 1936 : `generic_focus`, 56 focus vanilla ; bloc du tag ajouté au on_startup commun.
- Histoire : `history/countries/HOL - Holland.txt` conservée ; aucune attribution ou priorité précomplétée incompatible en 1936.
- Réattributions : aucun appel non générique visant potentiellement ce tag dans les scripts inspectés ; les appels visant explicitement un autre tag restent intacts.
- Dépendances représentatives conservées : `HOL_obtain_foreign_colonial_investments` dans `common/decisions/HOL.txt:69`; `HOL_obtain_foreign_colonial_investments_taog` dans `common/decisions/HOL.txt:70`; `HOL_prepare_the_inundation_lines` dans `common/decisions/HOL.txt:411`.
- Fichiers de ce commit : `common/on_actions/generic_focus_reset.txt`, `docs/specs/generic_focus_reset/progress.md`.
- Validation : preuve statique commune ci-dessus, garde exacte du tag, contenu extérieur aux gardes inchangé ; pas de validation en jeu.

#### Royaume-Uni — ENG

- Arbres antérieurs effectivement chargés : `british_focus` (164 focus, `common/national_focus/uk.txt`).
- Sélection DLC avant attribution : `british_focus` : sans condition DLC, score 10.
- Résultat 1936 : `generic_focus`, 56 focus vanilla ; bloc du tag ajouté au on_startup commun.
- Histoire : `history/countries/ENG - Britain.txt` conservée ; aucune attribution ou priorité précomplétée incompatible en 1936.
- Réattributions neutralisées uniquement pour ce tag : `common/on_actions/04_mtg_on_actions.txt` (2 appels).
- Dépendances représentatives conservées : `uk_burma_focus` dans `common/decisions/CHI_decisions.txt:3818`; `ENG_no_further_appeasement` dans `common/decisions/ENG.txt:101`; `uk_scandinavian_focus` dans `common/decisions/ENG.txt:102`.
- Fichiers de ce commit : `common/on_actions/04_mtg_on_actions.txt`, `common/on_actions/generic_focus_reset.txt`, `docs/specs/generic_focus_reset/progress.md`.
- Validation : preuve statique commune ci-dessus, garde exacte du tag, contenu extérieur aux gardes inchangé ; pas de validation en jeu.

#### Suisse — SWI

- Arbres antérieurs effectivement chargés : `swiss_focus` (160 focus, `common/national_focus/switzerland.txt`).
- Sélection DLC avant attribution : `swiss_focus` : By Blood Alone, score 10.
- Résultat 1936 : `generic_focus`, 56 focus vanilla ; bloc du tag ajouté au on_startup commun.
- Histoire : `history/countries/SWI - Switzerland.txt` conservée ; aucune attribution ou priorité précomplétée incompatible en 1936.
- Réattributions : aucun appel non générique visant potentiellement ce tag dans les scripts inspectés ; les appels visant explicitement un autre tag restent intacts.
- Dépendances représentatives conservées : `SWI_swiss_guiding_principles` dans `common/decisions/SWI.txt:131`; `SWI_case_north` dans `common/decisions/SWI.txt:286`; `SWI_case_west` dans `common/decisions/SWI.txt:327`.
- Fichiers de ce commit : `common/on_actions/generic_focus_reset.txt`, `docs/specs/generic_focus_reset/progress.md`.
- Validation : preuve statique commune ci-dessus, garde exacte du tag, contenu extérieur aux gardes inchangé ; pas de validation en jeu.

#### Bulgarie — BUL

- Arbres antérieurs effectivement chargés : `bulgarian_focus` (150 focus, `common/national_focus/bulgaria.txt`).
- Sélection DLC avant attribution : `bulgarian_focus` : Battle for the Bosporus, score 10.
- Résultat 1936 : `generic_focus`, 56 focus vanilla ; bloc du tag ajouté au on_startup commun.
- Histoire : `history/countries/BUL - Bulgaria.txt` conservée ; aucune attribution ou priorité précomplétée incompatible en 1936.
- Réattributions neutralisées uniquement pour ce tag : `common/on_actions/06_bftb_on_actions.txt` (2 appels).
- Dépendances représentatives conservées : `BUL_power_to_the_tsar` dans `common/decisions/BUL.txt:40`; `BUL_oppose_the_royal_dictatorship` dans `common/decisions/BUL.txt:48`; `BUL_cooperate_with_the_zveno` dans `common/decisions/BUL.txt:136`.
- Fichiers de ce commit : `common/on_actions/06_bftb_on_actions.txt`, `common/on_actions/generic_focus_reset.txt`, `docs/specs/generic_focus_reset/progress.md`.
- Validation : preuve statique commune ci-dessus, garde exacte du tag, contenu extérieur aux gardes inchangé ; pas de validation en jeu.

#### Espagne — SPR

- Arbres antérieurs effectivement chargés : `spanish_focus` (281 focus, `common/national_focus/spain.txt`).
- Sélection DLC avant attribution : `spanish_focus` : La Resistance, score 10.
- Résultat 1936 : `generic_focus`, 56 focus vanilla ; bloc du tag ajouté au on_startup commun.
- Histoire : `history/countries/SPR - Spain.txt` conservée ; aucune attribution ou priorité précomplétée incompatible en 1936.
- Réattributions : aucun appel non générique visant potentiellement ce tag dans les scripts inspectés ; les appels visant explicitement un autre tag restent intacts.
- Dépendances représentatives conservées : `SPA_the_phalanx_ascendant` dans `common/decisions/POR.txt:2094`; `SPA_unify_the_nationalist_front` dans `common/decisions/POR.txt:2096`; `SPA_the_iberian_pact` dans `common/decisions/POR.txt:2097`.
- Fichiers de ce commit : `common/on_actions/generic_focus_reset.txt`, `docs/specs/generic_focus_reset/progress.md`.
- Validation : preuve statique commune ci-dessus, garde exacte du tag, contenu extérieur aux gardes inchangé ; pas de validation en jeu.

#### Grèce — GRE

- Arbres antérieurs effectivement chargés : `greek_focus` (123 focus, `common/national_focus/greece.txt`).
- Sélection DLC avant attribution : `greek_focus` : Battle for the Bosporus, score 10.
- Résultat 1936 : `generic_focus`, 56 focus vanilla ; bloc du tag ajouté au on_startup commun.
- Histoire : `history/countries/GRE - Greece.txt` conservée ; aucune attribution ou priorité précomplétée incompatible en 1936.
- Réattributions : aucun appel non générique visant potentiellement ce tag dans les scripts inspectés ; les appels visant explicitement un autre tag restent intacts.
- Dépendances représentatives conservées : `GRE_the_right_to_rule` dans `common/decisions/GRE.txt:171`; `GRE_bolster_the_schachtplan` dans `common/decisions/GRE.txt:419`; `GRE_following_in_the_footsteps_of_giants` dans `common/decisions/GRE.txt:423`.
- Fichiers de ce commit : `common/on_actions/generic_focus_reset.txt`, `docs/specs/generic_focus_reset/progress.md`.
- Validation : preuve statique commune ci-dessus, garde exacte du tag, contenu extérieur aux gardes inchangé ; pas de validation en jeu.

#### Italie — ITA

- Arbres antérieurs effectivement chargés : `italian_focus` (314 focus, `common/national_focus/italy.txt`).
- Sélection DLC avant attribution : `italian_focus` : sans condition DLC, score 10.
- Résultat 1936 : `generic_focus`, 56 focus vanilla ; bloc du tag ajouté au on_startup commun.
- Histoire : `history/countries/ITA - Italy.txt` conservée ; aucune attribution ou priorité précomplétée incompatible en 1936.
- Réattributions neutralisées uniquement pour ce tag : `common/on_actions/03_wtt_on_actions.txt` (1 appel); `common/scripted_effects/ITA_scripted_effects.txt` (1 appel).
- Dépendances représentatives conservées : `ITA_triumph_in_africa_bba` dans `common/decisions/ETH.txt:23`; `ITA_war_with_greece` dans `common/decisions/GRE.txt:1263`; `ITA_befriend_turkey` dans `common/decisions/GRE.txt:1993`.
- Fichiers de ce commit : `common/on_actions/03_wtt_on_actions.txt`, `common/scripted_effects/ITA_scripted_effects.txt`, `common/on_actions/generic_focus_reset.txt`, `docs/specs/generic_focus_reset/progress.md`.
- Validation : preuve statique commune ci-dessus, garde exacte du tag, contenu extérieur aux gardes inchangé ; pas de validation en jeu.

#### Portugal — POR

- Arbres antérieurs effectivement chargés : `portuguese_focus` (126 focus, `common/national_focus/portugal.txt`).
- Sélection DLC avant attribution : `portuguese_focus` : La Resistance, score 10.
- Résultat 1936 : `generic_focus`, 56 focus vanilla ; bloc du tag ajouté au on_startup commun.
- Histoire : `history/countries/POR - Portugal.txt` conservée ; aucune attribution ou priorité précomplétée incompatible en 1936.
- Réattributions neutralisées uniquement pour ce tag : `common/on_actions/05_lar_on_actions.txt` (2 appels).
- Dépendances représentatives conservées : `POR_luso_tropicalism` dans `common/decisions/POR.txt:9`; `POR_revert_the_local_autonomy_policies` dans `common/decisions/POR.txt:78`; `POR_british_guns` dans `common/decisions/POR.txt:147`.
- Fichiers de ce commit : `common/on_actions/05_lar_on_actions.txt`, `common/on_actions/generic_focus_reset.txt`, `docs/specs/generic_focus_reset/progress.md`.
- Validation : preuve statique commune ci-dessus, garde exacte du tag, contenu extérieur aux gardes inchangé ; pas de validation en jeu.

#### Roumanie — ROM

- Arbres antérieurs effectivement chargés : `romanian_focus` (92 focus, `common/national_focus/romania.txt`).
- Sélection DLC avant attribution : `romanian_focus` : Death or Dishonor, score 10.
- Résultat 1936 : `generic_focus`, 56 focus vanilla ; bloc du tag ajouté au on_startup commun.
- Histoire : `history/countries/ROM - Romania.txt` conservée ; aucune attribution ou priorité précomplétée incompatible en 1936.
- Réattributions : aucun appel non générique visant potentiellement ce tag dans les scripts inspectés ; les appels visant explicitement un autre tag restent intacts.
- Dépendances représentatives conservées : `ROM_balkans_dominance` dans `common/decisions/GRE.txt:2693`; `ROM_force_abdication` dans `common/achievements.txt:1024`; `ROM_handle_the_king` dans `common/achievements.txt:1025`.
- Fichiers de ce commit : `common/on_actions/generic_focus_reset.txt`, `docs/specs/generic_focus_reset/progress.md`.
- Validation : preuve statique commune ci-dessus, garde exacte du tag, contenu extérieur aux gardes inchangé ; pas de validation en jeu.

#### Yougoslavie — YUG

- Arbres antérieurs effectivement chargés : `yugoslavian_focus` (118 focus, `common/national_focus/yugoslavia.txt`).
- Sélection DLC avant attribution : `yugoslavian_focus` : Death or Dishonor, score 10.
- Résultat 1936 : `generic_focus`, 56 focus vanilla ; bloc du tag ajouté au on_startup commun.
- Histoire : `history/countries/YUG - Yugoslavia.txt` conservée ; aucune attribution ou priorité précomplétée incompatible en 1936.
- Réattributions neutralisées uniquement pour ce tag : `common/on_actions/00_on_actions.txt` (1 appel).
- Dépendances représentatives conservées : `YUG_pan_balkan_workers_congress` dans `common/decisions/YUG.txt:197`; `YUG_invite_greece` dans `common/decisions/YUG.txt:422`; `YUG_invite_hungary` dans `common/decisions/YUG.txt:423`.
- Fichiers de ce commit : `common/on_actions/00_on_actions.txt`, `common/on_actions/generic_focus_reset.txt`, `docs/specs/generic_focus_reset/progress.md`.
- Validation : preuve statique commune ci-dessus, garde exacte du tag, contenu extérieur aux gardes inchangé ; pas de validation en jeu.

#### Estonie — EST

- Arbres antérieurs effectivement chargés : `estonia_tree` (59 focus, `common/national_focus/estonia.txt`).
- Sélection DLC avant attribution : `estonia_tree` : No Step Back, score 10.
- Résultat 1936 : `generic_focus`, 56 focus vanilla ; bloc du tag ajouté au on_startup commun.
- Histoire : `history/countries/EST - Estonia.txt` conservée ; aucune attribution ou priorité précomplétée incompatible en 1936.
- Réattributions neutralisées uniquement pour ce tag : `common/on_actions/07_nsb_on_actions.txt` (1 appel).
- Dépendances représentatives conservées : `EST_look_north` dans `common/decisions/BALTIC.txt:61`; `EST_rally_the_nation` dans `common/decisions/EST.txt:21`; `EST_era_of_silence` dans `common/decisions/EST.txt:30`.
- Fichiers de ce commit : `common/on_actions/07_nsb_on_actions.txt`, `common/on_actions/generic_focus_reset.txt`, `docs/specs/generic_focus_reset/progress.md`.
- Validation : preuve statique commune ci-dessus, garde exacte du tag, contenu extérieur aux gardes inchangé ; pas de validation en jeu.

#### Hongrie — HUN

- Arbres antérieurs effectivement chargés : `hungarian_focus` (99 focus, `common/national_focus/hungary.txt`); `wuw_hungarian_focus` (238 focus, `common/national_focus/hungary_wuw.txt`).
- Sélection DLC avant attribution : `hungarian_focus` : Death or Dishonor, score 10 ; `wuw_hungarian_focus` : Gotterdammerung, score 50.
- Résultat 1936 : `generic_focus`, 56 focus vanilla ; bloc du tag ajouté au on_startup commun.
- Histoire : `history/countries/HUN - Hungary.txt` conservée ; aucune attribution ou priorité précomplétée incompatible en 1936.
- Réattributions : aucun appel non générique visant potentiellement ce tag dans les scripts inspectés ; les appels visant explicitement un autre tag restent intacts.
- Dépendances représentatives conservées : `HUN_protect_czechoslovakia` dans `common/decisions/DOD_hungary.txt:11`; `HUN_elect_a_democratic_king` dans `common/decisions/DOD_hungary.txt:43`; `wuw_HUN_expand_the_hungarian_academy_of_sciences` dans `common/decisions/HUN.txt:20`.
- Fichiers de ce commit : `common/on_actions/generic_focus_reset.txt`, `docs/specs/generic_focus_reset/progress.md`.
- Validation : preuve statique commune ci-dessus, garde exacte du tag, contenu extérieur aux gardes inchangé ; pas de validation en jeu.

#### Lettonie — LAT

- Arbres antérieurs effectivement chargés : `latvia_tree` (56 focus, `common/national_focus/latvia.txt`).
- Sélection DLC avant attribution : `latvia_tree` : No Step Back, score 10.
- Résultat 1936 : `generic_focus`, 56 focus vanilla ; bloc du tag ajouté au on_startup commun.
- Histoire : `history/countries/LAT - Latvia.txt` conservée ; aucune attribution ou priorité précomplétée incompatible en 1936.
- Réattributions neutralisées uniquement pour ce tag : `common/on_actions/07_nsb_on_actions.txt` (1 appel).
- Dépendances représentatives conservées : `LAT_look_north` dans `common/decisions/BALTIC.txt:62`; `LAT_alignment_with_germany` dans `common/decisions/LAT.txt:17`; `LAT_banish_clemens` dans `common/decisions/LAT.txt:18`.
- Fichiers de ce commit : `common/on_actions/07_nsb_on_actions.txt`, `common/on_actions/generic_focus_reset.txt`, `docs/specs/generic_focus_reset/progress.md`.
- Validation : preuve statique commune ci-dessus, garde exacte du tag, contenu extérieur aux gardes inchangé ; pas de validation en jeu.

#### Lituanie — LIT

- Arbres antérieurs effectivement chargés : `lithuania_tree` (86 focus, `common/national_focus/lithuania.txt`).
- Sélection DLC avant attribution : `lithuania_tree` : No Step Back, score 10.
- Résultat 1936 : `generic_focus`, 56 focus vanilla ; bloc du tag ajouté au on_startup commun.
- Histoire : `history/countries/LIT - Lithuania.txt` conservée ; aucune attribution ou priorité précomplétée incompatible en 1936.
- Réattributions neutralisées uniquement pour ce tag : `common/on_actions/07_nsb_on_actions.txt` (1 appel).
- Dépendances représentatives conservées : `LIT_look_north` dans `common/decisions/BALTIC.txt:63`; `LIT_secure_a_loyal_cabinet` dans `common/decisions/LIT.txt:59`; `LIT_a_martial_prime_minister` dans `common/decisions/LIT.txt:61`.
- Fichiers de ce commit : `common/on_actions/07_nsb_on_actions.txt`, `common/on_actions/generic_focus_reset.txt`, `docs/specs/generic_focus_reset/progress.md`.
- Validation : preuve statique commune ci-dessus, garde exacte du tag, contenu extérieur aux gardes inchangé ; pas de validation en jeu.

#### Pologne — POL

- Arbres antérieurs effectivement chargés : `polish_focus` (301 focus, `common/national_focus/poland.txt`).
- Sélection DLC avant attribution : `polish_focus` : Poland: United and Ready ou No Step Back, score 10.
- Résultat 1936 : `generic_focus`, 56 focus vanilla ; bloc du tag ajouté au on_startup commun.
- Histoire : `history/countries/POL - Poland.txt` conservée ; aucune attribution ou priorité précomplétée incompatible en 1936.
- Réattributions neutralisées uniquement pour ce tag : `common/national_focus/poland.txt` (4 appels); `common/on_actions/07_nsb_on_actions.txt` (4 appels); `events/NSB_Poland.txt` (1 appel).
- Dépendances représentatives conservées : `POL_the_left_chairman` dans `common/decisions/POL.txt:301`; `POL_second_man_of_the_state` dans `common/decisions/POL.txt:331`; `POL_agrarian_reform` dans `common/decisions/POL.txt:372`.
- Fichiers de ce commit : `common/national_focus/poland.txt`, `common/on_actions/07_nsb_on_actions.txt`, `events/NSB_Poland.txt`, `common/on_actions/generic_focus_reset.txt`, `docs/specs/generic_focus_reset/progress.md`.
- Validation : preuve statique commune ci-dessus, garde exacte du tag, contenu extérieur aux gardes inchangé ; pas de validation en jeu.

#### Tchécoslovaquie — CZE

- Arbres antérieurs effectivement chargés : `czech_focus` (89 focus, `common/national_focus/czechoslovakia.txt`); `mu_czech_focus` (275 focus, `common/national_focus/czechoslovakia_mu.txt`).
- Sélection DLC avant attribution : `czech_focus` : Death or Dishonor, score 10 ; `mu_czech_focus` : Peace For Our Time, score 50.
- Résultat 1936 : `generic_focus`, 56 focus vanilla ; bloc du tag ajouté au on_startup commun.
- Histoire : `history/countries/CZE - Czechoslovakia.txt` conservée ; aucune attribution ou priorité précomplétée incompatible en 1936.
- Réattributions : aucun appel non générique visant potentiellement ce tag dans les scripts inspectés ; les appels visant explicitement un autre tag restent intacts.
- Dépendances représentatives conservées : `CZE_reform_the_naval_detachment` dans `common/decisions/CZE.txt:988`; `CZE_access_to_the_sea` dans `common/decisions/CZE.txt:991`; `CZE_airlift_soviet_support` dans `common/decisions/CZE.txt:1117`.
- Fichiers de ce commit : `common/on_actions/generic_focus_reset.txt`, `docs/specs/generic_focus_reset/progress.md`.
- Validation : preuve statique commune ci-dessus, garde exacte du tag, contenu extérieur aux gardes inchangé ; pas de validation en jeu.

#### URSS — SOV

- Arbres antérieurs effectivement chargés : `soviet_focus` (311 focus, `common/national_focus/soviet.txt`).
- Sélection DLC avant attribution : `soviet_focus` : sans condition DLC, score 10.
- Résultat 1936 : `generic_focus`, 56 focus vanilla ; bloc du tag ajouté au on_startup commun.
- Histoire : `history/countries/SOV - Soviet union.txt` conservée ; aucune attribution ou priorité précomplétée incompatible en 1936.
- Réattributions neutralisées uniquement pour ce tag : `common/on_actions/03_wtt_on_actions.txt` (1 appel); `common/scripted_effects/SOV_scripted_effects.txt` (1 appel).
- Dépendances représentatives conservées : `SOV_demand_balkan_submission` dans `common/decisions/GRE.txt:1496`; `SOV_expand_the_agitprop` dans `common/decisions/SOV.txt:1957`; `SOV_collectivist_propaganda` dans `common/decisions/SOV.txt:2713`.
- Fichiers de ce commit : `common/on_actions/03_wtt_on_actions.txt`, `common/scripted_effects/SOV_scripted_effects.txt`, `common/on_actions/generic_focus_reset.txt`, `docs/specs/generic_focus_reset/progress.md`.
- Validation : preuve statique commune ci-dessus, garde exacte du tag, contenu extérieur aux gardes inchangé ; pas de validation en jeu.

#### Danemark — DEN

- Arbres antérieurs effectivement chargés : `danish_focus` (175 focus, `common/national_focus/denmark.txt`).
- Sélection DLC avant attribution : `danish_focus` : Arms Against Tyranny, score 10.
- Résultat 1936 : `generic_focus`, 56 focus vanilla ; bloc du tag ajouté au on_startup commun.
- Histoire : `history/countries/DEN - Denmark.txt` conservée ; aucune attribution ou priorité précomplétée incompatible en 1936.
- Réattributions : aucun appel non générique visant potentiellement ce tag dans les scripts inspectés ; les appels visant explicitement un autre tag restent intacts.
- Dépendances représentatives conservées : `DEN_overthrow_the_government` dans `common/decisions/DEN.txt:467`; `DEN_social_stability` dans `common/decisions/DEN.txt:641`; `DEN_declare_neutrality` dans `common/decisions/DEN.txt:743`.
- Fichiers de ce commit : `common/on_actions/generic_focus_reset.txt`, `docs/specs/generic_focus_reset/progress.md`.
- Validation : preuve statique commune ci-dessus, garde exacte du tag, contenu extérieur aux gardes inchangé ; pas de validation en jeu.
