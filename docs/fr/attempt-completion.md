# attempt_completion (FR)

**Source** : https://kilocode.ai/docs/features/tools/attempt-completion

## Aperçu
Résumé concis de ce que fait **attempt_completion** dans Kilo Code, quand l’utiliser, et comment il se combine avec d’autres outils.

## Paramètres
- Voir la page officielle pour la liste complète et les règles de validation.

## Fonction
- Description pratique du comportement de l’outil et de son effet sur l’espace de travail.

## Quand l’utiliser
- Situations et critères de décision pour l’invoquer.

## Points forts
- Capacités notables et propriétés de sécurité.

## Limitations
- Contraintes connues et périmètres de performance/sécurité.

## Fonctionnement (flux)
- Étapes clés : validation → exécution → résultat.

## Bonnes pratiques
- Association avec des outils complémentaires.

## Exemples
- Scénarios courts ou extraits d’invocation en XML.

## Aperçu
Signale la **fin de tâche** avec un résultat concis, et peut exécuter **une commande de démo** (avec approbation).

## Paramètres
- `result` (requis), `command` (optionnel).

## Points forts
- UI de complétion, boucle de feedback, télémétrie, gestion des sous‑tâches.

## Limitations
- Pas pour le progrès partiel; une seule commande; nécessite approbation.

## Fonctionnement
- Présente le résultat → (option) exécute la commande → récupère le feedback → poursuit/termine.
