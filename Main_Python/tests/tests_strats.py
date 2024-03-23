import unittest
import sys
sys.path.append("..")
from model.strategie.strats import Avancer
from model.strategie.strats import Tourner_D
from model.strategie.strats import Tourner_G
from model.robot import Robot
from model.environnement import Environnement



class TestAvancer(unittest.TestCase):
    def setUp(self):
    #initialisation de l'environnement, du robot
        self.env = Environnement(400, 400, []) # Crée un environnement de 400x400 sans obstacles
        self.rob = Robot(0, 0, 5, 6, 1, 1, self.env,10) # Création d'un robot
        self.av = Avancer(self.rob,self.env,0)
        self.angle = 90  # Angle de rotation à effectuer

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
    
class TestTourner(unittest.TestCase):
    def setUp(self):
    #initialisation de l'environnement, du robot
        self.env = Environnement(400, 400, []) # Crée un environnement de 400x400 sans obstacles
        self.rob2 = Robot(0, 0, 5, 6, 1, 1, self.env,10) # Création d'un robot
        self.angle = 90  # Angle de rotation à effectuer
        self.tourner_d = Tourner_D(self.rob2, self.env, self.angle)  # Crée une action Tourner_D

    def test_tourner_d(self):
        self.tourner_d.start()
        angle_restant = (self.tourner_d.angle_vise - self.rob2.get_angle()) % 360
        self.rob2.set_vitesse(-9,9)
        self.assertEqual(self.tourner_d.cur,0)
        print("angle du rob", self.rob2.get_angle())
        while not self.tourner_d.stop():
            self.tourner_d.step()
            print("vit angulaire du rob",(self.angle - angle_restant) / self.tourner_d.cur)
            print("vitess angle_restant ",angle_restant)
            print("angle ajouté ",self.angle)
            print("angle du rob", self.rob2.get_angle())
            print("cur ", self.tourner_d.cur)
        self.assertEqual(self.rob2.get_angle(),self.tourner_d.angle_vise)
        return
        
#lancement des tests 
if __name__ == '__main__':
    unittest.main()