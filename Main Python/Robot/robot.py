import math

class Robot:
    
    def __init__(self,x,y,taille,directionx,directiony):
        self.x = x
        self.y = y
        self.taille = taille
        self.directionx = directionx
        self.directiony = directiony

    def avancer_vers(self,dest_x,dest_y,temps=1):

        Vecteur_x = dest_x - self.x
        Vecteur_y = dest_y - self.y

        NormeVecteur =math.sqrt(Vecteur_x**2 + Vecteur_y**2) #c'est la distance entre le robot et la destination

        Vecteur_x_normal = Vecteur_x / NormeVecteur
        Vecteur_y_normal = Vecteur_y / NormeVecteur

        print(str(round(NormeVecteur)))
        while NormeVecteur > temps:

            self.x += temps * Vecteur_x_normal
            self.y += temps * Vecteur_y_normal

            # Mise à jour de la distance restante à parcourir
            NormeVecteur -= temps

            # Affichage de la nouvelle position (optionnel)
            print("Les positions sont "+str(self))

        self.x = dest_x
        self.y = dest_y
        print("Les positions sont "+str(self))

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
    
robot = Robot(0,0,0,1,0)
robot.avancer_vers(3,5,1)
print()
robot.avancer(10)
robot.reculer(10)