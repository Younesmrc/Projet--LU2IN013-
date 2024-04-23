import unittest
import sys
sys.path.append("..")

from Main_Python import *

class TestObjet(unittest.TestCase):

    def setUp(self):

        # Initialisation d'objet 1 et 2 de paramètres différents
        self.objet_1 = Obstacle(0,0,10,10) # Objet aux coordonnées (0,0)
        self.objet_2 = Obstacle(10,20,10,10) # Objet aux coordonnées (10,20)

    def test_est_dans_obstacle(self):

        # Tests les coordonnées de l'objet 1 dans différentes configurations
        self.assertTrue(self.objet_1.est_dans_obstacle(7,8))
        self.assertFalse(self.objet_1.est_dans_obstacle(11,25))

        # Tests les coordonnées de l'objet 1 dans différentes configurations
        self.assertTrue(self.objet_2.est_dans_obstacle(15,25))
        self.assertFalse(self.objet_2.est_dans_obstacle(9,17))

# Résolution des tests
if __name__ == '__main__':
    unittest.main()