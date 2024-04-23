import pygame
from Main_Python import *
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
        fenetre = creation_fenetre(LARGEUR_SIMU, HAUTEUR_SIMU)
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
        time.sleep(1/100) #le controleur s'execute trop rapidement du coup les premiers point ne s'affiche pas quand le robot dessine
        thread_controler.start()


        