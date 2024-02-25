from ..robot import Robot 
from ..environnement import Environnement
from .avancer import Avancer

class Controleur:

    def __init__(self,robot,environnement):
        distance=10000
        self.strats = [Avancer(robot,environnement,distance)]
        self.cur = -1

    def start(self):
        self.cur = -1

    def step(self):

        if self.stop():
            return
        
        if self.cur <0 or self.strats[self.cur].stop():
            self.cur+=1
            self.strats[self.cur].start()
            self.strats[self.cur].step()
        elif self.cur < len(self.strats):
            self.strats[self.cur].step()

    def stop(self):
        return self.cur== len(self.strats)-1 and self.strats[self.cur].stop()
    