import math
class objet :
    """Classe objet  répertoriant les fonctionnalités permettant de simuler un objet 

        Attributs:
        :x (float): La coordonnée x actuelle du robot.
        :y (float): La coordonnée y actuelle du robot.
        :largeur (float): La largeur du robot.
        :hauteur (float): La hauteur du robot.
        
        
    Méthodes:
       __init__(self, x, y, largeur, hauteur)
        """
        
    def __init__(self, x, y, largeur, hauteur):
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur

        
