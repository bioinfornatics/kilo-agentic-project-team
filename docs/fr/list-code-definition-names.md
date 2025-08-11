# list_code_definition_names (FR)

**Source** : https://kilocode.ai/docs/features/tools/list-code-definition-names

## Aperçu
Résumé concis de ce que fait **list_code_definition_names** dans Kilo Code, quand l’utiliser, et comment il se combine avec d’autres outils.

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
Produit une **carte structurelle** des définitions de haut niveau (classes, fonctions, interfaces) d’un répertoire via Tree‑sitter.

## Paramètres
- `path` (requis).

## Points forts
- **Numéros de lignes + extraits**, multi‑langages, limite ~50 fichiers, non récursif.

## Limitations
- Définitions imbriquées non listées; pas de relations d’usage.

## Fonctionnement
- Valide → scanne les fichiers top‑level → parse → tri & rendu.
