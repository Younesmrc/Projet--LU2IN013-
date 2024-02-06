import unittest
import sys
sys.path.append("..")
from model.robot import Robot, Roue
from model.environnement import Environnement

class TestEnv(unittest.TestCase):
    def test_instanceof(self):  # Correction du nom de la méthode
        env = Environnement(400, 400, [])
        self.assertIsInstance(env, Environnement)

class TestRobot(unittest.TestCase):
    def test_robot_instanceof(self):  # Correction du nom de la méthode
        env1 = Environnement(400, 400, [])
        rob1 = Robot(0, 0, 5, 6, 200, 200, env1,2)
        self.assertIsInstance(rob1, Robot)

class TestRoue(unittest.TestCase):
    def test_roue_instanceof(self):  # Correction du nom de la méthode
        env2 = Environnement(400, 400, [])
        rob2 = Robot(0, 0, 5, 6, 200, 200, env2,2)  # Correction de l'utilisation de env2
        r = Roue(2, rob2, 45)

if __name__ == '__main__':
    unittest.main()
