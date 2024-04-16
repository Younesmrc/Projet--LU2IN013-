import pygame
from graphique.interface import *
from controller.strategies import Avancer,Tourner_D,Tourner_G,Sequentiel
from controller.controleur import Controleur
from .constante import fps_environnement,fps_controleur,fps_interface
import threading
import time

class Simulation:
    """
    Class chapeau pour les threads
    """

    def __init__(self, controleur,robot,environnement,graphique):
        self.robot = robot
        self.graphique= graphique
        self.running = True
        self.controleur = controleur
        self.environnement = environnement
        self.arret_a_la_fin_du_controleur = True

    def run_controleur(self):
        """
        boucle du controleur
        """
        self.controleur.start()
        while not self.controleur.stop():
            if not self.environnement.controle_collisions():
                self.controleur.step()
            time.sleep(1 / fps_controleur)

        self.running=False

    def run_controleur_reel(self):
        """
        Permet de run le robot adaptateur sans environnement
        """
        self.controleur.start()
        while not self.controleur.stop():
                self.controleur.step()
                time.sleep(1 / fps_controleur)
        self.running = False

    def run_environnement(self):
        """
        Boucle de l'environnement
        """
        while self.running:
            if not self.environnement.controle_positions():
                if not self.environnement.controle_collisions():
                    self.environnement.update(fps_environnement)

    def run_interface(self, robot, environnement):
        """
        Boucle de l'interface
        """
        pygame.init()
        fenetre = creation_fenetre(largeur_simu, hauteur_simu)
        robot_image = donner_image_robot(robot)
        while self.running:
            evenement(self.running)  
            interface(robot, environnement, fenetre, robot_image)  
            time.sleep(1 / fps_interface)

    def run_simulation(self):
        """
        Run de la simulation qui lance la simulation avec
        -boucle du controleur
        -boucle de l'environnement
        -boucle de l'interface.
        """
        thread_controler = threading.Thread(target=self.run_controleur, args=())
        thread_env = threading.Thread(target=self.run_environnement, args=())
        if self.graphique:
            thread_interface = threading.Thread(target=self.run_interface, args=(self.robot, self.environnement))
            thread_interface.start()
        thread_env.start()
        thread_controler.start()

    def run_reel(self):
        """
        Run du robot reel qui lance :
        -boucle du controleur
        + mise a jour du update a chaque step du controleur
        """
        thread_controler = threading.Thread(target=self.run_controleur_reel, args=())
        thread_controler.start()
        