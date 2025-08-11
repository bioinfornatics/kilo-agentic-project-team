# search_files (FR)

**Source** : https://kilocode.ai/docs/features/tools/search-files

## Aperçu
Résumé concis de ce que fait **search_files** dans Kilo Code, quand l’utiliser, et comment il se combine avec d’autres outils.

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
Recherche **regex** (Ripgrep) avec 1 ligne de contexte avant/après; filtre possible par **glob**.

## Paramètres
- `path` (requis), `regex` (requis), `file_pattern` (optionnel).

## Points forts
- Cap ~300 résultats; lignes très longues tronquées; fusion des hits proches.

## Limitations
- Fichiers texte uniquement; regex Rust; contexte par défaut figé.

## Fonctionnement
- Valide → résout → exécute rg → format groupes.
