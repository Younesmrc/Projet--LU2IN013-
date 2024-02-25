
class Avancer :
    
    def __init__(self, robot, environnement,distance):
        self.distance = distance
        self.robot = robot
        self.environnement = environnement

    def start(self):
        self.parcouru = 0
    
    def step(self):
        
        self.parcouru += ( robot.vitesse_gauche + robot.vitesse_droite ) / 2
        print("distance parcouru :" parcouru) 

        if self.stop(): return None
        
        self.avancer()
    
    def stop(self):
        return self.parcouru > self.distance
        
    def avancer(self) :

        self.robot.update_position(robot.vitesse_gauche, robot.vitesse_droite)