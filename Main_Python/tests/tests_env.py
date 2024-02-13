import unittest
import sys
sys.path.append("..")
from model.robot import Robot
from model.environnement import Environnement


class TestEnv(unittest.TestCase):
    # Initialisation de l'environnement, du robot et de la roue pour chaque test
    def setUp(self):
        self.env = Environnement(400, 400, [])
        self.rob = Robot(0, 0, 5, 6, 200, 200, self.env,2)
        self.robotest = Robot(-10, -10, 10, 10, 200, 200, self.env, 2)

    def test_ajoute(self):
        # Teste l'ajout du robot à l'environnement
        self.env.ajoute_object(self.rob)
        self.assertIn(self.rob,self.env.liste_object)

    def test_ctrl_position(self):
         # Teste le contrôle des positions des objets dans l'environnement
        self.env.ajoute_object(self.robotest)
        self.env.controle_positions()
        # Vérifie que les coordonnées du robot test sont correctement ajustées
        self.assertEqual(self.robotest.x,0)
        self.assertEqual(self.robotest.y,0)

    def test_ctrl_collisions(self):

        self.rob.x = 200
        self.rob.y = 200
        self.robotest.x = 199
        self.robotest.y = 199
        self.env.controle_collisions()
        self.assertNotEqual(self.rob.x,self.robotest.x)
        self.assertNotEqual(self.rob.y,self.robotest.y)

    def test_ajuste_position(self):

        self.rob.x = 200
        self.rob.y = 200
        self.robotest.x = 199
        self.robotest.y = 199
        self.env.ajuster_position(self.robotest,self.rob)
        self.assertEqual(self.robotest.x,190)
        self.assertEqual(self.robotest.y,190)

    def test_collision(self):
        self.rob.x = 200
        self.rob.y = 200
        self.robotest.x = 200
        self.robotest.y = 200
        self.assertTrue(self.env.collision(self.rob,self.robotest))
#lancer les testes
if __name__ == '__main__':
    unittest.main()
