import unittest
import sys
sys.path.append("..")
from model.robot import Robot, Roue
from model.environnement import Environnement


class TestEnv(unittest.TestCase):

    def setUp(self):
        self.env = Environnement(400, 400, [])
        self.rob = Robot(0, 0, 5, 6, 200, 200, self.env,2)
        self.roue = Roue(2, self.rob, 45)

    def test_instanceof(self):
        self.assertIsInstance(self.env, Environnement)
        self.env.ajoute_object(self.rob)
        self.assertIn(self.rob,self.env.liste_object)


class TestRobot(unittest.TestCase):

    def setUp(self):
        self.env = Environnement(400, 400, [])
        self.rob = Robot(0, 0, 5, 6, 200, 200, self.env,2)
        self.roue = Roue(2,self.rob, 45)

    def test_robot_instanceof(self):
        self.assertIsInstance(self.rob, Robot)

class TestRoue(unittest.TestCase):

    def setUp(self):
        self.env = Environnement(400, 400, [])
        self.rob = Robot(0, 0, 5, 6, 200, 200, self.env,2)
        self.roue = Roue(2, self.rob, 45)

    def test_roue_instanceof(self):
        self.assertIsInstance(self.roue,Roue)

if __name__ == '__main__':
    unittest.main()
