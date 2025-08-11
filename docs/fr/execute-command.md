# execute_command (FR)

**Source** : https://kilocode.ai/docs/features/tools/execute-command

## Aperçu
Résumé concis de ce que fait **execute_command** dans Kilo Code, quand l’utiliser, et comment il se combine avec d’autres outils.

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
Exécute des **commandes CLI** dans un terminal géré avec contrôles de sécurité (parsing shell, `.kilocodeignore`, allowlists).

## Paramètres
- `command` (requis), `cwd` (optionnel).

## Points forts
- Réutilisation de terminal, sortie temps réel, gestion des signaux/exit codes, support apps interactives.

## Limitations
- Différences OS; privilèges élevés non gérés automatiquement.

## Fonctionnement
- Valide/sécurise → réutilise/crée terminal → exécute → capture la sortie/exit → retourne l’état.
