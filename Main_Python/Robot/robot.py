import math

class Robot:
    """Classe Robot répertoriant les fonctionnalités permettant de simuler un robot

    Attributes:
        :x (float): La coordonnée x actuelle du robot.
        :y (float): La coordonnée y actuelle du robot.
        :largeur (float): La largeur du robot.
        :hauteur (float): La hauteur du robot.
        :direction_x (float): La composante x du vecteur de direction du robot.
        :direction_y (float): La composante y du vecteur de direction du robot.
    
    Methods:
        __init__(self, x, y, largeur, hauteur, direction_x, direction_y):
            Initialise un objet Robot avec les coordonnées, la taille et la direction spécifiées.

        avancer_vers(self, dest_x, dest_y, temps=1):
            Déplace le robot vers la destination spécifiée en ajustant sa position en fonction du temps.

        __str__(self):
            Renvoie une représentation sous forme de chaîne de la position actuelle du robot.

        avancer(self, pas):
            Déplace le robot dans sa direction actuelle d'une distance spécifiée.

        reculer(self, pas):
            Déplace le robot en sens inverse de sa direction actuelle d'une distance spécifiée.

        calculer_angle(self, dest_x, dest_y):
            Calcule l'angle en degrés entre la direction actuelle du robot et la destination spécifiée.

        tourner(self, theta):
            Tourne le robot d'un angle spécifié en radians.

    """
    
    def __init__(self,x,y,largeur,hauteur,direction_x,direction_y):
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.direction_x = direction_x
        self.direction_y = direction_y

    def avancer_vers(self,dest_x,dest_y,temps=1):
        """Déplace le robot vers une destination spécifiée.

        Args:
            dest_x (float): Coordonnée x de la destination.
            dest_y (float): Coordonnée y de la destination.
            temps (float, optional): Temps de déplacement. Par défaut, 1.

        Returns:
            bool: True si le déplacement est terminé, False sinon.
        """

        vecteur_x = dest_x - self.x
        vecteur_y = dest_y - self.y

        norme_vecteur =math.sqrt(vecteur_x**2 + vecteur_y**2) #c'est la distance entre le robot et la destination

        if norme_vecteur == 0 :
            pass
        else:
            vecteur_x_normal = vecteur_x / norme_vecteur
            vecteur_y_normal = vecteur_y / norme_vecteur

            if norme_vecteur >= temps:

                self.x += temps * vecteur_x_normal
                self.y += temps * vecteur_y_normal

                # Mise à jour de la distance restante à parcourir
                norme_vecteur -= temps

                # Affichage de la nouvelle position (optionnel)
                print(f"Position du robot : {self}")
                
            if norme_vecteur < temps :
                self.x = dest_x
                self.y = dest_y
                return True

    def __str__(self):
        return "("+str(round(self.x,2))+","+str(round(self.y,2))+")"
    
    def avancer(self,pas):
         """Déplace le robot d'une distance spécifiée dans sa direction actuelle.

        Args:
            pas (float): Distance à parcourir.

        Returns:
            None
        """   
        
        # Normaliser le vecteur direction
        norme = math.sqrt(self.direction_x**2 + self.direction_y**2)
        dx_normalise = self.direction_x / norme
        dy_normalise = self.direction_y / norme

        # Nouvelle coordonnée
        new_x = self.x + pas * dx_normalise
        new_y = self.y + pas * dy_normalise

        self.avancer_vers(new_x,new_y)

    def reculer(self,pas):
        """Recule le robot.

        Args:
            pas (float): Distance à parcourir.
        """

        self.avancer(-pas)


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
    
    def tourner(self, theta):
        """Tourne la direction du robot d'un angle spécifié en degrés.

        Args:
            theta (float): Angle de rotation en degrés.

        Returns:
            None
        """

        # Convertir l'angle theta en radians
        theta_rad = math.radians(theta)

        # Effectuer la rotation des vecteurs de direction
        new_direction_x = self.direction_x * math.cos(theta_rad) - self.direction_y * math.sin(theta_rad)
        new_direction_y = self.direction_x * math.sin(theta_rad) + self.direction_y * math.cos(theta_rad)

        # Mettre à jour la direction du robot
        self.direction_x, self.direction_y = new_direction_x, new_direction_y

    