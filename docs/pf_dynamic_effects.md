# Effets paramétrés

`rhenish_resistance_select`, défini dans `common/scripted_effects/rhenish_resistance.txt`, choisit un des cinq modificateurs de résistance rhénane en scope État.
Entrée obligatoire sans valeur par défaut : `MODIFIER`, identifiant de palier défini dans `common/dynamic_modifiers/rhenish_resistance.txt` ; l'appelant doit avoir vérifié `rhenish_resistance_eligible`.
Exemple : `rhenish_resistance_select = { MODIFIER = rhenish_resistance_light }`.
Il ne produit aucune variable de sortie et ne modifie pas la résistance native ; si le palier diffère, il retire uniquement les modificateurs de cette famille avant d'ajouter celui demandé.
Le détail des helpers sans paramètres, de leur routage et des limites figure dans [la spécification rhénane](specs/rhenish_resistance/implementation.md).
