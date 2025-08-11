# read_file (FR)

**Source** : https://kilocode.ai/docs/features/tools/read-file

## Aperçu
Résumé concis de ce que fait **read_file** dans Kilo Code, quand l’utiliser, et comment il se combine avec d’autres outils.

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
Lit un fichier (ou une plage de lignes) avec **numéros**; extrait le texte de **PDF/DOCX/IPYNB**; **auto‑troncature** pour gros fichiers.

## Paramètres
- `path` (requis), `start_line`/`end_line`, `auto_truncate`.

## Points forts
- Priorité aux plages; résumés avec plages de méthodes quand tronqué.

## Limitations
- Gros fichiers sans plage peuvent être lents.

## Fonctionnement
- Valide → résout → stratégie (plage > auto‑tronc > complet) → numérotation.
