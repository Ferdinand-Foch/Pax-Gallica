# Zone d’influence italienne de Sèvres

## Périmètre au 1er janvier 1936

La mécanique accorde à ITA les droits sur toutes les ressources stratégiques des États 342 Antalya, 343 Afyon, 345 Mersin et 346 Konya.

Les quatre États appartiennent à TUR. Chaque attribution est exécutée depuis le scope de ce propriétaire initial.

## Initialisation

Le fichier `common/on_actions/sevres_influence_zones.txt` utilise l’unique hook `on_startup` partagé avec la zone française. Ce mécanisme suit le précédent vanilla des concessions pétrolières mexicaines dans `common/on_actions/04_mtg_on_actions.txt`.

L’effet est limité au premier jour du scénario de 1936. `on_startup` ne s’exécute pas lors du chargement d’une sauvegarde, ce qui empêche une nouvelle attribution au rechargement.

Chaque État reçoit exactement un effet `give_resource_rights` dont le bénéficiaire est ITA. Aucun bloc `resources` n’est fourni. Les droits couvrent toutes les ressources présentes lors de l’initialisation ainsi que les ressources ajoutées ultérieurement dans ces États.

## Ressources au démarrage

- État 342 : 35 unités de chrome.
- État 343 : 25 unités de chrome et 1 unité de charbon.
- États 345 et 346 : aucune ressource stratégique initiale. Les droits généraux restent attachés à ces États pour leurs ressources futures.

## Éléments préservés

La mécanique ne modifie aucune usine civile, usine militaire, usine navale, infrastructure, ressource, province, frontière, propriété, contrôle ou core. Elle ne change aucune attribution française des États 344, 348, 349, 350 et 353.

## Icônes

Aucune icône ni définition de sprite n’est nécessaire.

## Extensions futures

Toute évolution politique ou industrielle de la zone d’influence est exclue de cette version. Une extension éventuelle devra préserver l’attribution unique des droits et rester distincte des bâtiments et de la propriété des États.

## Validation statique

Le contrôle des fichiers d'États effectivement hérités de vanilla confirme TUR comme propriétaire initial de 342, 343, 345 et 346, ainsi que les ressources indiquées ci-dessus.
La documentation installée 1.19.2 de give_resource_rights confirme le scope COUNTRY, le bénéficiaire et le ciblage de toutes les ressources lorsque resources est omis.
La comparaison au commit précédent confirme que les cinq attributions françaises sont identiques ; seuls les quatre droits italiens et les commentaires associés sont ajoutés.
Chaque État italien apparaît une fois, sous TUR, dans le on_startup limité au démarrage 1936.
Le démarrage 1939 ne satisfait pas sa condition de date.

L'inspection MCP ciblée du fichier retourne une entrée on_startup (`entry_bd5380038b06c0ae7a8a2b19`).
Le fichier n'appelle ni ne définit aucun événement et le diff ne touche aucune chaîne événementielle ; event_compare n'est donc pas requis pour ce changement, conformément à la clarification de l'utilisateur.
L'analyse MCP globale est partielle et n'est pas présentée comme une validation exhaustive.
Aucun effet de transfert territorial, de bâtiment ou de modification des quantités de ressources n'est ajouté.
Aucune modification de gameplay supplémentaire, aucune simplification ; aucun lancement du jeu ni validation en jeu.
Compétence utilisée pour le hook et sa validation : hoi4-events.
