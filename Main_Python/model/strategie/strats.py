import math


class Avancer:
    """
    Représente une action pour faire avancer un robot dans un environnement donné.

    Attributs:
        distance (float): La distance totale à parcourir.
        robot (Robot): L'objet robot à contrôler.
        environnement: L'environnement dans lequel le robot opère.

    Méthodes:
        start(): Initialise la distance parcourue par le robot.
        step(): Déplace le robot vers l'avant d'un petit pas.
        stop(): Vérifie si le robot a parcouru la distance spécifiée.

    """
    def __init__(self, robot, environnement, distance):
        self.distance = distance
        self.robot = robot
        self.environnement = environnement

    def start(self):
        """Initialise la distance parcourue."""
        self.parcouru = 0
        self.robot.set_vitesse(1, 1) 

    def step(self):
        """Déplace le robot vers l'avant d'un petit pas."""
                

        # Calcul la distance parcouru en fonction de la vitesse
        self.parcouru += (self.robot.vitesse_gauche + self.robot.vitesse_droite) / 2  
        
        if self.stop():
            return
        
       

    def stop(self):
        """Vérifie si le robot a parcouru la distance spécifiée."""
        return self.parcouru > self.distance


class Tourner_D:
    """
    Classe représentant une action pour faire tourner un robot vers la droite dans un environnement donné.

    Attributs:
        robot (Robot): L'objet robot à contrôler.
        environnement: L'environnement dans lequel le robot opère.
        angle (float): L'angle de rotation à effectuer en degrés.
        cur (int): Compteur courant du nombre de step effectué
        angle_vise(float): Angle voulu par le robot par rapport à son angle de départ

    Méthodes:
        start(): Initialise l'angle parcouru par le robot.
        step(): Effectue un petit pas de rotation vers la droite.
        stop(): Vérifie si l'angle de rotation spécifié est atteint.

    """
    
    def __init__(self, robot, environnement, angle):
        self.angle = angle
        self.robot = robot
        self.environnement = environnement
        self.cur = 0
        self.angle_vise = 0
        
    def start(self):
        """ Initialise l'angle parcouru par le robot."""
        self.cur = 0 # Initialisation du compteur à 0
        self.robot.set_vitesse(-1, 1)  # Rotation vers la droite
        self.angle_vise = (self.robot.get_angle() + self.angle) % 360 # Calcul de l'angle final
        print("Angle visé au début de la rotation ",self.angle_vise)

    def step(self):
        """ Effectue un petit pas de rotation vers la droite."""
        print("angle visé ",self.angle_vise)
        print("angle ",self.angle)
        print("angle actuel ",self.robot.get_angle())
        
        # Calcul de l'angle restant par rapport à l'angle réel du robot
        angle_restant = self.angle_vise - self.robot.get_angle()
        print("angle restant ",angle_restant)

        # Calcul de la vitesse angulaire en fonction du nombre de step
        if self.cur != 0:
            vitesse_angulaire = (self.angle - angle_restant) / self.cur
        else:
            vitesse_angulaire = 0
        
        # Si l'angle restant à parcourir est plus petit que le pas de rotation, on ajuste le pas
        if vitesse_angulaire > angle_restant :
            self.robot.set_vitesse(-0.05, 0.05)

        # Augmentation du compteur
        self.cur += 1
        
    def stop(self):
        """ Vérifie si l'angle de rotation spécifié est atteint."""
        return self.robot.get_angle() >= self.angle_vise


class Tourner_G:
    """
    Classe représentant une action pour faire tourner un robot vers la gauche dans un environnement donné.

    Attributs:
        robot (Robot): L'objet robot à contrôler.
        environnement: L'environnement dans lequel le robot opère.
        angle (float): L'angle de rotation à effectuer en degrés.
        cur (int): Compteur courant du nombre de step effectué
        angle_vise(float): Angle voulu par le robot par rapport à son angle de départ

    Méthodes:
        start(): Initialise l'angle parcouru par le robot.
        step(): Effectue un petit pas de rotation vers la gauche.
        stop(): Vérifie si l'angle de rotation spécifié est atteint.

    """
    
    def __init__(self, robot, environnement, angle):
        self.angle = -angle
        self.robot = robot
        self.environnement = environnement
        self.cur = 0
        self.angle_vise = 0
        
    def start(self):
        """ Initialise l'angle parcouru par le robot."""
        self.cur = 0 # Initialisation du compteur à 0
        self.robot.set_vitesse(1, -1)  # Rotation vers la gauche
        self.angle_vise = (self.robot.get_angle() + self.angle) % 360 # Calcul de l'angle final
        print("Angle visé au début de la rotation ",self.angle_vise)

    def step(self):
        """ Effectue un petit pas de rotation vers la gauche."""
        print("angle visé ",self.angle_vise)
        print("angle ",self.angle)
        print("angle actuel ",self.robot.get_angle())

        # Calcul de l'angle restant par rapport à l'angle réel du robot
        angle_restant = (self.robot.get_angle() - self.angle_vise) % 360
        print("angle restant ",angle_restant)
        # Calcul de la vitesse angulaire en fonction du nombre de step
        if self.cur != 0:
            vitesse_angulaire = ((-self.angle - angle_restant) / self.cur)
        else:
            vitesse_angulaire = 0
        
        print("vitesse angulaire ",vitesse_angulaire)
        # Si l'angle restant à parcourir est plus petit que le pas de rotation, on ajuste le pas
        if vitesse_angulaire > angle_restant :
            self.robot.set_vitesse(0.05, -0.05)

        # Augmentation du compteur
        self.cur += 1
        
    def stop(self):
        """ Vérifie si l'angle de rotation spécifié est atteint."""
        return round(self.robot.get_angle()) == round(self.angle_vise)
