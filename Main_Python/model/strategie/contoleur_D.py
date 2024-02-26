from ..robot import Robot 
from ..environnement import Environnement
from .tourner_D import Tourner_D


class controleur_D:

    def __init__(self,robot,environnement,angle):
        self.tourner_d = Tourner_D(robot, environnement, angle)
        

    def start(self):
        self.tourner_D.start()

    def step(self):
        self.tourner_D.step()

    def stop(self):
        return self.tourner_.stop()
