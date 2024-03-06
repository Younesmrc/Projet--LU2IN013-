import unittest
import sys
sys.path.append("..")
from model.strategie.strats import Avancer
from model.strategie.strats import Tourner_D
from model.strategie.strats import Tourner_G
from model.robot import Robot
from model.environnement import Environnement
from model.strategie.faire_carre import FaireCarre

class TestCarre(unittest.TestCase):
    def setUp(self):
    #initialisation de l'environnement, du robot
        self.env = Environnement(400, 400, []) # Crée un environnement de 400x400 sans obstacles
        self.rob = Robot(0, 0, 5, 6, 1, 1, self.env,2) # Création d'un robot
        self.av = Avancer(self.rob,self.env,0)
        self.angle = 90  # Angle de rotation fectuer
        self.tourner_d = Tourner_D(self.rob, self.env, self.angle)  # Crée une action Tourner_D
        self.distance = 10
        self.tourner = "D"
        self.faire_carre = FaireCarre(self.rob,self.env,self.distance,self.tourner)

    def tests_carre(self):
        self.faire_carre.start()
        self.assertEqual(self.faire_carre.cur, -1)  # Vérifie si cur est initialisé à -1
        while not self.faire_carre.stop():
            self.faire_carre.step()  # Exécute toutes les étapes des stratégies jusqu'à la fin
        self.assertEqual(self.faire_carre.cur, len(self.faire_carre.strats) - 1)  # Vérifie si cur est égal à la longueur de strats - 1


#lancement des tests 
if __name__ == '__main__':
    unittest.main()