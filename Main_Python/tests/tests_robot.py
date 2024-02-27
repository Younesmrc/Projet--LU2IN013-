import unittest
import sys
sys.path.append("..")
from model.robot import Robot
from model.environnement import Environnement
from model.objet import Objet

class TestRobot(unittest.TestCase):

    def setUp(self):
        #initialisation de l'environnement, du robot et de la roue pour chaque test
        self.env = Environnement(400, 400, [])#crée un environnement de 400x400 sans obstacles
        self.rob = Robot(0, 0, 5, 6, 200, 200, self.env,2)#crée un robot

    #Faire update position
        
    def test_angle(self):
        """L'objectif dans ce test est de donner une direction de base, puis de verifier l'angle de direction du robot en degrés, avec une marge d'erreur delta"""
        self.rob.direction_x= 1
        self.rob.direction_y = 1
        self.assertEqual(self.rob.get_angle(), 45)
        # l'angle doit etre = 45 comme la direction est en diagonale en haut a droite

        self.rob.direction_x = 1
        self.rob.direction_y = 0
        # l'angle du robot doit etre maintenant = a 0 (tout a droite)
        self.assertNotEqual(self.rob.get_angle(),45)
        self.assertEqual(self.rob.get_angle(),0)

    def test_set_vitesses(self):
        self.assertEqual(self.rob.vitesse_droite,1)
        self.assertEqual(self.rob.vitesse_droite,1)
        self.rob.set_vitesse(2,2)
        self.assertNotEqual(self.rob.vitesse_droite,1)
        self.assertNotEqual(self.rob.vitesse_droite,1)
        self.assertEqual(self.rob.vitesse_droite,2)
        self.assertEqual(self.rob.vitesse_droite,2)

        
    #faire detection_obstacle
        #Note pour moi meme, l'objectif est de voir si le robot detecte un obstacle dans la liste, il faut que ca soit false
        #Puis ensuite faire changer la direction du robot et il faut que cette fois il detecte l'obstacle
        #Facultatif, ca serait cool de tester la distance entre le robot et l'obstacle

#lancement des tests 
if __name__ == '__main__':
    unittest.main()
