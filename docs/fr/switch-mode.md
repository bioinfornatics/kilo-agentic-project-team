# switch_mode (FR)

**Source** : https://kilocode.ai/docs/features/tools/switch-mode

## Aperçu
Résumé concis de ce que fait **switch_mode** dans Kilo Code, quand l’utiliser, et comment il se combine avec d’autres outils.

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
Demande un **changement de mode** pour adapter outils et prompts à la phase suivante. Conserve le contexte; **approbation requise**.

## Paramètres
- `mode_slug` (requis), `reason` (optionnel).

## Points forts
- Respecte les restrictions; délai de stabilisation; modes core & custom.

## Limitations
- Impossible vers un mode inexistant; restrictions de type de fichiers possibles.

## Fonctionnement
- Valide & présente → active le nouveau mode après approbation → continue.
