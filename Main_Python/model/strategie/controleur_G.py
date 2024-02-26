from ..robot import Robot 
from ..environnement import Environnement
from .tourner_G import Tourner_G


class controleur_G:
    """
    Classe représentant un contrôleur pour faire tourner un robot vers la gauche dans un environnement donné.

    Attributs:
        robot (Robot): L'objet robot à contrôler.
        environnement: L'environnement dans lequel le robot opère.
        angle (float): L'angle de rotation à effectuer.

    Méthodes:
        start(): Initialise le contrôleur pour commencer l'action.
        step(): Exécute une étape de l'action en cours.
        stop(): Vérifie si l'action de rotation est terminée.

    """

    def __init__(self,robot,environnement,angle):
        self.tourner_G = Tourner_G(robot, environnement, angle)
        

    def start(self):
        """ Initialise l'action de rotation vers la droite."""
        self.tourner_G.start()

    def step(self):
        """ Exécute une étape de l'action de rotation vers la droite."""
        self.tourner_G.step()

    def stop(self):
        """ Vérifie si l'action de rotation est terminée."""
        return self.tourner_G.stop()
