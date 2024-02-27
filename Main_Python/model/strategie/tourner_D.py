from ..robot import Robot 
import math

class Tourner_D :
    """
    Classe représentant une action pour faire tourner un robot vers la droite dans un environnement donné.

    Attributs:
        robot (Robot): L'objet robot à contrôler.
        environnement: L'environnement dans lequel le robot opère.
        angle (float): L'angle de rotation à effectuer en degrés.

    Méthodes:
        start(): Initialise l'angle parcouru par le robot.
        step(): Effectue un petit pas de rotation vers la droite.
        stop(): Vérifie si l'angle de rotation spécifié est atteint.

    """
    
    def __init__(self, robot, environnement, angle):
        self.angle = angle
        self.robot = robot
        self.environnement = environnement
        self.angle_parcouru = 0
    
    def start(self):
        """ Initialise l'angle parcouru par le robot."""
        self.angle_parcouru = 0
    
    def step(self):
        """ Effectue un petit pas de rotation vers la droite."""
        x_direction_avant = self.robot.direction_x
        y_direction_avant = self.robot.direction_y
        
        if self.stop():
            return
        
        self.robot.set_vitesse(-1, 1)  # Rotation vers la droite
        
        # Mise à jour de la position du robot
        self.robot.update_position()

        x_direction_apres = self.robot.direction_x
        y_direction_apres = self.robot.direction_y
        
        # Calcul de l'angle de rotation effectué
        angle_rotation = self.angle_entre_vecteurs(x_direction_avant, y_direction_avant, x_direction_apres, y_direction_apres)
        self.angle_parcouru += angle_rotation

    def stop(self):
        """ Vérifie si l'angle de rotation spécifié est atteint."""
        return self.angle_parcouru >= self.angle
    
    @staticmethod
    def angle_entre_vecteurs(x1, y1, x2, y2):
        """Calcule l'angle entre deux vecteurs."""
        # Calcul des produits scalaires
        produit_scalaire = x1 * x2 + y1 * y2
        
        # Calcul des normes des vecteurs
        norme_u = math.sqrt(x1 ** 2 + y1 ** 2)
        norme_v = math.sqrt(x2 ** 2 + y2 ** 2)
        
        # Calcul de l'angle entre les deux vecteurs en radians
        angle_radians = math.acos(produit_scalaire / (norme_u * norme_v))
        
        # Convertir l'angle en degrés
        angle_degrees = math.degrees(angle_radians)
        
        return angle_degrees

    @staticmethod
    def rotate_vector(x, y, angle):
        """Effectue une rotation du vecteur (x, y) par l'angle spécifié."""
        # Conversion de l'angle en radians
        angle_radians = math.radians(angle)
        
        # Calcul des nouvelles composantes du vecteur
        x_new = x * math.cos(angle_radians) - y * math.sin(angle_radians)
        y_new = x * math.sin(angle_radians) + y * math.cos(angle_radians)
        
        return x_new, y_new