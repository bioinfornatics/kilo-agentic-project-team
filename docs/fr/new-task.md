# new_task (FR)

**Source** : https://kilocode.ai/docs/features/tools/new-task

## Aperçu
Résumé concis de ce que fait **new_task** dans Kilo Code, quand l’utiliser, et comment il se combine avec d’autres outils.

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
Crée une **sous‑tâche** avec son **mode** et son historique; met en pause le parent et restitue les résultats à la fin.

## Paramètres
- `mode` (requis), `message` (requis).

## Points forts
- Pile hiérarchique, approbation utilisateur, transitions claires.

## Limitations
- Mode doit exister; profondeur excessive = complexité.

## Fonctionnement
- Valide & vérifie le mode → crée le contexte enfant → bascule → restitue au parent à la fin.
