# Compte rendu semaine 8 (20 mars 2024)

## Problèmes rencontrés

- Le main n'est pas encore assez léger.

- Certaines fonctions ne sont pas assez claires. Il est important de créer une fonction en ajoutant verbe+complément.

- Il faut ajouter une façon de choisir entre le robot simulé et le robot réel dans le main.

- Attention à l'opérateur == dans tourner, c'est risqué car cela peut ne pas fonctionner.

- Ne pas créer un fichier par stratégie.

- La mise à jour du temps passé ne sert à rien.

- Faire un calcul de distance parcourue dans le robot simulé et le robot adaptateur.

## Objectifs

- Créer une fonction pour calculer la distance parcourue.

- Supprimer la mise à jour du temps passé et implémenter la fonction "faire rond".

- Corriger la méthode "faire carré".

- Refactoriser le code.

- Mettre en place 3 threads (While pour le contrôleur, le graphique et la simulation).

- Utiliser get_attr dans le robot adaptateur.

- Créer une stratégie séquentielle qui exécute une liste de stratégies données.

- Remplacer les == dans la stratégie "tourner".

## Réalisations

- Nous avons créé une fonction pour calculer la distance parcourue.

- Nous avons supprimé la mise à jour du temps passé et avons implémenté la fonction "faire rond".

- La méthode "faire carré" a été corrigée.

- Nous avons refactorisé le code.

- Les 3 threads ont été implémentés (While pour le contrôleur, le graphique et la simulation).

- Nous avons utilisé get_attr dans le robot adaptateur.

- Nous avons créé une stratégie séquentielle qui exécute une liste de stratégies données.

- Les == dans la stratégie "tourner" ont été remplacés.

# Conclusion

Au cours de cette période, nous avons identifié plusieurs problèmes dans notre code initial et avons travaillé efficacement pour les résoudre. Nous avons constaté que le programme principal n'était pas aussi léger qu'il aurait dû l'être, certaines fonctions manquaient de clarté et il y avait des risques potentiels dans l'utilisation de l'opérateur == dans certaines parties du code.

Pour remédier à ces problèmes, nous avons entrepris plusieurs actions. Nous avons amélioré la lisibilité du code en adoptant une convention de nommage claire pour les fonctions, en refactorisant le code pour le rendre plus efficace et en remplaçant les opérateurs == par des méthodes plus sûres.

De plus, nous avons introduit de nouvelles fonctionnalités telles que le calcul de la distance parcourue par le robot simulé, la création d'une stratégie séquentielle permettant l'exécution d'une liste de stratégies données, ainsi que l'implémentation de trois threads pour le contrôleur, le graphique et la simulation.

Nous avons également supprimé les fonctionnalités inutiles telles que la mise à jour du temps passé, ce qui a permis de simplifier le code et d'améliorer sa performance.

En résumé, ces efforts ont abouti à une amélioration significative de notre code, le rendant plus léger, plus clair et plus robuste. Nous sommes confiants dans le fait que ces modifications contribueront à améliorer l'efficacité et la fiabilité de notre programme dans ses futures itérations.