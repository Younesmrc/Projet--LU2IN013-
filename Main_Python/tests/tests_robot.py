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
        self.obj = Objet(0,0,3,3)
        self.env.ajoute_object(self.obj)

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

        

    def test_detection_obstacle(self):
        self.obj.x = 100
        self.obj.y = 0
        #Nous placons un objet en coordonnées 100 0
        self.rob.direction_x = 0
        self.rob.direction_y = -1
        #Le robot regarde en bas, soit dans une direction ou il n'y a pas d'objet
        #Verifions que le robot ne detecte aucun objet
        self.assertEqual(self.rob.detection_obstacle(self.env.liste_object),None)
        self.rob.direction_x = 1
        self.rob.direction_y = 0
        #A présent, le robot regarde en direction de l'obstacle
        self.assertNotEqual(self.rob.detection_obstacle(self.env.liste_object),None)
        #Regardons a présent si la distance entre le robot et l'obstacle est bien de 100
        self.assertEqual(self.rob.detection_obstacle(self.env.liste_object),100)
        #La distance est bien de 100, faisons avancer le robot pour voir si cela marche toujours
        self.rob.x = 5
        #Avec ces parametres, le robot n'est plus qu'a une distance de 95 de l'obstacle, verifions cela
        self.assertEqual(self.rob.detection_obstacle(self.env.liste_object),95)




#lancement des tests 
if __name__ == '__main__':
    unittest.main()
