# write_to_file (FR)

**Source** : https://kilocode.ai/docs/features/tools/write-to-file

## Aperçu
Résumé concis de ce que fait **write_to_file** dans Kilo Code, quand l’utiliser, et comment il se combine avec d’autres outils.

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
Crée ou **réécrit complètement** un fichier avec **approbation interactive** via diff. À privilégier pour **nouveaux fichiers**; préférer `apply_diff` pour les petites modifs.

## Paramètres
- `path` (requis), `content` (requis), `line_count` (requis).

## Points forts
- Vue diff éditable, détection de troncature, contrôles de chemin/permissions, nettoyage des artefacts de modèle.

## Limitations
- Lent sur gros fichiers; écrasement total; interactif uniquement; `line_count` exact requis.

## Fonctionnement
- Valide + pré‑traite → ouvre diff → attend approbation → écrit.
