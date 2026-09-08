# Esprit national de résistance rhénane

## Contrat accepté

Cible : installation HOI4 1.19.2.0.a729, sans lancement du jeu ni recherche Internet.
La précision utilisateur définit le renseignement en points absolus dans les quatre domaines : 15 % de renseignement civil allemand sur FRA avec +10 points donne 25 %, hors bornes ou autres calculs du moteur.
Il ne s'agit pas d'une multiplication relative de 15 par 1,10.
Cet esprit français de système est expressément autorisé au démarrage par cette demande, après la suppression antérieure des esprits initiaux.

| Maximum éligible | Esprit français | Points GER → FRA par domaine | Stabilité persistante |
| --- | --- | ---: | ---: |
| 0–20 inclus | Occupation Rhénane | +5 | 0 |
| >20–40 inclus | Inquiétude Rhénane | +10 | −5 % |
| >40–60 inclus | Crise Rhénane | +20 | −10 % |
| >60–80 inclus | Insurrection Rhénane | +30 | −15 % |
| >80–100 inclus | Soulèvement Rhénan | +50 | −25 % |

## Agrégation et cycle de vie

Le passage existant sur Sarre (42), Roer (1082), Rhin-et-Moselle (1083) et Mont-Tonnerre (1084) conserve `rhenish_resistance_eligible` : État de cette liste, possédé ET contrôlé par FRA, sans core FRA.
Les on_actions existants `on_startup` et `on_daily_FRA` restent inchangés ; aucune nouvelle boucle n'est installée.
Le même passage actualise les effets locaux et calcule le maximum de `resistance`, sans moyenne, somme, arrondi ni écriture dans la variable moteur.
La temporaire non scopée `rhenish_max_resistance` repart de −1 à chaque appel ; les seuils proviennent des constantes locales déjà utilisées par les paliers d'État.
Un seul État au-dessus de 80 suffit donc à sélectionner le cinquième esprit, quelle que soit la résistance des trois autres.
Les comparaisons strictes descendantes donnent les bornes supérieures inclusives du tableau et permettent aussi les diminutions.

Depuis l'absence d'esprit ou un palier existant, le sélecteur conserve exactement un esprit de la famille lorsque le périmètre est non vide.
Si l'esprit attendu est déjà présent, aucune attribution ni suppression n'est exécutée.
Sinon, le nettoyage partagé retire les anciens esprits de cette famille avant l'ajout du palier attendu ; il préserve tous les autres esprits, lois et catégories.
Sans État éligible, il retire l'esprit et ses jetons.
Le bloc `cancel` de chaque idée couvre aussi la disparition du périmètre par l'annulation native des idées ; l'annulation déclenche `on_remove` selon la documentation des idées.
L'héritage en guerre civile est désactivé pour éviter de dupliquer les callbacks destinés à FRA.
La réactivité du sélecteur reste quotidienne ; aucun événement de transfert ni autre système n'est réécrit.

## Renseignement ciblé

`common/operation_tokens/rhenish_resistance.txt` définit vingt jetons propres à cette famille : cinq paliers multipliés par quatre domaines.
Chaque esprit français exécute dans `GER` quatre `add_operation_token = { tag = FRA token = ... }` dans `on_add` et les quatre `remove_operation_token` correspondants dans `on_remove`.
Le bénéficiaire est donc exclusivement GER et la cible exclusivement FRA.
Les jetons vanilla d'infiltration et les relations envers les autres pays ne sont pas modifiés.
Les identifiants propres à cette famille ne sont consommés par aucune opération du mod ou de vanilla.

Un jeton ne prend en charge qu'un `intel_source` : `civilian`, `army`, `navy` ou `airforce`.
Son `intel_gain` représente des points de renseignement pour ce domaine ; les quatre jetons actifs apportent chacun la valeur du palier, et non quatre fois cette valeur dans chaque domaine.
Le jeton est non cumulable avec lui-même pour une même relation et reste actif jusqu'à son retrait ; les callbacks réalisent ce retrait lors de chaque changement ou annulation de l'esprit.
Il n'y a ni `add_intel` répété, ni facteur d'agence allemand global, ni renseignement français accru, ni bonus de tous les pays contre FRA.
Les modificateurs `*_intel_to_others`, `local_intel_to_enemies` et `enemy_intel_network_gain_factor_over_occupied_tag` ne conviennent pas à cette relation et ne sont pas utilisés.
Les cinq modificateurs d'État ne contiennent aucun effet de renseignement, comme avant cette tranche ; leurs six contributions locales sont préservées sans duplication nationale.
La stabilité est uniquement `stability_factor` dans l'esprit, sans `add_stability` ni perte périodique.

## Valeurs, textes et icônes

Les seuils et la sentinelle sont centralisés dans `common/script_constants/rhenish_resistance.txt`.
Les cinq valeurs de stabilité n'existent qu'une fois dans les constantes `@..._stability` de `common/ideas/rhenish_resistance.txt`.
Les cinq gains de renseignement n'existent qu'une fois dans les constantes `@..._intel` de `common/operation_tokens/rhenish_resistance.txt`, chacun partagé par les quatre domaines.
Les constantes de fichier sont utilisées pour ces champs numériques statiques ; la prise en charge de `constant:` n'est pas attestée dans ces champs, contrairement aux champs variables du sélecteur.

Les cinq noms et descriptions existent en français et en anglais dans les fichiers `rhenish_resistance_l_<langue>.yml`, avec les noms et descriptions des quatre sources de renseignement.
Les cinq esprits réutilisent `picture = DEN_occupation_laws` : sprite vanilla `GFX_idea_DEN_occupation_laws`, défini dans `interface/ideas.gfx`, texture `gfx/interface/ideas/idea_DEN_occupation_laws.dds` présente dans l'installation.
Les jetons utilisent les sprites vanilla `GFX_infiltrate_civilian_bg`, `GFX_infiltrate_army_bg`, `GFX_infiltrate_navy_bg` et `GFX_infiltrate_air_bg`, comme les quatre jetons d'infiltration vanilla.
Aucun asset ni fichier GFX supplémentaire n'est nécessaire.

## Références consultées

Racine vanilla : `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV`.

- `common/operation_tokens/_documentation.md` : relation origine/cible, durée, non-cumul, limitation à une source par jeton et quatre domaines admis.
- `common/operation_tokens/00_OperationTokens.txt` : `token_civilian`, `token_army`, `token_navy`, `token_airforce`, chacun avec `intel_gain = 10` ; `token_resistance_contacts` apporte cinq points terrestres.
- `documentation/effects_documentation.md` : scopes pays et paramètres de `add_operation_token`, `remove_operation_token` et variables temporaires.
- `documentation/triggers_documentation.md`, `dynamic_variables_documentation.md`, `modifiers_documentation.md` : comparaisons, résistance native et stabilité ; distinction entre gains dirigés et facteurs de renseignement.
- `documentation/script_concept_documentation.md` et `common/script_constants/documentation.md` : constantes et limites des champs compatibles.
- Wiki hors ligne : pages centrales requises, `Idea modding` pour callbacks/annulation, `Data structures` pour temporaire sans scope, `Effects`, `Modifiers`, `Intelligence agency modding` et `On actions`.

## Vérifications et limites

`.tools/tests/test_rhenish_national_spirits.py` interprète le sous-ensemble des sources réellement utilisées, y compris les callbacks d'idées et les définitions de jetons.
Il couvre 240 combinaisons : les quatre États gagnants, six situations initiales (aucun esprit ou chacun des cinq) et dix valeurs de résistance dont les bornes exactes et 0,001 point au-dessus.
Chaque combinaison est suivie de trois actualisations sans aucune nouvelle opération d'idée ou de jeton.
Les scénarios supplémentaires couvrent la chute du maximum, sa perte par propriétaire/contrôleur/core, l'absence d'État éligible, l'annulation native simulée, le retour dans le périmètre, les maxima ex æquo et un État français extérieur à la liste à 100 de résistance.
Les assertions vérifient les quatre domaines à la bonne valeur, la relation GER → FRA, la stabilité persistante, la conservation des idées et jetons tiers, l'absence de renseignement local et l'absence d'écriture dans la résistance native.
Le test importe aussi `.tools/tests/test_rhenish_resistance.py`, dont les 240 cas locaux restent valides avec les six effets d'État inchangés.

Aucune surface MCP événementielle, cartographique, de focus, de technologie, de GUI ou de probabilités scriptées n'est modifiée ; les hooks existants ne sont pas édités.
Les inspections antérieures du système local restent documentées dans `implementation.md` ; aucune comparaison MCP d'événement n'est revendiquée pour cette tranche sans événement.
Skills utilisés : `hoi4-events` et `hoi4-feature-assets`, sans modification de skill ni subagent.
Aucune simplification ni omission par rapport au contrat précisé ; la seule contribution de renseignement de ce système est celle des quatre jetons du palier français actif.
Les contrôles sont statiques et simulés sur les scripts, sans exécution de HOI4 ; l'affichage et les bornes finales du renseignement restent ceux du moteur et n'ont pas été observés en jeu.
Aucune dépendance de progression existante n'est réécrite ; les mécanismes natifs de résistance et d'occupation restent décrits dans la spécification locale.

## Extensions

Aucune extension n'est prévue dans cette tranche ; toute interaction ultérieure avec décisions ou opérations devra préserver la propriété des jetons par les callbacks de l'esprit français.
