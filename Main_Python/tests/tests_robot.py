import unittest

from ..model.robot import Robot
from ..model.environnement import Environnement
from ..model.objet import Objet

class TestRobot(unittest.TestCase):

    def setUp(self):
        #initialisation de l'environnement, du robot et de la roue pour chaque test
        self.env = Environnement(400, 400, [])#crée un environnement de 400x400 sans obstacles
        self.rob = Robot(0, 0, 5, 6, 200, 200, self.env,2)#crée un robot

    def test_angle(self):
        """L'objectif dans ce test est de donner une direction de base, puis de verifier l'angle de direction du robot en degrés, avec une marge d'erreur delta"""
        self.rob.direction_x= 1
        self.rob.direction_y = 1

        angle_resultat = self.rob.get_angle()
        # l'angle doit etre = 45 comme la direction est en diagonale en haut a droite
        self.assertAlmostEqual(angle_resultat, 45, delta=0.01)



#lancement des tests 
if __name__ == '__main__':
    unittest.main()
