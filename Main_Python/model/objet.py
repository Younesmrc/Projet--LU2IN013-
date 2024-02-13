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


class Robot(Objet):
    def __init__(self, x, y, largeur, hauteur, direction_x, direction_y, environnement, rayon_roue):
        super().__init__(x, y, largeur, hauteur)
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.environnement = environnement
        self.rayon_roue = rayon_roue

    def collision_avec_objet(self, objet):
        """
        Vérifie s'il y a collision avec un autre objet (override de la méthode dans la classe Robot).
        """

        # Exemple d'une logique de collision spécifique au robot (à adapter selon vos besoins) :
        if isinstance(objet, Robot):
            # La collision avec un autre robot est gérée différemment, si nécessaire.
            return False

        return super().collision_avec_objet(objet)
        
