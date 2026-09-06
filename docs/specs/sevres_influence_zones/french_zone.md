# Zone d’influence française de Sèvres

## Périmètre au 1er janvier 1936

La mécanique accorde à FRA les droits sur toutes les ressources stratégiques des États 344 Adana, 348 Kayseri, 349 Sivas, 350 Diyarbekir et 353 Erzurum.

Les États 344, 348 et 349 appartiennent à TUR. Les États 350 et 353 appartiennent à KUR. Chaque attribution est exécutée depuis le scope de ce propriétaire initial.

## Initialisation

Le fichier `common/on_actions/sevres_influence_zones.txt` utilise `on_startup`, conformément au précédent vanilla des concessions pétrolières mexicaines dans `common/on_actions/04_mtg_on_actions.txt`.

L’effet est limité au premier jour du scénario de 1936. `on_startup` ne s’exécute pas lors du chargement d’une sauvegarde, ce qui empêche une nouvelle attribution au rechargement.

Chaque État reçoit exactement un effet `give_resource_rights` dont le bénéficiaire est FRA. Aucun bloc `resources` n’est fourni. Les droits couvrent donc toutes les ressources présentes lors de l’initialisation ainsi que les ressources ajoutées ultérieurement dans ces États.

## Ressources au démarrage

- État 344 : 2 unités de charbon.
- État 348 : 32 unités de chrome.
- États 349, 350 et 353 : aucune ressource stratégique initiale. Les droits généraux restent attachés à ces États pour leurs ressources futures.

## Éléments préservés

La mécanique ne modifie aucune usine civile, usine militaire, usine navale, infrastructure, ressource, province, frontière, propriété, contrôle ou core. Elle n’ajoute aucun bâtiment hors carte, modificateur industriel, statut de sujet, événement visible, décision, focus ou interface.

## Icônes

Aucune icône ni définition de sprite n’est nécessaire.

## Extensions futures

Toute évolution politique ou industrielle de la zone d’influence est exclue de cette version. Une extension éventuelle devra préserver l’attribution unique des droits et rester distincte des bâtiments et de la propriété des États.
