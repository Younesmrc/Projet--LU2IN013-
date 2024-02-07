import unittest
import sys
sys.path.append("..")
from model.robot import Robot, Roue
from model.environnement import Environnement

class TestRobot(unittest.TestCase):

    def setUp(self):
        #initialisation de l'environnement, du robot et de la roue pour chaque test
        self.env = Environnement(400, 400, [])#crée un environnement de 400x400 sans obstacles
        self.rob = Robot(0, 0, 5, 6, 200, 200, self.env,2)#crée un robot 
        self.roue = Roue(2, self.rob)#crée une roue

    def test_robot_instanceof(self):
        #vérifie si les instance sont bien crées comme prévu 
        self.assertIsInstance(self.rob, Robot)

    def test_avancer(self):
        robx = self.rob.x
        roby = self.rob.y
        self.rob.avancer(4)
        self.assertNotEqual(robx,self.rob.x)
        self.assertNotEqual(roby,self.rob.y)

    def test_reculer(self):
        robx = self.rob.x
        roby = self.rob.y
        self.rob.reculer(6)
        self.assertNotEqual(robx,self.rob.x)
        self.assertNotEqual(roby,self.rob.y)

class TestRoue(unittest.TestCase):

    def setUp(self):
        self.env = Environnement(400, 400, [])
        self.rob = Robot(0, 0, 5, 6, 200, 200, self.env,2)
        self.roue = Roue(2, self.rob)

    def test_roue_instanceof(self):
        self.assertIsInstance(self.roue,Roue)
#lancement des tests 
if __name__ == '__main__':
    unittest.main()
