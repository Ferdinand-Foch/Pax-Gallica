# Découpage territorial de la rive gauche du Rhin

## Objet

Ce paquet établit le découpage territorial rhénan du scénario de 1936 sans modifier les provinces, les rivières, les adjacences, les chemins de fer ni les nœuds logistiques de la carte vanilla.

La France possède et contrôle la Sarre, le Roer, Rhin-et-Moselle et Mont-Tonnerre au début de la partie, sans noyau ni revendication française.

Les noyaux allemands, rhénans et prussiens sont conservés dans les quatre départements, tandis que le noyau hessois demeure exclusivement dans le reliquat de Nassau.

## États

| ID | Nom | Provinces | Préfecture | Propriétaire initial | Population | Infrastructure | Usines civiles | Usines militaires |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| 42 | Sarre | 11435, 11470, 9575, 11531 | Sarrebruck (11531) | FRA | 1 386 454 | 4 | 1 | 0 |
| 51 | Ruhr | 529, 6469, 6570, 9482 | Essen (6469) | GER | 2 629 193 | 4 | 3 | 2 |
| 55 | Nassau | 564, 589, 3397, 3524, 3574, 6444, 6488, 6549, 9486, 9524, 9547, 11445, 11533 | Francfort (6488) | GER | 3 550 216 | 4 | 2 | 1 |
| 1082 | Roer | 3512, 3444, 587, 9522 | Aix-la-Chapelle (9522) | FRA | 2 778 579 | 4 | 1 | 1 |
| 1083 | Rhin-et-Moselle | 3547, 11494, 3423 | Coblence (3423) | FRA | 1 397 804 | 3 | 1 | 0 |
| 1084 | Mont-Tonnerre | 11547, 563, 3558, 11560 | Mayence (11560) | FRA | 1 228 471 | 4 | 1 | 0 |

Les champs `owner` et `controller` établissent explicitement la propriété et le contrôle initiaux à la date de départ.

Les préfectures sont des désignations administratives et narratives : conformément au cahier des charges, Aix-la-Chapelle et Trèves ne reçoivent pas de VP artificiellement supérieur à Cologne ou Sarrebruck, de sorte que le marqueur de capitale mécanique de Roer demeure Cologne.

Les ressources de l’ancien État 42 restent dans la Sarre, celles de l’ancien État 51 restent dans le reliquat de la Ruhr et celles de l’ancien État 55 restent dans le reliquat de Nassau.

Les ajouts vanilla non fortifiés du signet de 1939 restent également dans leurs reliquats d’origine : la Sarre conserve le radar et les raffineries synthétiques de l’État 42, tandis que la Ruhr conserve l’extension de la base aérienne et le radar de l’État 51. Les forts provinciaux datés du Westwall et l’historique de démilitarisation sont volontairement écartés, puisque la rive gauche annexée constitue une frontière française militarisable.

Le barrage d’Edersee reste dans la province 11533 du Nassau.

## Population

La population de chacun des trois États vanilla a été distribuée entre ses successeurs au prorata du nombre de pixels terrestres de chaque province mesuré par `hoi4.map_inspect`.

La méthode du plus fort reste a été appliquée aux valeurs entières afin de préserver exactement chaque total source sans duplication ni perte.

| Source vanilla | Parts en pixels | Répartition de population |
| --- | --- | --- |
| État 42, 701 pixels | Sarre 321 ; Rhin-et-Moselle 153 ; Mont-Tonnerre 227 | 1 386 454 ; 660 833 ; 980 452 |
| État 51, 617 pixels | Roer 279 ; Rhin-et-Moselle 74 ; Ruhr 264 | 2 778 579 ; 736 971 ; 2 629 193 |
| État 55, 1 072 pixels | Mont-Tonnerre 70 ; Nassau 1 002 | 248 019 ; 3 550 216 |

Les populations sources de 3 027 739, 6 144 743 et 3 798 235 habitants totalisent 12 970 717 habitants, soit exactement le total des six États après découpage.

## Réseau, bâtiments et région stratégique

Les 52 entrées de `map/buildings.txt` dont les coordonnées se trouvent dans une province transférée ont reçu le nouvel ID d’État correspondant.

Les chemins de fer et les nœuds logistiques de Cologne (587) et Sarrebruck (11531) restent définis par les fichiers vanilla et n’ont pas été réécrits.

La région stratégique 7 conserve strictement sa composition et reçoit seulement le nom localisé « Région rhénane ».

## Compatibilité des mécanismes vanilla

La remilitarisation allemande et ses événements ne manipulent plus les territoires français de la rive gauche et restent attachés au seul État démilitarisé de Bade (978).

La construction du Westwall ne place plus de fortifications dans les provinces françaises et reste attachée à Bade, faute de tracé allemand de remplacement autorisé.

Les investissements sidérurgiques allemands restent attachés au reliquat industriel de la Ruhr (51).

Le barrage de la Rur est associé à Rhin-et-Moselle (1083) et le focus allemand correspondant est contourné lorsque l’Allemagne ne contrôle pas cet État.

Les stratégies de front françaises et allemandes visent les reliquats de la Ruhr et du Nassau au lieu de considérer la Sarre française comme un territoire allemand.

Les frontières naturelles françaises revendiquent les quatre départements sans créer automatiquement un objectif de guerre contre l’Allemagne qui les a déjà cédés.

La désunion de l’Allemagne exclut les quatre départements français du transfert générique vers la Prusse, mais laisse la Ruhr allemande suivre le traitement normal.

Les décisions de formation qui énumèrent explicitement les territoires allemands exigent et intègrent aussi les États 1082, 1083 et 1084.

Les chaînes alternatives de remilitarisation et d’Anschluss utilisent Bade (978), tandis que les objectifs de guerre allemands alternatifs conservent le reliquat allemand de la Ruhr (51).

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

Les arbres nationaux allemand et français ont également été inspectés et rendus après adaptation à la révision MCP `1263eaa4ed2e5bcb4976e74fd9706bc56ff54d927051c83c6aea100b077bae5f`. Leurs nombres de nœuds et leurs hashes de disposition restent identiques aux preuves préalables : `abe189340cf67a71e15d6e08eb7de37e97437430f03d7a77c4c29789f50df3b1` pour l’Allemagne et `04bd763dbc684d1f376d0b038bc2b458e87918fca6f2da94d1bf33ba3d52c553` pour la France. Les adaptations territoriales n’ont donc déplacé ni supprimé aucun focus.

La chaîne événementielle allemande affectée a été inspectée puis rendue après adaptation. Le rendu final ciblé autour de `germany.60` est établi à la révision `886126ea4c9e5e03e47e0481f483e5471d68b00a83842683e2da0695065db03d`, avec le PNG `35afe90fdcdbc7501927361b1cafd30f45b9e764bf7cdce21a84fe99d2487755`. Les diagnostics globaux restant signalés par l’outil appartiennent au corpus vanilla complet ; aucun diagnostic bloquant n’est associé à la chaîne ciblée.

## Limites et pistes futures

Le paquet n’ajoute ni reconstruction politique française, ni système économique régional, ni nouvelle identité nationale.

Une extension future pourrait relier les préfectures aux décisions françaises, représenter l’administration militaire ou civile et proposer un tracé alternatif du Westwall sur la nouvelle frontière allemande.

Toute extension devra conserver les IDs, les noyaux et le partage de population établis ici, sauf décision de conception explicite contraire.
