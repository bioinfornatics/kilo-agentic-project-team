# ask_followup_question (FR)

**Source** : https://kilocode.ai/docs/features/tools/ask-followup-question

## Aperçu
Résumé concis de ce que fait **ask_followup_question** dans Kilo Code, quand l’utiliser, et comment il se combine avec d’autres outils.

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
Pose une **question ciblée** (avec **suggestions** optionnelles) pour combler une lacune d’information. Toujours disponible.

## Paramètres
- `question` (requis), `follow_up` (XML `<suggest>`).

## Points forts
- Choix interactifs, réponse encapsulée dans `<answer>…</answer>`, historique conservé.

## Limitations
- Une seule question par appel; pas de schéma imposé sur la réponse.

## Fonctionnement
- Transforme en JSON pour l’IU → collecte la réponse (texte/images) → reprend la tâche.
