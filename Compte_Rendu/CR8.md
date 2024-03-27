# Compte rendu semaine 8 (20 mars 2024)

## Problèmes rencontrés

- Le main n'est pas encore assez léger

- Certaines fonction ne sont pas assez clair, il est important de créer une fonction en ajoutant verbe+complément

- Il faut ajouter une façon de choisir entre le robot simulé et le robot réel dans le main

- Attention a == dans tourner, c'est risqué car ca peut ne pas marcher

- Ne pas faire 1 fichier par stratégie

- Update temps passé ne sert a rien

- Faire un calcul de distance parcourue dans robot simulé et robot adaptateur

## Objectifs

- Faire une fonction distance parcourue

- Supprimer update temps passé et faire rond

- Corriger la méthode faire carré

- Refactorisation du code

- Faire 3 thread (While pour le controleur, le graphique et la simulation)

- Utilisation de get_attr dans robot adaptateur

- Faire une strategie séquentiel qui execute une liste de stratégie donné

- Remplacer les == dans la stratégie tourner

## Réalisations

- Nous avons fait une fonction distance parcourue

- Nous avons supprimer update temps passé et faire rond

- La méthode faire carré à été corrigé

- Nous avons refactoriser le code

-Les 3 thread ont été implémenter (While pour le controleur, le graphique et la simulation)

- Nous avons utiliserget_attr dans robot adaptateur

- Nous avons fait une strategie séquentiel qui execute une liste de stratégie donné

- Les == dans la stratégie tourner ont été remplacé


# Conclusion

Au cours de cette période, nous avons identifié plusieurs problèmes dans notre code initial et avons travaillé efficacement pour les résoudre. Nous avons constaté que le programme principal n'était pas aussi léger qu'il aurait dû l'être, certaines fonctions manquaient de clarté et il y avait des risques potentiels dans l'utilisation de l'opérateur == dans certaines parties du code.

Pour remédier à ces problèmes, nous avons entrepris plusieurs actions. Nous avons amélioré la lisibilité du code en adoptant une convention de nommage claire pour les fonctions, en refactorisant le code pour le rendre plus efficace et en remplaçant les opérateurs == par des méthodes plus sûres.

De plus, nous avons introduit de nouvelles fonctionnalités telles que le calcul de la distance parcourue par le robot simulé, la création d'une stratégie séquentielle permettant l'exécution d'une liste de stratégies données, ainsi que l'implémentation de trois threads pour le contrôleur, le graphique et la simulation.

Nous avons également supprimé les fonctionnalités inutiles telles que la mise à jour du temps passé, ce qui a permis de simplifier le code et d'améliorer sa performance.

En résumé, ces efforts ont abouti à une amélioration significative de notre code, le rendant plus léger, plus clair et plus robuste. Nous sommes confiants dans le fait que ces modifications contribueront à améliorer l'efficacité et la fiabilité de notre programme dans ses futures itérations.