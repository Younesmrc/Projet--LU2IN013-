import math
from ..robot import Robot 
from ..environnement import Environnement


class TracerRond:
    """
    Classe représentant une action pour faire tracer un rond à un robot dans un environnement donné.

    Attributs:
        robot (Robot): L'objet robot à contrôler.
        environnement: L'environnement dans lequel le robot opère.
        rayon (float): Le rayon du cercle à tracer.
        vitesse_lineaire (float): La vitesse linéaire du robot.
        vitesse_angulaire (float): La vitesse angulaire pour faire tourner le robot autour du cercle.

    Méthodes:
        start(): Initialise les paramètres nécessaires pour tracer le rond.
        step(): Effectue un petit pas de rotation pour faire tracer le rond.
        stop(): Vérifie si l'angle voulu est atteint.

    """
    
    def __init__(self, robot, environnement, distance):
        self.robot = robot
        self.environnement = environnement
        self.distance = distance 

        self.angle_vise = 0

    def start(self):
        """ Initialise les paramètres nécessaires pour tracer le rond."""
        self.parcouru = 0
        self.robot.set_vitesse(2, 1) 

    def step(self):
        """Déplace le robot vers l'avant d'un petit pas."""
                

        # Calcul la distance parcouru en fonction de la vitesse
        self.parcouru += (self.robot.vitesse_gauche + self.robot.vitesse_droite) / 2  
        
        if self.stop():
            return
        
       

    def stop(self):
        """Vérifie si le robot a parcouru la distance spécifiée."""
        return self.parcouru > self.distance * 2.85