# use_mcp_tool (FR)

**Source** : https://kilocode.ai/docs/features/tools/use-mcp-tool

## Aperçu
Résumé concis de ce que fait **use_mcp_tool** dans Kilo Code, quand l’utiliser, et comment il se combine avec d’autres outils.

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
Exécute un **outil** d’un serveur MCP avec **arguments** validés. Étend Kilo avec des capacités métier.

## Paramètres
- `server_name` (requis), `tool_name` (requis), `arguments` (JSON).

## Points forts
- Transports (stdio/SSE), validations Zod, types de contenu, timeouts, auto‑restart, liste «always allow».

## Limitations
- Disponibilité du serveur/outil; réseau; une opération MCP à la fois; approbation requise sauf liste blanche.

## Fonctionnement
- Valide hub/serveur/outil/args → choisit le transport → exécute → formate (et chaîne avec `access_mcp_resource` si nécessaire).
