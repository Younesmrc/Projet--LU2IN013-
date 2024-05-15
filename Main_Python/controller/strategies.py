from Main_Python.Traitement_image import *
import time
from PIL import Image
import numpy as np


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
        self.robot.reset_distance()
        self.robot.set_vitesse(200,200) 

    def step(self):
        """Déplace le robot vers l'avant d'un petit pas."""

        self.robot.update_distance()
       
    def stop(self):
        """Vérifie si le robot a parcouru la distance spécifiée."""
        #print("GET DISTANCE POUR AVANCER : "+str(self.robot.get_distance()))
        if self.robot.get_distance() > self.distance :
            self.robot.set_vitesse(0,0) 
            self.robot.reset_distance()
            return True
        return False


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
        self.angle_parcouru = 0
        
    def start(self):
        """ Initialise l'angle parcouru par le robot."""
        self.cur = 0 # Initialisation du compteur à 0
        self.robot.set_vitesse(-1, 1)  # Rotation vers la droite
        self.angle_vise = (self.robot.get_angle() + self.angle) % 360 # Calcul de l'angle final


    def step(self):
        """ Effectue un petit pas de rotation vers la droite."""

        self.robot.update_distance()
        self.angle_parcouru += self.robot.angle_parcouru
        self.robot.reset()
        # Calcul de l'angle restant par rapport à l'angle réel du robot
        angle_restant = (self.angle_vise - self.robot.get_angle()) % 360
        # Calcul de la vitesse angulaire en fonction du nombre de step
        if self.cur != 0:
            vitesse_angulaire = (self.angle - angle_restant) / self.cur
        else:
            vitesse_angulaire = 0
        # Si l'angle restant à parcourir est plus petit que le pas de rotation, on ajuste le pas
        if vitesse_angulaire > angle_restant :
            self.robot.set_vitesse(-0.025, 0.025)

        # Augmentation du compteur
        self.cur += 1
        
    def stop(self):
        """ Vérifie si l'angle de rotation spécifié est atteint."""
        if self.robot.condition_angle(self.angle_vise):
            print("PASSAGE")
            self.robot.set_vitesse(0,0)
            return True
        return False


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
        self.angle = angle
        self.robot = robot
        self.environnement = environnement
        self.cur = 0
        self.angle_vise = 0
        self.angle_parcouru = 0
        
    def start(self):
        """ Initialise l'angle parcouru par le robot."""
        self.cur = 0 # Initialisation du compteur à 0
        self.robot.set_vitesse(1, -1)  # Rotation vers la gauche
        self.angle_vise = (self.robot.get_angle() - self.angle) % 360 # Calcul de l'angle final
        print("Angle visé au début de la rotation ",self.angle_vise)

    def step(self):
        """ Effectue un petit pas de rotation vers la gauche."""
        self.robot.update_distance()
        self.angle_parcouru += self.robot.angle_parcouru
        self.robot.reset()
        # Calcul de l'angle restant par rapport à l'angle réel du robot
        angle_restant = (self.robot.get_angle() - self.angle_vise) % 360

        # Calcul de la vitesse angulaire en fonction du nombre de step
        if self.cur != 0:
            vitesse_angulaire = ((self.angle - angle_restant) / self.cur)
        else:
            vitesse_angulaire = 0

        # Si l'angle restant à parcourir est plus petit que le pas de rotation, on ajuste le pas
        if vitesse_angulaire > angle_restant :
            self.robot.set_vitesse(0.025, -0.025)

        # Augmentation du compteur
        self.cur += 1
        
    def stop(self):
        """ Vérifie si l'angle de rotation spécifié est atteint."""
        if self.robot.condition_angle(self.angle_vise):
            self.robot.set_vitesse(0,0)
            return True
        return False
    
class Sequentiel:
    """
    Classe représentant un contrôleur pour orchestrer les actions d'un robot dans un environnement donné.

    Attributs:
        robot (Robot): L'objet robot à contrôler.
        environnement: L'environnement dans lequel le robot opère.
        distance (float): La distance maximale à parcourir.
        tourner (str): Le sens dans lequel le robot doit tourner ("D" pour droite, "G" pour gauche).

    Méthodes:
        start(): Initialise le contrôleur.
        step(): Exécute une étape de la stratégie en cours.
        stop(): Vérifie si l'exécution des stratégies est terminée.

    """
    def __init__(self):
        # La liste des startegies
        self.strategies = []

        # La startegie courrante
        self.current_strat = -1
    
    def start(self):
        """ Initialise le contrôleur en réinitialisant l'indice de stratégie courant."""
        self.cur = -1

    def step(self):
        """ Exécute une étape de la stratégie en cours ou passe à la suivante si nécessaire."""
        
        if self.cur < 0 or self.strategies[self.cur].stop():
            print("ICI")
            self.cur += 1
            self.strategies[self.cur].start()
            self.strategies[self.cur].step()
        
        elif self.cur < len(self.strategies):
            self.strategies[self.cur].step()

    def stop(self):
        """ Vérifie si l'exécution des stratégies est terminée."""
        return self.cur == len(self.strategies) - 1 and self.strategies[self.cur].stop()   
    
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
    def __init__(self, robot, environnement,ecartAvecMur):
        self.robot = robot
        self.ecartAvecMur = ecartAvecMur
        self.environnement = environnement
        self.avancer_strat = Avancer(robot,environnement,float('inf'))  # Stratégie pour avancer indéfiniment
        self.detected_obstacle = False  #bool pour détecter si un obstacle a été rencontré
        self.arret = False

    def start(self):
        """ Initialise le contrôleur."""
        self.robot.set_vitesse(100,100)
        self.detected_obstacle = False

    def step(self):
        """ Exécute une étape de la stratégie en cours."""
        if self.detected_obstacle:
            #Si un obstacle a été détecté, on arrête d'avancer
            self.robot.set_vitesse(0, 0)
            self.arret = True
        else:
            # On vérifie si un obstacle est détecté
            dist=self.robot.detection_obstacle(self.environnement.liste_object[1:])
            print("Distance element plus proche :"+str(dist))
            if dist <= self.ecartAvecMur and dist > 0 : #si c'est inf a la largeur du robot (devant lui) et si c'est sup a 0 (cas du -1 dans la detection quand il detecte rien)
                self.detected_obstacle = True

    def stop(self):
        """ Vérifie si l'exécution des stratégies est terminée."""
        return self.arret

class Boucle :
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
    def __init__(self,strategie):
        self.strategie = strategie 
    def step(self):
        """
        Exécute une étape de la stratégie en cours.
        """
        self.strategie.step()
    def stop(self):
        """
        Vérifie si l'exécution des stratégies est terminée.
        """
        return False
    def restart(self):
        """
        Redémarre la stratégie si elle s'est arrêtée.
        """
        self.strategie.start()
     
class Tourner_reel:
    """
    Classe représentant une stratégie pour faire tourner un robot dans un environnement donné.

    Attributs:
        robot (Robot): L'objet robot à contrôler.
        environnement: L'environnement dans lequel le robot opère.
        angle (float): L'angle à tourner, en degrés.
        sens (str): Le sens dans lequel le robot doit tourner ("D" pour droite, "G" pour gauche).

    Méthodes:
        start(): Initialise la stratégie de rotation.
        step(): Exécute une étape de la rotation.
        stop(): Vérifie si la rotation est terminée.

    """
    def __init__(self, robot, angle, sens):
        self.robot = robot
        self.angle = angle
        self.sens = sens
        self.angle_parcouru = 0
        self.vitesse_rotation = 100  # Vitesse de rotation du robot
        self.aproximation = 0

    def start(self):
        """Initialise la stratégie de rotation."""
        self.robot.reset_angle()  # Remise à zéro de l'angle parcouru
        self.robot.update_distance()
        if self.sens:
            self.robot.set_vitesse(-self.vitesse_rotation, self.vitesse_rotation)  # Rotation vers la gauche
        else:
            self.robot.set_vitesse(self.vitesse_rotation, -self.vitesse_rotation)  # Rotation vers la droit


    def step(self):
        """Exécute une étape de la rotation."""
        # Mise à jour de l'angle parcouru
        self.robot.update_distance()
        print(" ANGLE REEL PARCOURU : "+str(abs(self.robot.get_angle())))



    def stop(self):
        """Vérifie si la rotation est terminée."""
        if abs(self.robot.get_angle()) >= (self.angle - self.aproximation):
            self.robot.set_vitesse(0,0)
            return True
        return False

class Suivre_balise:
    """
    Classe représentant une stratégie pour faire tourner un robot dans un environnement donné.

    Attributs:
        robot (Robot): L'objet robot à contrôler.
        environnement: L'environnement dans lequel le robot opère.
        angle (float): L'angle à tourner, en degrés.
        sens (str): Le sens dans lequel le robot doit tourner ("D" pour droite, "G" pour gauche).

    Méthodes:
        start(): Initialise la stratégie de rotation.
        step(): Exécute une étape de la rotation.
        stop(): Vérifie si la rotation est terminée.

    """
    def __init__(self, robot):
        self.robot = robot
        self.detected = False

    def start(self):
        """Initialise la stratégie de rotation."""
        self.robot.robot.start_recording()
        time.sleep(1)
        self.image = self.robot.robot.get_image()
        self.x,self.y = get_position_balise(self.image)

    def step(self):
        """Exécute une étape de la rotation."""
        print("X ET Y:"+str(self.x)+" "+ str(self.y))
        # Mise à jour de l'angle parcouru
        if self.x == -1 and self.y == -1 :
            self.robot.set_vitesse(-50,50)
        else:
            self.robot.set_vitesse(0,0)

        self.image = self.robot.robot.get_image()
        self.x,self.y = get_position_balise(self.image)
        print('SLEEP')
        time.sleep(3)
        print("end")



    def stop(self):
        """Vérifie si la rotation est terminée."""
        return False
