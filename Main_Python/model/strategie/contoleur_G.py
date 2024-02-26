from ..robot import Robot 
from ..environnement import Environnement
from .tourner_G import Tourner_G


class controleur_G:

    def __init__(self,robot,environnement,angle):
        self.tourner_G = Tourner_G(robot, environnement, angle)
        

    def start(self):
        self.tourner_G.start()

    def step(self):
        self.tourner_G.step()

    def stop(self):
        return self.tourner_G.stop()
