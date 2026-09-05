# Découpage territorial de la rive gauche du Rhin

## Objet

Ce paquet établit le découpage territorial rhénan du scénario de 1936 sans modifier les provinces, les rivières, les adjacences, les chemins de fer ni les nœuds logistiques de la carte vanilla.

La France possède et contrôle la Sarre, le Roer, Rhin-et-Moselle et Mont-Tonnerre au début de la partie, sans noyau ni revendication française.

Les noyaux allemands, rhénans et prussiens sont conservés dans les quatre départements. Le noyau hessois demeure dans les deux États allemands de Hesse et de Hesse-Rhénan.

## États

| ID | Nom | Provinces | Préfecture | Propriétaire initial | Population | Infrastructure | Usines civiles | Usines militaires |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| 42 | Sarre | 11435, 11470, 9575, 11531 | Sarrebruck (11531) | FRA | 1 386 454 | 4 | 1 | 0 |
| 51 | Rhénanie | 529, 3512, 6469, 6570, 9482 | Essen (6469) | GER | 3 306 409 | 4 | 3 | 2 |
| 55 | Hesse | 564, 3397, 3524, 6549, 9524, 9547, 11445, 11533 | Cassel (564) | GER | 2 550 000 | 4 | 0 | 1 |
| 1082 | Roer | 3444, 587, 9522 | Aix-la-Chapelle (9522) | FRA | 2 101 363 | 4 | 1 | 1 |
| 1083 | Rhin-et-Moselle | 3547, 11494, 3423 | Coblence (3423) | FRA | 1 397 804 | 3 | 1 | 0 |
| 1084 | Mont-Tonnerre | 11547, 563, 3558, 11560 | Mayence (11560) | FRA | 1 228 471 | 4 | 1 | 0 |
| 1085 | Hesse-Rhénan | 589, 3574, 6444, 6488, 9486 | Francfort (6488) | GER | 1 000 216 | 4 | 2 | 0 |

La zone française annexée compte quatorze provinces. La prévalidation initiale avait incorrectement classé la province 3512 sur la rive gauche du Rhin ; le test en jeu sur HOI4 1.19 a confirmé sa position sur la rive droite, ce qui impose son maintien dans l’État allemand 51. La province 3444 reste dans Roer conformément au tracé demandé.

Le reliquat allemand est subdivisé entre la Rhénanie, la Hesse et le nouvel État 1085 de Hesse-Rhénan. La Rhénanie conserve ses cinq provinces et reçoit explicitement le statut de zone démilitarisée. Hesse-Rhénan reçoit Francfort, Wiesbaden, les provinces 589, 3574 et 9486, ainsi que deux usines civiles, le barrage de la province 9486 et les extensions industrielles datées de 1939. La Hesse conserve Cassel, huit provinces, une usine militaire et ses extensions datées de 1939.

Les champs `owner` et `controller` établissent explicitement la propriété et le contrôle initiaux à la date de départ.

Les préfectures sont des désignations administratives et narratives : conformément au cahier des charges, Aix-la-Chapelle et Trèves ne reçoivent pas de VP artificiellement supérieur à Cologne ou Sarrebruck, de sorte que le marqueur de capitale mécanique de Roer demeure Cologne.

Les ressources de l’ancien État 42 restent dans la Sarre et celles de l’ancien État 51 restent dans le reliquat allemand de Rhénanie. Hesse et Hesse-Rhénan disposent chacune de 8 unités de charbon dans le découpage retenu.

Les ajouts vanilla non fortifiés du signet de 1939 restent également dans leurs reliquats d’origine : la Sarre conserve le radar et les raffineries synthétiques de l’État 42, tandis que la Rhénanie conserve l’extension de la base aérienne et le radar de l’État 51. Les forts provinciaux datés du Westwall et l’historique de démilitarisation sont volontairement écartés, puisque la rive gauche annexée constitue une frontière française militarisable.

Le barrage hessois est placé dans la province 9486 de Hesse-Rhénan.

## Population

La population de chacun des trois États vanilla a été distribuée entre ses successeurs au prorata du nombre de pixels terrestres de chaque province mesuré par `hoi4.map_inspect`.

La méthode du plus fort reste a été appliquée aux valeurs entières afin de préserver exactement chaque total source sans duplication ni perte.

| Source vanilla | Parts en pixels | Répartition de population |
| --- | --- | --- |
| État 42, 701 pixels | Sarre 321 ; Rhin-et-Moselle 153 ; Mont-Tonnerre 227 | 1 386 454 ; 660 833 ; 980 452 |
| État 51, 617 pixels | Roer 211 ; Rhin-et-Moselle 74 ; Rhénanie 332 | 2 101 363 ; 736 971 ; 3 306 409 |
| État 55, 1 072 pixels | Mont-Tonnerre ; Hesse ; Hesse-Rhénan | 248 019 ; 2 550 000 ; 1 000 216 |

Les populations sources de 3 027 739, 6 144 743 et 3 798 235 habitants totalisent 12 970 717 habitants, soit exactement le total des sept États après découpage. La subdivision manuelle de l’ancien reliquat de Nassau conserve son total de 3 550 216 habitants entre Hesse et Hesse-Rhénan.

## Réseau, bâtiments et région stratégique

Les 52 entrées initialement réattribuées dans `map/buildings.txt` ont reçu l’ID d’État correspondant à leur province. La correction de la frontière réattribue ensuite à l’État 51 les quatre entrées situées dans la province 3512. La création de Hesse-Rhénan réattribue enfin 17 positions de l’État 55 vers l’État 1085 sans modifier leurs coordonnées, leur type ou leur province résolue. Le fichier final conserve donc 65 réattributions par rapport à vanilla.

Les chemins de fer et les nœuds logistiques de Cologne (587) et Sarrebruck (11531) restent définis par les fichiers vanilla et n’ont pas été réécrits.

La région stratégique 7 conserve strictement sa composition et reçoit seulement le nom localisé « Région rhénane ».

## Compatibilité des mécanismes vanilla

La remilitarisation allemande et ses événements ne manipulent plus les territoires français de la rive gauche et restent attachés au seul État démilitarisé de Bade (978).

La construction du Westwall ne place plus de fortifications dans les provinces françaises et reste attachée à Bade, faute de tracé allemand de remplacement autorisé.

Les investissements sidérurgiques allemands restent attachés au reliquat industriel de Rhénanie (51).

Le barrage de la Rur est associé à Rhin-et-Moselle (1083) et le focus allemand correspondant est contourné lorsque l’Allemagne ne contrôle pas cet État.

Les stratégies de front françaises et allemandes visent les reliquats de Rhénanie, de Hesse et de Hesse-Rhénan au lieu de considérer la Sarre française comme un territoire allemand.

Les frontières naturelles françaises revendiquent les quatre départements sans créer automatiquement un objectif de guerre contre l’Allemagne qui les a déjà cédés.

La désunion de l’Allemagne exclut les quatre départements français du transfert générique vers la Prusse, mais laisse la Rhénanie allemande suivre le traitement normal.

Les décisions de formation qui énumèrent explicitement les territoires allemands exigent et intègrent aussi les États 1082, 1083, 1084 et 1085. Le succès autrichien portant sur le contrôle de l’Allemagne exige également Hesse-Rhénan.

Les deux décisions allemandes de développement occidental incluent Hesse-Rhénan dans leurs conditions, leur surbrillance et leurs effets. Les stratégies de front françaises et allemandes qui couvraient déjà la Hesse incluent aussi l’État 1085, sans changement de poids. Le partage territorial de Yalta classe Hesse-Rhénan avec l’Allemagne occidentale.

Les chaînes alternatives de remilitarisation et d’Anschluss utilisent Bade (978), tandis que les objectifs de guerre allemands alternatifs conservent le reliquat allemand de Rhénanie (51).

## Ressources visuelles

Aucune icône, texture, définition de sprite ou autre ressource visuelle n’est requise pour ce découpage.

## Preuves MCP

L’inspection préalable `hoi4.map_inspect` a établi la révision `11d579532fccd67de591e0e7b1c3a9523972cea02072cf5cbb851197d2cfb631` avec trois États sources, 32 provinces rhénanes connues et aucune lacune géométrique.

Le rendu préalable `hoi4.map_render` a produit le PNG `cb750430b46533bcce77d3cac8b68954bd5bdf655027b81d2879ea17c33cf5cb`.

Les tentatives déclaratives `hoi4.map_rewrite` ont été automatiquement annulées par le serveur : les créations dépassaient sa limite structurelle et une mise à jour minimale a échoué sur des références de provinces vanilla considérées à tort comme non résolues par l’index partagé.

Le repli manuel a été explicitement autorisé après ces annulations et reprend sans variation le plan contrôlé par l’inspection préalable.

L’inspection finale `hoi4.map_inspect` a établi la révision `f9b5b49ac89e5ce32c96aeabfa8d2633059b53653a76d092a06d415e9e4777bc`, six États inspectés, les 32 provinces attendues, 2 390 pixels terrestres, aucune province inconnue et aucune géométrie manquante.

Les contrôles MCP finaux des fichiers et définitions, de la géométrie, de l’appartenance aux États et à la région stratégique, des adjacences, des nœuds logistiques et des voies ferrées réussissent.

Le contrôle global des positions signale des `floating_harbor` vanilla hors périmètre à partir de la ligne 26352 du fichier complet surchargé ; ces lignes sont inchangées par rapport au fichier vanilla et aucune des 52 lignes rhénanes réaffectées n’est concernée.

Le rendu final `hoi4.map_render` a produit le PNG `c3e31ced3faeab8c6280ecf89141a95b7cf21131ee66d62eae2fed824caa9748`.

La comparaison avant/après montre le passage de trois enveloppes territoriales vanilla à six États sans changement des 32 géométries provinciales, de la région stratégique 7 ni des réseaux ferroviaires et logistiques.

### Correction de la province 3512

Le contrôle préalable ciblé de la correction a repris la révision `f9b5b49ac89e5ce32c96aeabfa8d2633059b53653a76d092a06d415e9e4777bc`. Le rendu avec bâtiments, chemins de fer, ravitaillement et connexions a produit le PNG `81ba729582a0b8d4bac3cc2e42d32790ded0426b58c514c551d3f75b8c620c1f` alors que 3512 appartenait encore à Roer.

L’opération ciblée `move_state_provinces` de `hoi4.map_rewrite` a été appelée pour déplacer uniquement 3512 de 1082 vers 51 et faire suivre ses bâtiments, positions, nœuds et voies ferrées. Le serveur l’a annulée avant écriture avec `REWRITE_STRUCTURE_LIMIT`; le repli manuel strictement équivalent a ensuite été explicitement autorisé.

L’inspection finale ciblée établit la révision `38616328b693592458dd5c0a03c1a15e41905094a5f838e8951e8200eba4f8d9` : 3512 appartient à l’État allemand 51, 3444 reste dans Roer, et les contrôles de géométrie, d’appartenance, d’adjacence, de ravitaillement et de voies ferrées réussissent. Le rendu final produit le PNG `5e545cf4218cf827356a72109b1e7ccd2694fa7b31ed78b7d471ab5c79b4789a`. La comparaison avec le rendu préalable confirme le recul de la frontière française sur la rive gauche du Rhin sans modification du contour de 3512 ni d’aucune autre province.

Les arbres nationaux allemand et français ont également été inspectés et rendus après adaptation à la révision MCP `1263eaa4ed2e5bcb4976e74fd9706bc56ff54d927051c83c6aea100b077bae5f`. Leurs nombres de nœuds et leurs hashes de disposition restent identiques aux preuves préalables : `abe189340cf67a71e15d6e08eb7de37e97437430f03d7a77c4c29789f50df3b1` pour l’Allemagne et `04bd763dbc684d1f376d0b038bc2b458e87918fca6f2da94d1bf33ba3d52c553` pour la France. Les adaptations territoriales n’ont donc déplacé ni supprimé aucun focus.

La chaîne événementielle allemande affectée a été inspectée puis rendue après adaptation. Le rendu final ciblé autour de `germany.60` est établi à la révision `886126ea4c9e5e03e47e0481f483e5471d68b00a83842683e2da0695065db03d`, avec le PNG `35afe90fdcdbc7501927361b1cafd30f45b9e764bf7cdce21a84fe99d2487755`. Les diagnostics globaux restant signalés par l’outil appartiennent au corpus vanilla complet ; aucun diagnostic bloquant n’est associé à la chaîne ciblée.

### Subdivision manuelle de la Hesse

La subdivision manuelle a été contrôlée avant correction à la révision MCP `90885880e3652673d0f34e3f3b3d7fafdc0380e19fa27f6be02961ae116dfdba`. L’inspection reconnaissait correctement les États 51, 55 et 1085 et leurs dix-huit provinces, mais signalait 17 positions encore rattachées à l’État 55 alors que leurs coordonnées se trouvaient dans les provinces de Hesse-Rhénan. Le rendu préalable avec bâtiments, ravitaillement et voies ferrées a produit le PNG `ff354e94e3bb8e5bd650e7640657af2a6215c0376d7745367a9332df432183cc`.

Une réécriture atomique `hoi4.map_rewrite` par 17 opérations `upsert_building_position` a été tentée et annulée sans écriture par `REWRITE_STRUCTURE_LIMIT`. Le repli source a modifié uniquement l’ID d’État de ces 17 lignes, de 55 vers 1085, sans modifier leurs coordonnées, leur type, leur rotation ou leur province résolue.

L’inspection finale établit la révision `7949da0e156fc45997a5274e70155aac5237f25f5e9c0077f8351603e065dacd`. Les 17 erreurs ciblées ont disparu ; les contrôles des définitions, de la géométrie, de l’appartenance aux États et régions, des adjacences, du ravitaillement et des voies ferrées réussissent. Les seuls diagnostics de positions restants sont les `floating_harbor` vanilla hors périmètre déjà documentés.

Le rendu final conserve le même PNG `ff354e94e3bb8e5bd650e7640657af2a6215c0376d7745367a9332df432183cc`, ce qui confirme l’absence de déplacement visuel. Son catalogue JSON passe de `cedf6b80ae7f421db4eab5bb5a06306e6c90a62bbbe2df33aebc27d5cbf39780` à `3955cc623fb64baa44b24ce9fa6d83b9ae24da84730d04898e15c03a90408444`, conformément à la seule réattribution des 17 identifiants d’État.

Après l’ajout de Hesse-Rhénan au partage de Yalta, l’inspection événementielle ciblée autour de `germany.119` établit la révision `2eb46e54eb5914aa7669ce27b3a1d9bf2f2bf218f6c57a00b972f295de3a1088`, sans diagnostic bloquant ciblé. Le rendu de voisinage final produit le PNG `5eaaac2534e90fb88b47776668a3a11713b7709403698c3e551ce8769144efda`.

## Limites et pistes futures

Le paquet n’ajoute ni reconstruction politique française, ni système économique régional, ni nouvelle identité nationale.

Une extension future pourrait relier les préfectures aux décisions françaises, représenter l’administration militaire ou civile et proposer un tracé alternatif du Westwall sur la nouvelle frontière allemande.

Toute extension devra conserver les IDs, les noyaux et le partage de population établis ici, sauf décision de conception explicite contraire.
