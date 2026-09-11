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

Les cinq noms et descriptions existent en français et en anglais dans les fichiers `rhenish_resistance_l_<langue>.yml`.
Chaque esprit possède un `custom_modifier_tooltip` qui affiche explicitement « Renseignement de l’Allemagne sur la France » et quatre lignes chiffrées, une par domaine, avec le gain en points absolus.
Le texte explique aussi l'actualisation quotidienne, les montées/descentes et la disparition du bonus en l'absence de département occupé éligible.
Les cinq clés `rhenish_<palier>_intel_points` de chaque langue sont des projections d'affichage des constantes `@<palier>_intel` ; elles sont partagées par les titres et les infobulles, et le test rejette tout écart avec les valeurs runtime.
Elles ne règlent aucun effet de jeu.

Les vingt jetons portent des noms quantifiés, par exemple « Réseaux rhénans — Civil : +10 pts ».
Leur description indique l'apport continu de résistance, le bénéficiaire allemand, la cible française, le nom exact de l'esprit français et le gain du domaine concerné.
Chaque description rappelle que le montant suit le maximum de résistance et peut augmenter, diminuer ou disparaître.
Les cinq esprits réutilisent `picture = DEN_occupation_laws` : sprite vanilla `GFX_idea_DEN_occupation_laws`, défini dans `interface/ideas.gfx`, texture `gfx/interface/ideas/idea_DEN_occupation_laws.dds` présente dans l'installation.
Les jetons utilisent le sprite vanilla `GFX_contact_resistance_bg`, défini dans `interface/operationoverview.gfx` vers `gfx/interface/operations/contact_resistance_token.dds`, comme `token_resistance_contacts` ; l'icône représente ainsi leur source rhénane.
Aucun asset ni fichier GFX supplémentaire n'est nécessaire.

### Présentation du registre allemand

Le registre natif regroupe les jetons dans `INTEL_STATIC_SOURCE_OperationTokens` et qualifie les sources de ce type avec `INTEL_STATIC_INFO`, dans `localisation/english/intel_ledger_l_english.yml` vanilla.
Cette catégorie technique n'implique pas que la valeur du système rhénan reste constante : les callbacks remplacent toujours les jetons au changement de palier.
Le schéma documenté des jetons n'offre aucun champ de catégorie de registre propre à un jeton.
La capture utilisateur confirme que l'infobulle du total civil affiche uniquement cette ligne agrégée et son qualificatif : les noms et descriptions individuels des jetons n'y sont pas affichés.
Les fichiers `localisation/{french,english}/replace/rhenish_intel_ledger_l_<langue>.yml` remplacent donc directement les deux clés natives, avec la priorité `replace` documentée dans la section « Replacing » du wiki hors ligne `Localisation`.
La ligne française devient « Opérations et réseaux de résistance : <montant> (apport maintenu) » ; l'anglais utilise « Operations and resistance networks » et « maintained contribution ».
Le paramètre moteur `$AMOUNT|.1+%%$` reste intact : il représente toujours le total des jetons applicables au domaine et à la relation affichés, y compris les autres opérations.
Le qualificatif signifie que l'apport est maintenu par sa source ; il n'implique pas que cette source ou sa valeur soit permanente.
Ces deux textes sont partagés par tous les pays ; le qualificatif concerne aussi les autres sources natives de la même catégorie, sans modifier leurs effets ou leur durée.
La ligne ne constitue pas une ventilation séparée du bonus rhénan : les esprits et descriptions des jetons fournissent ce détail.

## Références consultées

Racine vanilla : `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV`.

- `common/operation_tokens/_documentation.md` : relation origine/cible, durée, non-cumul, limitation à une source par jeton et quatre domaines admis.
- `common/operation_tokens/00_OperationTokens.txt` : `token_civilian`, `token_army`, `token_navy`, `token_airforce`, chacun avec `intel_gain = 10` ; `token_resistance_contacts` apporte cinq points terrestres.
- `documentation/effects_documentation.md` : scopes pays et paramètres de `add_operation_token`, `remove_operation_token` et variables temporaires.
- `documentation/triggers_documentation.md`, `dynamic_variables_documentation.md`, `modifiers_documentation.md` : comparaisons, résistance native et stabilité ; distinction entre gains dirigés et facteurs de renseignement.
- `documentation/script_concept_documentation.md` et `common/script_constants/documentation.md` : constantes et limites des champs compatibles.
- Wiki hors ligne : pages centrales requises, `Idea modding` pour callbacks/annulation, `Data structures` pour temporaire sans scope, `Effects`, `Modifiers`, `Intelligence agency modding` et `On actions`.
- Infobulles : section « Tooltip modification » de `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md` et précédent `BEL_chasseurs_ardennais` dans `common/ideas/belgium.txt`, avec `custom_modifier_tooltip` dans le bloc `modifier`.

## Vérifications et limites

`.tools/tests/test_rhenish_national_spirits.py` interprète le sous-ensemble des sources réellement utilisées, y compris les callbacks d'idées et les définitions de jetons.
Il couvre 240 combinaisons : les quatre États gagnants, six situations initiales (aucun esprit ou chacun des cinq) et dix valeurs de résistance dont les bornes exactes et 0,001 point au-dessus.
Chaque combinaison est suivie de trois actualisations sans aucune nouvelle opération d'idée ou de jeton.
Les scénarios supplémentaires couvrent la chute du maximum, sa perte par propriétaire/contrôleur/core, l'absence d'État éligible, l'annulation native simulée, le retour dans le périmètre, les maxima ex æquo et un État français extérieur à la liste à 100 de résistance.
Les assertions vérifient les quatre domaines à la bonne valeur, la relation GER → FRA, la stabilité persistante, la conservation des idées et jetons tiers, l'absence de renseignement local et l'absence d'écriture dans la résistance native.
Les vérifications de présentation développent les références de localisation françaises et anglaises, contrôlent les quatre montants dans chaque esprit et les vingt noms de sources, puis les comparent aux constantes des jetons.
Elles contrôlent aussi le nom du palier français, la cible, le bénéficiaire, le caractère continu de la source, sa fréquence quotidienne et l'icône de résistance.
Le contrôle du registre impose les deux clés natives dans les fichiers prioritaires `replace` français et anglais, conserve leur paramètre de montant agrégé et rejette l'ancien qualificatif « fixe ».
Le test importe aussi `.tools/tests/test_rhenish_resistance.py`, dont les 240 cas locaux restent valides avec les six effets d'État inchangés.

Aucune surface MCP événementielle, cartographique, de focus, de technologie, de GUI ou de probabilités scriptées n'est modifiée ; les hooks existants ne sont pas édités.
Les inspections antérieures du système local restent documentées dans `implementation.md` ; aucune comparaison MCP d'événement n'est revendiquée pour cette tranche sans événement.
Skills utilisés : `hoi4-events` et `hoi4-feature-assets`, sans modification de skill ni subagent.
Aucune simplification ni omission par rapport au contrat précisé ; la seule contribution de renseignement de ce système est celle des quatre jetons du palier français actif.
Les contrôles sont statiques et simulés sur les scripts, sans exécution de HOI4 ; l'affichage et les bornes finales du renseignement restent ceux du moteur et n'ont pas été observés en jeu.
Aucune dépendance de progression existante n'est réécrite ; les mécanismes natifs de résistance et d'occupation restent décrits dans la spécification locale.

## Extensions

Aucune extension n'est prévue dans cette tranche ; toute interaction ultérieure avec décisions ou opérations devra préserver la propriété des jetons par les callbacks de l'esprit français.

## Notifications de changement national

Après l’actualisation existante des quatre États et de l’esprit national, FRA humaine reçoit un événement informatif unique si un palier national existant augmente ou diminue, même lors d’un saut de plusieurs paliers.
Le démarrage et le rechargement sont silencieux ; l’initialisation sans esprit précédent, un palier national identique, les seuls changements locaux et l’absence d’État éligible ne produisent aucune notification.
Le nettoyage national existant est conservé.
Le texte français indique simplement « La résistance dans les départements rhénan continue de s'aggraver » à la hausse et « La résistance dans les départements rhénan semble se calmer » à la baisse, avec traduction anglaise.
Le bouton « inquiétant » à la hausse ou « rassurant » à la baisse expose les effets nationaux et rappelle que les pénalités locales dépendent de chaque État, sans effet de gameplay au clic.
Les événements `rhenish_notification.1` et `.2` sont définis dans `events/rhenish_notifications.txt`, avec la présentation native des événements pays et l’image vanilla `GFX_report_event_french_resistance_02` ; aucun nouvel asset n’est nécessaire.
Les libellés dynamiques sont dans `common/scripted_localisation/rhenish_notifications.txt` et les textes dans les deux fichiers existants `rhenish_resistance_l_<langue>.yml`.
