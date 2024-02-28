import unittest
import sys
sys.path.append("..")
from model.robot import Robot
from model.environnement import Environnement
from model.objet import Objet

class TestRobot(unittest.TestCase):

    def setUp(self):
        #initialisation de l'environnement, du robot et de la roue pour chaque test
        self.env = Environnement(400, 400, []) # Crée un environnement de 400x400 sans obstacles
        self.rob = Robot(0, 0, 5, 6, 200, 200, self.env,2) # Création d'un robot
        self.rob2 = Robot(5, 5, 5, 6, 200, 200, self.env,2,2,-1) # Création d'un second robot effectuant une rotation
        self.obj = Objet(0,0,3,3)
        self.env.ajoute_object(self.obj)

    #Faire update position
    def test_update_position(self):
        """ Ce test doit vérifier si le robot effectue bien un déplacement après l'appel de la fonction update_position. 
            On rappelle que le robot 1 se trouve en (0,0) et le robot 2 en (5.0,5.0) à l'origine
        """

        # Coordonnées avant le déplacement des robots :
        rob1_x = self.rob.x
        rob1_y = self.rob.y

        rob2_x = self.rob2.x
        rob2_y = self.rob2.y

        # Déplacement des robots, la vitesse de chaque roue est de 1
        self.rob.update_position()
        self.rob2.update_position()

        # Vérification que les robots du déplacement des robots
        self.assertNotEqual((self.rob.x, self.rob.y), (0,0))
        self.assertNotEqual((self.rob2.x, self.rob2.y), (5,5))

        # Vérification de la position relative du robot 1
        self.assertAlmostEqual( (self.rob.x) , (rob1_x + self.rob.direction_x), 5) 
        self.assertAlmostEqual( (self.rob.y) , (rob1_y + self.rob.direction_y), 5) 

        # Afin de vérifier la position du robot tout en prenant compte sa rotation, il est nécessaire de recalculer certains paramètres :
        vitesse_lineaire = (self.rob2.vitesse_gauche + self.rob2.vitesse_droite) / 2.0

        # Vérification de la position relative du robot 2
        self.assertAlmostEqual( (self.rob2.x) , (rob2_x + self.rob2.direction_x * vitesse_lineaire) , 5)
        self.assertAlmostEqual( (self.rob2.y) , (rob2_y + self.rob2.direction_y * vitesse_lineaire) , 5)


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
