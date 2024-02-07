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
    
    def __init__(self,x,y,largeur,hauteur,direction_x,direction_y,environnement,rRoue):
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.environnement=environnement
         # Créer les roues avec un rayon de rRoue
        self.roue_gauche = Roue(rayon=rRoue, robot=self)
        self.roue_droite = Roue(rayon=rRoue, robot=self)
        #vitesse_des_roues
        self.vitesse_g = 0.
        self.vitesse_d = 0.

    def __str__(self):
        return "("+str(round(self.x,2))+","+str(round(self.y,2))+")"
    

    def avancer(self,distance,vitesse=1.0):
        """Déplace le robot d'une distance spécifiée dans sa direction actuelle.

        Args:
            distance (float): Distance à parcourir.
            vitesse (float): Facteur de vitesse. Par défaut, 1.0.

        Returns:
            None
        """   
        # Normaliser le vecteur direction
        norme = math.sqrt(self.direction_x**2 + self.direction_y**2)
        dx_normalise = self.direction_x / norme
        dy_normalise = self.direction_y / norme

        # Nouvelles coordonnées en fonction de la distance et de la vitesse
        new_x = self.x + vitesse * dx_normalise
        new_y = self.y + vitesse * dy_normalise

        # Mise à jour des coordonnées
        self.x = new_x
        self.y = new_y

        print(f"Position du robot : {self}")



    def reculer(self,distance):
        """Recule le robot.

        Args:
            distance (float): Distance à parcourir.
        """

        self.avancer(-distance)


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
    
    def set_vitesse(self,vg,vd):
        self.vitesse_g = vg
        self.vitesse_d = vd

    def calculer_angle_robot(self, temps):
        # Calculer la vitesse linéaire de chaque roue
        vitesse_lineaire_gauche = self.vitesse_g * self.roue_gauche.rayon
        vitesse_lineaire_droite = self.vitesse_d * self.roue_droite.rayon
        
        # Calculer la différence de vitesse linéaire entre les deux roues
        difference_vitesse = vitesse_lineaire_droite - vitesse_lineaire_gauche
        
        # Calculer la vitesse de rotation du robot (en radians par unité de temps)
        vitesse_rotation = difference_vitesse / self.largeur
        
        # Convertir la vitesse de rotation en angle en radians
        angle_radians = vitesse_rotation * temps

        # Convertir l'angle en degrés si nécessaire
        angle_degres = math.degrees(angle_radians)

        return angle_degres
    
    
    def freinage_progressif(self, deceleration_rate):
        """Applique un freinage progressif au robot.

        Args:
            deceleration_rate (float): Taux de décélération. Plus le taux est élevé, plus le freinage est rapide.

        Returns:
            None
        """
        # Déterminer la direction du freinage en fonction de la vitesse actuelle des roues
        if self.vitesse_g > 0:
            self.vitesse_g -= deceleration_rate
            if self.vitesse_g < 0:
                self.vitesse_g = 0
        elif self.vitesse_g < 0:
            self.vitesse_g += deceleration_rate
            if self.vitesse_g > 0:
                self.vitesse_g = 0

        if self.vitesse_d > 0:
            self.vitesse_d -= deceleration_rate
            if self.vitesse_d < 0:
                self.vitesse_d = 0
        elif self.vitesse_d < 0:
            self.vitesse_d += deceleration_rate
            if self.vitesse_d > 0:
                self.vitesse_d = 0


    
    
