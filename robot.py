import math

class Robot:
    
    def __init__(self,x,y,taille,direction):
        self.x = x
        self.y = y
        self.taille = taille
        self.direction = direction

    def avancer_vers(self,dest_x,dest_y):

        Vecteur_x = dest_x - self.x
        Vecteur_y = dest_y - self.y

        NormeVecteur =math.sqrt(Vecteur_x**2 + Vecteur_y**2) #c'est la distance entre le robot et la destination

        Vecteur_x_normal = Vecteur_x / NormeVecteur
        Vecteur_y_normal = Vecteur_y / NormeVecteur

        temps = 1


        print(str(round(NormeVecteur)))

        while NormeVecteur > 0:

            self.x += temps * Vecteur_x_normal
            self.y += temps * Vecteur_y_normal

            # Mise à jour de la distance restante à parcourir
            NormeVecteur -= temps

            # Affichage de la nouvelle position (optionnel)
            print("Les positions sont "+str(self))


    def __str__(self):
        return "("+str(round(self.x,2))+","+str(round(self.y,2))+")"
    
    def set_x_y(self,x,y):
        self.x=x
        self.y=y
    
robot = Robot(0,0,0,0)
robot.avancer_vers(3,5)
robot.avancer_vers(9,11)