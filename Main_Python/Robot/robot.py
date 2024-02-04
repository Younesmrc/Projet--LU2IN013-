import math

class Robot:
    
    def __init__(self,x,y,largeur,hauteur,direction_x,direction_y,environnement):
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.environnement=environnement

    def avancer_vers(self,dest_x,dest_y,temps=1):

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

                # Vérifier les collisions après le déplacement
                self.detecter_collision()

                # Mise à jour de la distance restante à parcourir
                norme_vecteur -= temps

                # Affichage de la nouvelle position (optionnel)
                print(f"Position du robot : {self}")
                
            if norme_vecteur < temps :
                self.x = dest_x
                self.y = dest_y
                # Vérifier les collisions après le déplacement
                self.detecter_collision()
                return True

    def __str__(self):
        return "("+str(round(self.x,2))+","+str(round(self.y,2))+")"
    
    def detecter_collision(self):
        # Vérifier les collisions avec les bords de l'environnement
        if self.x < 0:
            self.x = 0
        elif self.x > self.environnement.largeur - self.largeur:
            self.x = self.environnement.largeur - self.largeur

        if self.y < 0:
            self.y = 0
        elif self.y > self.environnement.hauteur - self.hauteur:
            self.y = self.environnement.hauteur - self.hauteur

    def avancer(self,pas):
        # Normaliser le vecteur direction
        norme = math.sqrt(self.direction_x**2 + self.direction_y**2)
        dx_normalise = self.direction_x / norme
        dy_normalise = self.direction_y / norme

        # Nouvelle coordonnée
        new_x = self.x + pas * dx_normalise
        new_y = self.y + pas * dy_normalise

        self.avancer_vers(new_x,new_y)

    def reculer(self,pas):
        self.avancer(-pas)


    def calculer_angle(self, dest_x, dest_y):
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
        # Convertir l'angle theta en radians
        theta_rad = math.radians(theta)

        # Effectuer la rotation des vecteurs de direction
        new_direction_x = self.direction_x * math.cos(theta_rad) - self.direction_y * math.sin(theta_rad)
        new_direction_y = self.direction_x * math.sin(theta_rad) + self.direction_y * math.cos(theta_rad)

        # Mettre à jour la direction du robot
        self.direction_x, self.direction_y = new_direction_x, new_direction_y

    