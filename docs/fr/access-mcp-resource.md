# access_mcp_resource (FR)

**Source** : https://kilocode.ai/docs/features/tools/access-mcp-resource

## Aperçu
Résumé concis de ce que fait **access_mcp_resource** dans Kilo Code, quand l’utiliser, et comment il se combine avec d’autres outils.

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
Récupère des **ressources** (texte/images/structurées) via un serveur MCP par **URI**. C’est **lecture seule** (à l’inverse de `use_mcp_tool`).

## Paramètres
- `server_name` (requis), `uri` (requis ; supporte **standard** et **templates** de ressources).

## Points forts
- Approbation utilisateur, délais, états de connexion, rendu correct des contenus.

## Limitations
- Dépend des serveurs connectés; pas de cache; formats d’URI spécifiques à chaque serveur.

## Fonctionnement
- Valide hub/serveur/activation → requête `resources/read` via MCP SDK → renvoie le contenu structuré.
