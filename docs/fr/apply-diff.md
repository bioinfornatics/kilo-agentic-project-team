# apply_diff (FR)

**Source** : https://kilocode.ai/docs/features/tools/apply-diff

## Aperçu
Résumé concis de ce que fait **apply_diff** dans Kilo Code, quand l’utiliser, et comment il se combine avec d’autres outils.

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
Fait des **modifications chirurgicales** dans des fichiers existants via un **bloc diff** avec **numéros de lignes** (MultiSearchReplaceDiffStrategy). Préférer pour **petites modifications**.

## Paramètres
- `path` (requis), `diff` (requis avec marqueurs `:start_line:`).

## Points forts
- Fuzzy‑matching (≈0.8–1.0), contexte `BUFFER_LINES` (~40), fenêtres chevauchantes, respect de l’indentation, preview diff, vérif `.kilocodeignore`.

## Limitations
- Cible ambiguë : peut nécessiter une revue manuelle.

## Fonctionnement
- Valide → vérifie `.kilocodeignore` → lit → localise les matches → prépare le patch → **revue utilisateur** → applique.
