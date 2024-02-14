# Compte rendu semaine 4 (7 février 2024)

## Problèmes rencontrés

- Le code contient encore trop de parties "spaghetti"

- Certains unittest sont inutles (isinstance)

- Certaines fonctions sont inutiles (avancer/reculer/freinage progressif)

- La simulation n'est pas 100% indépendante de pygame, il faut enlever tout ce qui concerne pygame dans simulation et le mettre dans interface

## Objectifs

- Réaliser une documentation pour l'ensemble du code.

- Création d'un système de collision et d'obstacle.

- Simulation des roues.

- Ajout d'une conclusion sur le choix de l'interface graphique.

- Réalisation d'un fichier nommé test où les tests unitaires sont effectués.

## Réalisations

- Continuer et améliorer les tests unitaires

- Supprimer les parties inutiles du code, notamment les fonctions avancer, reculer, la classe roue...

- Nettoyer la partie simulation et interface

- Améliorer la physique des roues

- Travail d'organisation sur le code spaghetti

- Améliorer la DocString

- Démontrer mathématiquement si ce que nous avons utilisé en physique des roues ne correspond pas à une méthode ou un théorème existant.

## Conclusion

# Conclusion

Au cours de cette semaine, notre principal objectif a été de continuer à améliorer la qualité globale de notre projet. Nous avons pris des mesures significatives pour résoudre certains problèmes identifiés dans le code, tels que la simplification des parties inutiles et la suppression des fonctions qui ne contribuaient pas à l'objectif global du projet.

Nous avons également poursuivi nos efforts pour rendre le code plus lisible en travaillant sur l'organisation du code spaghetti. Les tests unitaires ont été étendus et améliorés pour garantir une meilleure couverture du code.

En parallèle, nous avons entrepris une démarche visant à rendre la simulation des roues plus réaliste en travaillant sur l'amélioration de la physique des roues.

Malgré ces progrès, nous avons identifié des aspects restants à améliorer, notamment l'indépendance totale de la simulation vis-à-vis de Pygame et la démonstration mathématique des choix effectués en physique des roues.

Dans l'ensemble, la semaine a été productive, mais nous sommes conscients qu'il reste du travail à accomplir pour atteindre nos objectifs fixés. Nous restons déterminés à fournir un code robuste, bien documenté et efficace pour la simulation de notre robot.
