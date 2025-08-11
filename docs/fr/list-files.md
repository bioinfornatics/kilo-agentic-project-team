# list_files (FR)

**Source** : https://kilocode.ai/docs/features/tools/list-files

## Aperçu
Résumé concis de ce que fait **list_files** dans Kilo Code, quand l’utiliser, et comment il se combine avec d’autres outils.

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
Liste fichiers/répertoires à un chemin; option **récursif**. Respecte `.gitignore`/`.kilocodeignore`, limite le volume.

## Paramètres
- `path` (requis), `recursive` (optionnel).

## Points forts
- Ignore `node_modules`, `.git` en récursif; ~200 entrées; timeout 10s.

## Limitations
- Pas pour confirmer un fichier fraîchement créé; pas de listing root/home.

## Fonctionnement
- Valide → résout le chemin → parcours (filtres/timeouts) → format (dossiers d’abord).
