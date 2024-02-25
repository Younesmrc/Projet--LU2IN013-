from ..robot import Robot 

class Avancer :
    
    def __init__(self, robot, environnement,distance):
        self.distance = distance
        self.robot = robot
        self.environnement = environnement

    def start(self):
        self.parcouru = 0
    
    def step(self):
        self.robot.set_vitesse(1, 1) 
        self.parcouru += (self.robot.vitesse_gauche + self.robot.vitesse_droite) / 2  
        if self.stop():
            return
        if not self.environnement.controle_collisions():
            self.robot.update_position()  

    
    def stop(self):
        return self.parcouru > self.distance
        