import math

class Objet :
    """Classe objet  répertoriant les fonctionnalités permettant de simuler un objet 

        Attributs:
        :x (float): La coordonnée x actuelle de l'objet.
        :y (float): La coordonnée y actuelle de l'objet.
        :largeur (float): La largeur de l'objet.
        :hauteur (float): La hauteur de l'objet.
        
        
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
            bool : retourne True si les coordonnées sont dans l'objet et False dans le cas inverse
        """
        
        return self.x <= x <= self.x + self.largeur and self.y <= y <= self.y + self.hauteur 



        
