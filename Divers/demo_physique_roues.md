# Calcul de la vitesse linéaire du robot :

- Formule :
  vitesse_lineaire = (vitesse_gauche+vitesse_droite)/2

- Explication :
  La vitesse linéaire est la moyenne des vitesses des roues gauche et droite. Cela assure un déplacement linéaire cohérent du robot, car la vitesse est uniformément répartie entre les deux roues.

# Calcul de la rotation du robot :

- Formule :
  rotation = (vitesse_droite - vitesse_gauche)\*(rayon_roue/largeur)

- Explication :
  La rotation est déterminée par la différence des vitesses des roues, ajustée en fonction de la largeur du robot. Une différence de vitesse entraîne une rotation.

# Mise à jour de la direction du robot :

- Formule :
  nouvelle*direction_x = direction_X * cos(rotation) - direction*y * sin(rotation)

nouvelle*direction_Y = direction_X * sin(rotation) + direction*y * cos(rotation)

- Explication :

La modification de la direction du robot est réalisée en appliquant des formules de rotation en 2D. Ces formules, basées sur les fonctions trigonométriques, permettent d'ajuster la direction du robot conformément à son orientation après le déplacement. Plus précisément, nouvelle_direction_x est calculée en prenant la composante x de la direction (direction_x) et en appliquant une rotation trigonométrique,tandis que nouvelle_direction_y est déterminée en utilisant la composante y de la direction (direction_y).Ces calculs garantissent que la direction du robot évolue de manière cohérente avec la rotation définie par les vitesses des roues gauche et droite, assurant ainsi un déplacement précis.

# Normalisation de la nouvelle direction :

- Formule :
  norme = sqrt(nouvelle_direction_X^2 + nouvelle_direction_y^2)
  nouvelle_direction_x/= norme
  nouvelle_direction_y/= norme

- Explication :
  La normalisation garantit que la nouvelle direction reste une unité vectorielle, facilitant le suivi et la compréhension. La norme représente la longueur du vecteur direction. En divisant chaque composante par la norme, on s'assure que le vecteur résultant a une longueur de 1.

# Nouvelles coordonnées en fonction de la direction et de la vitesse :

- Formule :
  nouveau*x = x + vitesse_lineaire * nouvelle*direction_x
  nouveau_Y = Y + vitesse_lineaire * nouvelle_direction_y

- Explication :
  Les nouvelles coordonnées sont calculées en ajoutant à la position actuelle le produit de la vitesse linéaire et de la nouvelle direction. Cela représente le déplacement dans l'environnement en fonction de la direction choisie et de la vitesse.

# Mise à jour des coordonnées et de la direction :

- Explication :
  Après avoir calculé la nouvelle direction et les nouvelles coordonnées, elles sont mises à jour pour refléter le déplacement effectif du robot. Les nouvelles coordonnées deviennent les coordonnées actuelles, et la nouvelle direction devient la direction actuelle.

# Exemple :

- Dans le contexte de notre fonction, la rotation est déterminée par la différence entre les vitesses des roues gauche et droite, dans le tableau on suppose une itération où la vitesse de la roue gauche est constante et la vitesse de la roue droite varie progressivement.

| Itération | Vitesse Gauche (m/s) | Vitesse Droite (m/s) | Rotation | Nouvelle Direction X | Nouvelle Direction Y | Nouveau X | Nouveau Y |
| --------- | -------------------- | -------------------- | -------- | -------------------- | -------------------- | --------- | --------- |
| 1         | 3.5                  | 3.5                  | 0        | 1                    | 0                    | 3.5       | 0         |
| 2         | 3.5                  | 4.0                  | 0.125    | 0.9914               | 0.1305               | 7.5       | 0         |
| 3         | 3.5                  | 4.5                  | 0.25     | 0.9659               | 0.2588               | 11.5      | 0         |
| 4         | 3.5                  | 5.0                  | 0.375    | 0.9239               | 0.3827               | 15.5      | 0         |
| 5         | 3.5                  | 5.5                  | 0.5      | 0.866                | 0.5                  | 19.5      | 0         |

# Conclusion :

La fonction update_position est conçue pour déplacer le robot en fonction des vitesses spécifiées pour ses roues gauche et droite. À travers une séquence de calculs mathématiques, elle assure une mise à jour cohérente de la position du robot. La vitesse linéaire moyenne, la rotation, la nouvelle direction, la normalisation de la direction et les nouvelles coordonnées sont autant d'étapes cruciales qui garantissent un déplacement précis du robot dans l'espace en fonction des commandes des roues. La normalisation assure que le vecteur direction reste unitaire, facilitant ainsi la compréhension et le suivi. Les exemples illustrent comment ces calculs s'appliquent, et dans l'ensemble, la fonction remplit efficacement sa mission en offrant une approche mathématiquement solide pour le contrôle du déplacement du robot.
