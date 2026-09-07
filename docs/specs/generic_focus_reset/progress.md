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
