from ..robot import Robot 
from ..environnement import Environnement
from .avancer import Avancer

class Controleur:
    """
    Classe représentant un contrôleur pour orchestrer les actions d'un robot dans un environnement donné.

    Attributs:
        robot (Robot): L'objet robot à contrôler.
        environnement: L'environnement dans lequel le robot opère.
        distance (float): La distance maximale à parcourir.

    Méthodes:
        start(): Initialise le contrôleur.
        step(): Exécute une étape de la stratégie en cours.
        stop(): Vérifie si l'exécution des stratégies est terminée.

    """
    def __init__(self, robot, environnement, distance):
        distance = 10000  
        self.strats = [Avancer(robot, environnement, distance)]
        self.cur = -1

    def start(self):
        """ Initialise le contrôleur en réinitialisant l'indice de stratégie courant."""
        self.cur = -1

    def step(self):
        """ Exécute une étape de la stratégie en cours ou passe à la suivante si nécessaire."""
        if self.stop():
            return
        
        if self.cur < 0 or self.strats[self.cur].stop():
            self.cur += 1
            self.strats[self.cur].start()
            self.strats[self.cur].step()
        
        elif self.cur < len(self.strats):
            self.strats[self.cur].step()

    def stop(self):
        """ Vérifie si l'exécution des stratégies est terminée."""
        return self.cur == len(self.strats) - 1 and self.strats[self.cur].stop()


