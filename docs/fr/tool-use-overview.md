# Tool Use Overview (FR)

**Source** : https://kilocode.ai/docs/features/tools/tool-use-overview

## Aperçu
Résumé concis de ce que fait **Tool Use Overview** dans Kilo Code, quand l’utiliser, et comment il se combine avec d’autres outils.

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
Kilo Code expose un **système d’outils** regroupé par finalité : **read**, **edit**, **browser**, **command**, **MCP**, **workflow**. Certains outils sont **toujours disponibles** : `ask_followup_question`, `attempt_completion`, `switch_mode`, `new_task`, `update_todo_list`.

## Points forts
- **Garde‑fous par mode** : vérification `isToolAllowedForMode(...)` avant l’appel.
- **Processus de décision** : validation du mode → exigences (capacités, permissions) → validation des paramètres.
- **Couches de sécurité** : restrictions FS, allowlists de commandes, contrôle réseau.
- **Patrons** : Info—`ask_followup_question → read_file → search_files` ; Code—`read_file → apply_diff → attempt_completion` ; Tâche—`new_task → switch_mode → execute_command` ; Suivi—`update_todo_list → execute_command → update_todo_list`.

## Fonctionnement
- Invocation selon le besoin, la disponibilité du mode ou le contexte, avec gestion d’erreurs et de reprise (retries, fallbacks).
