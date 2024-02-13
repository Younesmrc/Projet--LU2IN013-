import unittest
import sys
sys.path.append("..")
from model.robot import Robot
from model.environnement import Environnement

class TestRobot(unittest.TestCase):

    def setUp(self):
        #initialisation de l'environnement, du robot et de la roue pour chaque test
        self.env = Environnement(400, 400, [])#crée un environnement de 400x400 sans obstacles
        self.rob = Robot(0, 0, 5, 6, 200, 200, self.env,2)#crée un robot

    def test_angle(self):
        # Créez une instance de votre classe Robot avec des coordonnées directionnelles appropriées
        self.rob.direction_x= 1
        self.rob.direction_y = 1
        # Appelez la méthode get_angle()
        angle_resultat = self.rob.get_angle()
        # Vérifiez que l'angle est proche de 0 degré (vers la droite)
        print(self.assertAlmostEqual(angle_resultat, 45, delta=0.01))

#lancement des tests 
if __name__ == '__main__':
    unittest.main()
