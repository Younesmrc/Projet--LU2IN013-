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
    
    def __init__(self, robot, environnement,angle):
        self.angle = angle
        self.robot = robot
        self.environnement = environnement

    def start(self):
        """ Initialise l'angle parcouru par le robot."""
        self.parcouru = 0
    
    def step(self):
        """ Effectue un petit pas de rotation vers la droite."""
        
        self.robot.set_vitesse(1, -1) 
        temps =((self.robot.vitesse_droite - self.robot.vitesse_gauche) * self.robot.rayon_roue / self.robot.largeur)*(180/math.pi)
        self.parcouru += temps
        
        if self.stop():
            return
        
        if not self.environnement.controle_collisions():
            self.robot.update_position()  
    
    def stop(self):
        """ Vérifie si l'angle de rotation spécifié est atteint."""
        return self.parcouru > self.angle
        