import math

class Objet :
    """Classe objet  répertoriant les fonctionnalités permettant de simuler un objet 

        Attributs:
        :x (float): La coordonnée x actuelle du robot.
        :y (float): La coordonnée y actuelle du robot.
        :largeur (float): La largeur du robot.
        :hauteur (float): La hauteur du robot.
        
        
    Méthodes:
       __init__(self, x, y, largeur, hauteur)
        Initialise un objet  avec les coordonnées, la largeur et la hauteur .
        """
        
    def __init__(self, x, y, largeur, hauteur):
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur

    
    def est_dans_obstacle(self,x,y):
        """ Méthode vérifiant si les coordonnées données en paramètre rentrent en collision avec l'objet

        Args:
            x (int): coordonnée en x
            y (int): coordonnée en y

        Returns:
            bool : retourne True ou False en fonction de la collision
        """
        
        if self.x <= x <= self.x + self.largeur and self.y <= y <= self.y + self.hauteur :
            return True
        return False



        
