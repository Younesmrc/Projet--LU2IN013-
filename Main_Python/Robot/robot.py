import math

class Robot:
    
    def __init__(self,x,y,largeur,hauteur,directionx,directiony):
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.directionx = directionx
        self.directiony = directiony

    def avancer_vers(self,dest_x,dest_y,temps=1):

        Vecteur_x = dest_x - self.x
        Vecteur_y = dest_y - self.y

        NormeVecteur =math.sqrt(Vecteur_x**2 + Vecteur_y**2) #c'est la distance entre le robot et la destination

        if NormeVecteur == 0 :
            pass
        else:
            Vecteur_x_normal = Vecteur_x / NormeVecteur
            Vecteur_y_normal = Vecteur_y / NormeVecteur

            if NormeVecteur >= temps:

                self.x += temps * Vecteur_x_normal
                self.y += temps * Vecteur_y_normal

                # Mise à jour de la distance restante à parcourir
                NormeVecteur -= temps

                # Affichage de la nouvelle position (optionnel)
                
            if NormeVecteur < temps :
                self.x = dest_x
                self.y = dest_y
                return True

    def __str__(self):
        return "("+str(round(self.x,2))+","+str(round(self.y,2))+")"
    
    def avancer(self,pas):
        # Normaliser le vecteur direction
        norme = math.sqrt(self.directionx**2 + self.directiony**2)
        dx_normalise = self.directionx / norme
        dy_normalise = self.directiony / norme

        # Nouvelle coordonnée
        new_x = self.x + pas * dx_normalise
        new_y = self.y + pas * dy_normalise

        self.avancer_vers(new_x,new_y)

    def reculer(self,pas):
        self.avancer(-pas)
    
    def set_x_y(self,x,y):
        self.x=x
        self.y=y

    def calculer_angle(self, dest_x, dest_y):
        # Calcul du vecteur entre la position actuelle et la destination
        vecteur_x = dest_x - self.x
        vecteur_y = dest_y - self.y

        # Calcul de la norme des deux vecteurs
        norme_direction = math.sqrt(self.directionx**2 + self.directiony**2)
        norme_vecteur = math.sqrt(vecteur_x**2 + vecteur_y**2)

        # Calcul du produit scalaire
        produit_scalaire = self.directionx * vecteur_x + self.directiony * vecteur_y

        # Calcul de l'angle en radians
        angle_radians = math.acos(produit_scalaire / (norme_direction * norme_vecteur))

        # Conversion de l'angle en degrés
        angle_degres = math.degrees(angle_radians)

        return angle_degres
    
    def tourner(self, theta):
        # Convertir l'angle theta en radians
        theta_rad = math.radians(theta)

        # Effectuer la rotation des vecteurs de direction
        new_directionx = self.directionx * math.cos(theta_rad) - self.directiony * math.sin(theta_rad)
        new_directiony = self.directionx * math.sin(theta_rad) + self.directiony * math.cos(theta_rad)

        # Mettre à jour la direction du robot
        self.directionx, self.directiony = new_directionx, new_directiony

    