import math

class Tourner_D:
    """
    Classe représentant une action pour faire tourner un robot vers la droite dans un environnement donné.

    Attributs:
        robot (Robot): L'objet robot à contrôler.
        environnement: L'environnement dans lequel le robot opère.
        angle (float): L'angle de rotation à effectuer en degrés.

    Méthodes:
        start(): Initialise l'angle parcouru par le robot.
        step(): Effectue un petit pas de rotation vers la droite.
        stop(): Vérifie si l'angle de rotation spécifié est atteint.

    """
    
    def __init__(self, robot, environnement, angle):
        self.angle = angle
        self.robot = robot
        self.environnement = environnement
        self.angle_parcouru = 0
        self.angle_vise = 0
        
    def start(self):
        """ Initialise l'angle parcouru par le robot."""
        self.angle_parcouru = 0
        self.robot.set_vitesse(-1, 1)  # Rotation vers la droite
        self.angle_vise = self.robot.get_angle() + self.angle
        print("Angle visé au début de la rotation ",self.angle_vise)

    def step(self):
        """ Effectue un petit pas de rotation vers la droite."""
        
        angle_actuel = self.robot.get_angle()
        angle_restant = self.angle_vise - self.robot.get_angle()
        
        if self.angle_parcouru != 0:
            vitesse_angulaire = (self.angle - angle_restant) / self.angle_parcouru
        else:
            vitesse_angulaire = 0
        
        # Si l'angle restant à parcourir est plus petit que le pas de rotation, on ajuste le pas
        if vitesse_angulaire > angle_restant :
            print("ce cas arrive")
            self.robot.set_vitesse(-0.05, 0.05)
       
        self.angle_parcouru += 1
        
    def stop(self):
        """ Vérifie si l'angle de rotation spécifié est atteint."""
        return self.robot.get_angle() >= self.angle_vise
