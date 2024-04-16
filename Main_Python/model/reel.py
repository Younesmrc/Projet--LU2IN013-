import pygame
from graphique.interface import *
from controller.strategies import Avancer,Tourner,Sequentiel
from controller.controleur import Controleur
from .constante import fps_controleur
import threading
import time

class Reel:
    """
    Class chapeau pour les threads
    """

    def __init__(self, controleur,robot):
        self.robot = robot
        self.running = True
        self.controleur = controleur
        self.arret_a_la_fin_du_controleur = True

    def run_controleur_reel(self):
        """
        Permet de run le robot adaptateur sans environnement
        """
        self.controleur.start()
        while not self.controleur.stop():
                self.controleur.step()
                time.sleep(1 / fps_controleur)
        self.running = False


    def run_reel(self):
        """
        Run du robot reel qui lance :
        -boucle du controleur
        + mise a jour du update a chaque step du controleur
        """
        thread_controler = threading.Thread(target=self.run_controleur_reel, args=())
        thread_controler.start()
        