from ..robot import Robot 
from ..environnement import Environnement
from .tourner_G import Tourner_G


class controleur_G:

    def __init__(self,robot,environnement,angle):
        self.tourner_d = Tourner_G(robot, environnement, angle)
        

    def start(self):
        self.tourner_D.start()

    def step(self):
        self.tourner_D.step()

    def stop(self):
        return self.tourner_.stop()
