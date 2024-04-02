# Compte rendu semaine 8 (20 mars 2024)

## Problèmes rencontrés

- Impossible d'utiliser toutes les stratégies sans modifier le main.
- Le robot réel gère l'environnement et le robot simulé (sans intérêt) problème d'optimisation.
- On se comporte avec le robot réel comme s'il s'agissait d'un robot simulé.
- Certaines lignes sont inutiles.
- Pow() n'est pas optimal, il vaut mieux utiliser **.
- Il faut ajouter une façon de choisir entre le robot simulé et le robot réel dans le main
## Objectifs

- renommer la classe object en class obstacle

- implementation des threads dans le main(environnement controleur, interface).

- Creation d'une classe chapeau simulation pour les threads.

- Definir des fps différents selon le thread.

- Enlever les imports * et corriger le code.

- faire des sous dossier(environnement, robot)(interface).

- faire des recherche sur le choix de la 3D.

## Réalisations

- Nous avons implémenté les threads dans le main.
- Nous avons remplacé pow par **2 ou X*X.
- Nous avons corrigé les imports *.
- Nous avons créé des sous-dossiers (environnement, robot, interface).
- Nous avons choisi l'interface 3D.
- Nous avons refactorisé le code.
- Les 3 threads ont été mis en place (boucles While pour le contrôleur, le graphique et la simulation).


# Conclusion
Au cours de cette période, nous avons identifié et résolu plusieurs problèmes dans notre code initial, notamment des difficultés à utiliser toutes les stratégies sans modifier le main, des problèmes d'optimisation liés à la gestion de l'environnement par le robot réel, et des lignes de code inutiles. Pour remédier à ces problèmes, nous avons entrepris diverses actions telles que le nettoyage du code, le remplacement des opérateurs pow() par **, et la mise en place de threads pour gérer l'environnement, le contrôleur et l'interface. Malgré ces progrès, il reste des défis à relever, notamment la nécessité de choisir entre le robot simulé et le robot réel dans le main, ainsi que la définition de fps différents selon le thread. En résumé, bien que nous ayons fait des progrès significatifs, il reste encore du travail à faire pour améliorer la qualité et la performance de notre code.