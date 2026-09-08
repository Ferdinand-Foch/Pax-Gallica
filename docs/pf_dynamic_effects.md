# Effets scriptés rhénans

`rhenish_resistance_update`, défini dans `common/scripted_effects/rhenish_resistance.txt`, s'appelle depuis le scope pays FRA et visite les quatre États autorisés pour actualiser leurs effets locaux, agréger le maximum éligible et sélectionner l'esprit national français.
`rhenish_resistance_update_state` travaille en scope État : il vérifie l'éligibilité et choisit un palier par des branches explicites contenant des identifiants de modificateurs littéraux.
Exemple : `FRA = { rhenish_resistance_update = yes }` dans l'effet de `on_startup` ; aucun argument ni sortie persistante.
Les appels d'effets scriptés ordinaires utilisent `= yes`, sans substitution de paramètres ; le nettoyage partagé `rhenish_resistance_clear = yes` retire uniquement les cinq modificateurs rhénans.
Le détail des helpers sans paramètres, de leur routage et des limites figure dans [la spécification rhénane](specs/rhenish_resistance/implementation.md).

`rhenish_resistance_update_and_accumulate = yes` travaille en scope État, actualise le modificateur local puis augmente la temporaire non scopée `rhenish_max_resistance` uniquement si cet État est éligible et dépasse le maximum courant.
Son appelant doit initialiser cette temporaire à `constant:rhenish_resistance.no_eligible_resistance` avant la première visite ; aucune valeur implicite n'est utilisée.
La sortie temporaire est le maximum natif 0–100, ou −1 si aucun État visité n'est éligible ; aucune écriture de résistance native ni de compliance n'a lieu.

`rhenish_resistance_update_national = yes` travaille exclusivement en scope FRA et consomme ce maximum après l'agrégation complète.
Il retire le palier en l'absence d'État éligible et remplace l'esprit uniquement lorsque le palier attendu est absent.
`rhenish_resistance_clear_national = yes`, également en scope FRA, retire seulement les cinq esprits de cette famille et peut être appelé sans initialiser la temporaire.
Les callbacks des esprits attribuent et retirent leurs quatre jetons de renseignement GER → FRA ; aucun autre esprit ni jeton n'est retiré.
Ces helpers n'acceptent aucun paramètre et n'ont aucune sortie persistante ; leur contrat complet figure dans [la spécification nationale](specs/rhenish_resistance/national_spirits.md).
