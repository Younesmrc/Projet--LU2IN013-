import math
from ..robot import Robot 
from ..environnement import Environnement


class TracerRond:
    """
    Classe représentant une action pour faire tracer un rond à un robot dans un environnement donné.

    Attributs:
        robot (Robot): L'objet robot à contrôler.
        environnement: L'environnement dans lequel le robot opère.
        rayon (float): Le rayon du cercle à tracer.
        vitesse_lineaire (float): La vitesse linéaire du robot.
        vitesse_angulaire (float): La vitesse angulaire pour faire tourner le robot autour du cercle.

    Méthodes:
        start(): Initialise les paramètres nécessaires pour tracer le rond.
        step(): Effectue un petit pas de rotation pour faire tracer le rond.
        stop(): Vérifie si l'angle voulu est atteint.

    """
    
    def __init__(self, robot, environnement, rayon, vitesse_lineaire, vitesse_angulaire):
        self.robot = robot
        self.environnement = environnement
        self.rayon = rayon
        self.vitesse_lineaire = vitesse_lineaire
        self.vitesse_angulaire = vitesse_angulaire
        self.angle_vise = 0

    def start(self):
        """ Initialise les paramètres nécessaires pour tracer le rond."""
        self.angle_vise = 0

    def step(self):
        """ Effectue un petit pas de rotation pour faire tracer le rond."""
        temps_passe = self.robot.update_temps_passe()
        self.angle_vise +=self.vitesse_lineaire * temps_passe 
        distance_parcourue = self.vitesse_angulaire * temps_passe

         # Calcul des vitesses des roues pour un mouvement circulaire
        vitesse_gauche = self.vitesse_lineaire - (self.vitesse_angulaire * self.rayon)
        vitesse_droite = self.vitesse_lineaire + (self.vitesse_angulaire * self.rayon)

        self.robot.set_vitesse(vitesse_gauche, vitesse_droite)

    def stop(self):
        """ Vérifie si l'angle voulu est atteint."""
        return abs(self.robot.get_angle() - self.angle_vise) < 0.1
