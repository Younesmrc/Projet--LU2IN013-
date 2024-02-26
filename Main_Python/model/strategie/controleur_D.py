from ..robot import Robot 
from ..environnement import Environnement
from .tourner_D import Tourner_D

class controleur_D:
    """
    Classe représentant un contrôleur pour faire tourner un robot vers la droite dans un environnement donné.

    Attributs:
        robot (Robot): L'objet robot à contrôler.
        environnement: L'environnement dans lequel le robot opère.
        angle (float): L'angle de rotation à effectuer.

    Méthodes:
        start(): Initialise le contrôleur pour commencer l'action.
        step(): Exécute une étape de l'action en cours.
        stop(): Vérifie si l'action de rotation est terminée.

    """
    
    def __init__(self, robot, environnement, angle):
        self.tourner_d = Tourner_D(robot, environnement, angle)

    def start(self):
        """ Initialise l'action de rotation vers la droite."""
        self.tourner_d.start()

    def step(self):
        """ Exécute une étape de l'action de rotation vers la droite."""
        self.tourner_d.step()

    def stop(self):
        """ Vérifie si l'action de rotation est terminée."""
        return self.tourner_d.stop()
