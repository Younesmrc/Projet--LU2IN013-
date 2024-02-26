from ..robot import Robot 
import math

class Tourner_D :
    
    def __init__(self, robot, environnement,angle):
        self.angle = angle
        self.robot = robot
        self.environnement = environnement

    def start(self):
        self.parcouru = 0
    
    def step(self):
        self.robot.set_vitesse(1, -1) 
        temps =((self.robot.vitesse_droite - self.robot.vitesse_gauche) * self.robot.rayon_roue / self.robot.largeur)*(180/math.pi)
        self.parcouru += temps
        if self.stop():
            return
        if not self.environnement.controle_collisions():
            self.robot.update_position()  

    
    def stop(self):
        return self.parcouru > self.angle
        