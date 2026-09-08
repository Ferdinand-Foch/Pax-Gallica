# Effets scriptés rhénans

`rhenish_resistance_update`, défini dans `common/scripted_effects/rhenish_resistance.txt`, s'appelle depuis le scope pays FRA et visite les quatre États autorisés.
`rhenish_resistance_update_state` travaille en scope État : il vérifie l'éligibilité et choisit un palier par des branches explicites contenant des identifiants de modificateurs littéraux.
Exemple : `FRA = { rhenish_resistance_update = yes }` dans l'effet de `on_startup` ; aucun argument, valeur par défaut ni variable de sortie.
Les appels d'effets scriptés ordinaires utilisent `= yes`, sans substitution de paramètres ; le nettoyage partagé `rhenish_resistance_clear = yes` retire uniquement les cinq modificateurs rhénans.
Le détail des helpers sans paramètres, de leur routage et des limites figure dans [la spécification rhénane](specs/rhenish_resistance/implementation.md).
