# Compte rendu semaine 7 (6 mars 2024)

## Problèmes rencontrés

- Ne pas mélanger certains fichiers dans des dossiers (par exemple ne pas mettre de photo png dans le code source du robot)

- Il faut écrire un log lorsque le robot se crash

- Dans le controleur, le delta du temps dois etre différent

## Objectifs

- Creer un robot adaptateur

- Rajouter une log pour le robot qui se crash

- Implémentation d'un delta t pour le simu

- Déplacer les fichiers aux bons endroits pour un meilleure visibilité

- Implémentation methode update position fans l'adaptateur


## Réalisations

- La classe robot adaptateur a été créer

- La méthode update position du robot adaptateur a été créer

- le delta t de la simu a été créer

- La log lorsque le robot de crash a été implémenter

- Création d'un selectionneur de robot

- Création de la classe Mockup

- Déplacement des fichiers png hors du code source du robot

- Test des controleurs dans le robot adaptateur

- Le fichier simulation a été déplacer dans model


# Conclusion

Cette semaine, nous avons identifié et résolu plusieurs problèmes importants. Tout d'abord, nous avons mis en évidence la nécessité de restructurer nos fichiers pour une meilleure organisation. En déplaçant les fichiers appropriés vers des emplacements plus adéquats, tels que le déplacement des fichiers PNG hors du code source du robot, nous avons amélioré la lisibilité et la maintenance de notre projet.

En parallèle, nous avons introduit un nouvel élément crucial : l'adaptateur de robot. Cette implémentation offre une modularité accrue à notre système, permettant une gestion plus souple et efficace des différents types de robots. De plus, nous avons élaboré et intégré la méthode de mise à jour de la position dans cet adaptateur, une avancée significative pour garantir le bon fonctionnement de notre simulation.

Dans le même ordre d'idées, nous avons également pris des mesures pour améliorer la précision de notre simulation en introduisant un delta t, permettant ainsi de mieux contrôler le temps de simulation. Cette fonctionnalité est essentielle pour garantir la cohérence et la fiabilité de nos résultats.

Enfin, nous avons abordé la question des crashes du robot en introduisant des logs pour enregistrer ces événements. Cette mesure renforce la surveillance et le débogage de notre système, offrant une visibilité accrue sur les incidents survenant lors de la simulation.

Dans l'ensemble, cette semaine a été marquée par des progrès significatifs dans la résolution de problèmes et l'atteinte d'objectifs clés, renforçant ainsi la robustesse et la fonctionnalité globale de notre projet.