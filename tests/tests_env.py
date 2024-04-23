import unittest

import sys
sys.path.append("..")
from Main_Python import *


class TestEnv(unittest.TestCase):
    
    # Initialisation de l'environnement, du robot et de la roue pour chaque test
    
    def setUp(self):
        self.env = Environnement(400, 400, [])
        self.robot1 = Robot(0, 0, 5, 6, 200, 200, self.env,2)
        self.robot2 = Robot(-10, -10, 10, 10, 200, 200, self.env, 2)
        self.obj =  Obstacle(0,0,5,5)
        self.env.ajoute_object(self.obj)
        self.env.ajoute_object(self.robot2)

    def test_ajoute(self):
        
        # Teste l'ajout du robot à l'environnement
        self.env.ajoute_object(self.robot1)
        self.assertIn(self.robot1,self.env.liste_object)

    def test_ajoute_rand(self):
        #La fonction ajoute_obj_rand ajoute aleatoirement entre 1 et 10 objet aleatoirement dans l'environnement
        #Nous allons donc voir si la liste des objets est differente avant et apres l'execution de ajout_obj_rand
        #Nous allons enfin regarder si le nombre d'objets ajouter aleatoirement est bien compris entre 1 et 10

        l1 = len(self.env.liste_object)
        self.env.ajout_obj_rand()
        l2 = len(self.env.liste_object)
        self.assertNotEqual(l1,l2)

        l3 = l2 - l1
        self.assertLessEqual(l3,10)
        self.assertGreaterEqual(l3,1)

    def test_ctrl_position(self):
        
        # Teste le contrôle des positions des objets dans l'environnement
        self.env.ajoute_object(self.robot2)
        self.env.ajoute_object(self.robot1)
        self.env.controle_positions()
        
        # Vérifie si les coordonnées de chaque robot est dans les limites du cadre de la fenêtre
        
        # Robot1
        self.assertEqual(self.robot1.x,0)
        self.assertEqual(self.robot2.y,0)

        # Robot2
        self.assertEqual(self.robot2.x,0)
        self.assertEqual(self.robot2.y,0)

    def test_ctrl_collisions(self):

        self.obj.x = 200
        self.obj.y = 200
        self.robot2.x = 160
        self.robot2.y = 160

        n = True
        
        while n:
            self.assertNotEqual(self.obj.x,self.robot2.x)
            self.assertNotEqual(self.obj.y,self.robot2.y)
            self.env.controle_collisions()
            self.robot2.x += 1
            self.robot2.y += 1
            print(self.robot2.x)
            if self.env.controle_collisions() == True:
                n = False

        print("Il y a eu une collision")
        
        #On verifie que les objets ne sont pas superposé
        self.assertNotEqual(self.obj.x,self.robot2.x)
        self.assertNotEqual(self.obj.y,self.robot2.y)
        
        #On verifie que les coordonnées de la collision a bien lieu au milieu de l'objet moins la largeur de l'objet en x et le robot en x
        self.assertNotEqual(200,200-self.obj.largeur-self.robot2.largeur)


# Lancer les tests
if __name__ == '__main__':
    unittest.main()
