import math

class Obstacle :
    """Classe obstacle  répertoriant les fonctionnalités permettant de simuler un obstacle

        Attributs:
        :x (float): La coordonnée x actuelle de l'obstacle.
        :y (float): La coordonnée y actuelle de l'obstacle.
        :largeur (float): La largeur de l'obstacle.
        :hauteur (float): La hauteur de l'obstacle.
        
        
    Méthodes:
       __init__(self, x, y, largeur, hauteur)
        Initialise un obstacle  avec les coordonnées, la largeur et la hauteur .
        """
        
    def __init__(self, x, y, largeur, hauteur):
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur

    
    def est_dans_obstacle(self,x,y):
        """ Méthode vérifiant si les coordonnées données en paramètre rentrent en collision avec l'obstacle

        Args:
            x (int): coordonnée en x
            y (int): coordonnée en y

        Returns:
            bool : retourne True si les coordonnées sont dans l'obstacle et False dans le cas inverse
        """
        
        return self.x <= x <= self.x + self.largeur and self.y <= y <= self.y + self.hauteur 



        
