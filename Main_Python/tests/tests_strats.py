import unittest
import sys
sys.path.append("..")
from model.strategie.strategies import Avancer
from model.strategie.strategies import Tourner_D
from model.strategie.strategies import Tourner_G
from model.robot import Robot
from model.environnement import Environnement



class TestAvancer(unittest.TestCase):
    def setUp(self):
    #initialisation de l'environnement, du robot
        self.env = Environnement(400, 400, []) # Crée un environnement de 400x400 sans obstacles
        self.rob = Robot(0, 0, 5, 6, 200, 200, self.env,2) # Création d'un robot
        self.av = Avancer(self.rob,self.env,0)

    def test_avancer(self):
        i = 1
        self.av.start()  # Initialise l'action Avancer
        while not self.av.stop():
            for i in range (5): #On veut effectuer 5 tour de boucle (5 step)
                initial_parcouru = self.av.parcouru #On verifiera grace a cette ligne que le robot avance bien
                self.av.step() #Ligne qui dit au robot d'avancer
                print("Le robot a parcouru ",self.av.parcouru," pas")
                self.assertNotEqual(initial_parcouru, self.av.parcouru)
                self.assertEqual(self.av.parcouru,initial_parcouru+1) #Verification que le robot a bien avancer
            self.av.stop()
        return
        
#lancement des tests 
if __name__ == '__main__':
    unittest.main()