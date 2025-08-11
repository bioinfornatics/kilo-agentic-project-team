# browser_action (FR)

**Source** : https://kilocode.ai/docs/features/tools/browser-action

## Aperçu
Résumé concis de ce que fait **browser_action** dans Kilo Code, quand l’utiliser, et comment il se combine avec d’autres outils.

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
Automatise Chromium via Puppeteer. Actions : `launch`, `click`, `type`, `scroll_{down|up}`, `close`, avec **captures écran**.

## Paramètres
- `action` (requis), `url`, `coordinate`, `text` (selon l’action).

## Points forts
- Session **locale** ou **remote**, logs console, attente de stabilité DOM, historique.

## Limitations
- Verrou pendant la session; clicks en coordonnées **viewport**; seulement Chrome/Chromium; fermer avant d’utiliser d’autres outils.

## Fonctionnement
- Valide & gère la session → interactions → captures → fermeture.
