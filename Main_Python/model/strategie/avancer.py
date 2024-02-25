from ..robot import Robot 

class Avancer :
    
    def __init__(self, robot, environnement,distance):
        self.distance = distance
        self.robot = robot
        self.environnement = environnement

    def start(self):
        self.parcouru = 0
    
    def step(self):
        self.robot.set_vitesse(1, 1)  # Ajuster les vitesses
        self.parcouru += (self.robot.vitesse_gauche + self.robot.vitesse_droite) / 2  # Mettre à jour la distance parcourue
        if self.stop():
            return
        self.robot.update_position()  # Mettre à jour la position du robot

    
    def stop(self):
        return self.parcouru > self.distance
        