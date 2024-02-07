import math


class Robot:
    """Classe Robot répertoriant les fonctionnalités permettant de simuler un robot

    Attributs:
        :x (float): La coordonnée x actuelle du robot.
        :y (float): La coordonnée y actuelle du robot.
        :largeur (float): La largeur du robot.
        :hauteur (float): La hauteur du robot.
        :direction_x (float): La composante x du vecteur de direction du robot.
        :direction_y (float): La composante y du vecteur de direction du robot.
        :environnement (Environnement): L'environnement dans lequel le robot évolue.
        :rRoue (Roue): Le rayon des ses roues.
    
    Methodes:
        __init__(self, x, y, largeur, hauteur, direction_x, direction_y):
            Initialise un objet Robot avec les coordonnées, la taille et la direction spécifiées.

        __str__(self):
            Renvoie une représentation sous forme de chaîne de la position actuelle du robot.

        avancer(self, pas):
            Déplace le robot dans sa direction actuelle d'une distance spécifiée.

        reculer(self, pas):
            Déplace le robot en sens inverse de sa direction actuelle d'une distance spécifiée.

        calculer_angle(self, dest_x, dest_y):
            Calcule l'angle en degrés entre la direction actuelle du robot et la destination spécifiée.

        tourner(self, angle_degres):
            Tourne le robot d'un angle spécifié en radians.

    """
    
    def __init__(self,x,y,largeur,hauteur,direction_x,direction_y,environnement,rayon_roue):
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.environnement=environnement
         # Créer les roues avec un rayon de rRoue
        self.rayon_roue=rayon_roue

    def __str__(self):
        return "("+str(round(self.x,2))+","+str(round(self.y,2))+")"
    

    def uptade_position(self,vitesse_gauche,vitesse_droite):
        """Déplace le robot en fonction des vitesses spécifiées pour les roues gauche et droite.

        Args:
            vitesse_gauche (float): Vitesse de la roue gauche.
            vitesse_droite (float): Vitesse de la roue droite.

        """   
        # Calcul de la vitesse linéaire du robot (moyenne des vitesses des roues)
        vitesse_lineaire = (vitesse_gauche + vitesse_droite) / 2.0

        # Calcul de la rotation du robot (différence des vitesses des roues)
        print("SUUU "+str(self.rayon_roue))
        rotation = (vitesse_droite - vitesse_gauche) * self.rayon_roue / self.largeur

        # Mise à jour de la direction du robot
        nouvelle_direction_x = self.direction_x * math.cos(rotation) - self.direction_y * math.sin(rotation)
        nouvelle_direction_y = self.direction_x * math.sin(rotation) + self.direction_y * math.cos(rotation)

        # Normalisation de la nouvelle direction
        norme = math.sqrt(nouvelle_direction_x**2 + nouvelle_direction_y**2)
        nouvelle_direction_x /= norme
        nouvelle_direction_y /= norme

        # Nouvelles coordonnées en fonction de la direction et de la vitesse
        nouveau_x = self.x + vitesse_lineaire * nouvelle_direction_x
        nouveau_y = self.y + vitesse_lineaire * nouvelle_direction_y

        # Mise à jour des coordonnées et de la direction
        self.x = nouveau_x
        self.y = nouveau_y
        self.direction_x = nouvelle_direction_x
        self.direction_y = nouvelle_direction_y

        print(f"Position du robot : {self}")




    def calculer_angle(self, dest_x, dest_y):
        """Calcule l'angle en degrés entre la direction actuelle du robot et la direction vers une destination.

        Args:
            dest_x (float): Coordonnée x de la destination.
            dest_y (float): Coordonnée y de la destination.

        Returns:
            float: Angle en degrés entre la direction actuelle et la direction vers la destination.
        """

        # Calcul du vecteur entre la position actuelle et la destination
        vecteur_x = dest_x - self.x
        vecteur_y = dest_y - self.y

        # Calcul de la norme des deux vecteurs
        norme_direction = math.sqrt(self.direction_x**2 + self.direction_y**2)
        norme_vecteur = math.sqrt(vecteur_x**2 + vecteur_y**2)

        # Calcul du produit scalaire
        produit_scalaire = self.direction_x * vecteur_x + self.direction_y * vecteur_y

        # Calcul de l'angle en radians
        angle_radians = math.acos(produit_scalaire / (norme_direction * norme_vecteur))

        # Conversion de l'angle en degrés
        angle_degres = math.degrees(angle_radians)

        return angle_degres
    



    
    
