import math
import time
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
        self.ballon = False

    
    def est_dans_obstacle(self,x,y):
        """ Méthode vérifiant si les coordonnées données en paramètre rentrent en collision avec l'objet

        Args:
            x (int): coordonnée en x
            y (int): coordonnée en y

        Returns:
            bool : retourne True si les coordonnées sont dans l'objet et False dans le cas inverse
        """
        
        return self.x <= x <= self.x + self.largeur and self.y <= y <= self.y + self.hauteur 

class Ballon (Objet):
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
        
    def __init__(self, x, y, largeur, hauteur,direction_x,direction_y,vitesse):
        super().__init__(x,y,largeur,hauteur)
        self.direction_x=direction_x
        self.direction_y=direction_y
        self.vitesse = vitesse
        self.ballon = True
        self.temps_passe = time.time()


    
    def est_dans_obstacle(self,x,y):
        """ Méthode vérifiant si les coordonnées données en paramètre rentrent en collision avec l'objet

        Args:
            x (int): coordonnée en x
            y (int): coordonnée en y

        Returns:
            bool : retourne True si les coordonnées sont dans l'objet et False dans le cas inverse
        """
        
        return self.x <= x <= self.x + self.largeur and self.y <= y <= self.y + self.hauteur 

    def update_position(self,robot):
        """Déplace le robot en fonction des vitesses spécifiées pour les roues gauche et droite.

        Args:
            vitesse_gauche (float): Vitesse de la roue gauche.
            vitesse_droite (float): Vitesse de la roue droite.
        """
        temps_actuel = time.time()
        delta_t = temps_actuel - self.temps_passe
        self.temps_passe = temps_actuel
        # Calcul de la vitesse linéaire du robot (moyenne des vitesses des roues)
        vitesse_lineaire = (robot.vitesse_gauche + robot.vitesse_droite) / 2.0
        v = max(0,abs(vitesse_lineaire)-delta_t*(0.01*(abs(vitesse_lineaire)**2)-0.06*abs(vitesse_lineaire)))
        # Nouvelles coordonnées en fonction de la direction et de la vitesse
        print(delta_t)
        nouveau_x = self.x + v * robot.direction_x * delta_t
        nouveau_y = self.y + v * robot.direction_y * delta_t

        # Mise à jour des coordonnées et de la direction
        self.x = nouveau_x
        self.y = nouveau_y
        self.direction_x = robot.direction_x 
        self.direction_y = robot.direction_y



        
