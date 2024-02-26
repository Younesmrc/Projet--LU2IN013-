from ..robot import Robot 
from ..environnement import Environnement
from .tourner_D import Tourner_D


class ControleurD:

    def __init__(self,robot,environnement,angle):
        angle=angle
        self.strats = [Tourner_D(robot,environnement,angle)]
        self.cur = -1

    