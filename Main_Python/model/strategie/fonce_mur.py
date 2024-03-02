from ..robot import Robot 
from ..environnement import Environnement
from .strats import Avancer

class FonceMur:
    """
    Classe représentant un contrôleur pour faire foncer un robotdans un mur.

    Attributs:
        robot (Robot): L'objet robot à contrôler.
        environnement: L'environnement dans lequel le robot opère.

    Méthodes:
        start(): Initialise le contrôleur.
        step(): Exécute une étape de la stratégie en cours.
        stop(): Vérifie si l'exécution des stratégies est terminée.

    """
    def __init__(self, robot, environnement):
        self.robot = robot
        self.environnement = environnement
        self.avancer_strat = Avancer(robot,environnement,float('inf'))  # Stratégie pour avancer indéfiniment
        self.detected_obstacle = False  #bool pour détecter si un obstacle a été rencontré

    def start(self):
        """ Initialise le contrôleur."""
        self.avancer_strat.start()
        self.detected_obstacle = False

    def step(self):
        """ Exécute une étape de la stratégie en cours."""
        if self.detected_obstacle:
            #Si un obstacle a été détecté, on arrête d'avancer
            self.robot.set_vitesse(0, 0)
        else:
            # Sinon, on continue d'avancer
            self.avancer_strat.step()
            # On vérifie si un obstacle est détecté
            dist=self.robot.detection_obstacle(self.environnement.liste_object[1:])
            if dist <= self.robot.largeur and dist > 0 : #si c'est inf a la largeur du robot (devant lui) et si c'est sup a 0 (cas du -1 dans la detection quand il detecte rien)
                self.detected_obstacle = True

    def stop(self):
        """ Vérifie si l'exécution des stratégies est terminée."""
        return self.detected_obstacle
