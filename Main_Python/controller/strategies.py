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
        self.robot.set_vitesse(100,100) 

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
        self.vitesse_rotation = 1  # Vitesse de rotation du robot
        self.aproximation = 0
        self.cpt = 0

    def start(self):
        """Initialise la stratégie de rotation."""
        self.robot.reset_angle()  # Remise à zéro de l'angle parcouru
        self.robot.update_distance()
        self.cpt=0
        if self.sens :
            self.angle_vise = (self.robot.get_angle() + self.angle) % 360
        else :
            self.angle_vise = (self.robot.get_angle() - self.angle) % 360
        if self.sens:
            self.robot.set_vitesse(-self.vitesse_rotation, self.vitesse_rotation)  # Rotation vers la gauche
        else:
            self.robot.set_vitesse(self.vitesse_rotation, -self.vitesse_rotation)  # Rotation vers la droit


    def step(self):
        """Exécute une étape de la rotation."""
        # Mise à jour de l'angle parcouru
        self.robot.update_distance()
        print(" ANGLE REEL PARCOURU : "+str(abs(self.robot.get_angle())))
        self.robot.angle_restant(self.cpt,self.angle_vise,self.angle,self.sens)
        self.cpt +=1

    def stop(self):
        """Vérifie si la rotation est terminée."""
        #abs(self.robot.get_angle()) >= (self.angle - self.aproximation)
        if self.robot.condition_angle(self.angle_vise,self.angle,self.aproximation,self.sens):
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
    
class Chercher_balise:
    """
    Classe représentant une stratégie pour chercher une balise dans un environnement donné en tournant par étapes de 10 degrés.
    
    Attributs:
        robot (Robot): L'objet robot à contrôler.
        environnement: L'environnement dans lequel le robot opère.
        angle_step (float): L'angle de chaque étape de rotation en degrés.
        max_angle (float): L'angle maximal à tourner pour chercher la balise.
        current_angle (float): L'angle actuellement parcouru.
        trouver (bool): Indique si la balise a été trouvée.
        avancer_strat (Avancer): La stratégie pour avancer une fois la balise trouvée.
    
    Méthodes:
        start(): Initialise la stratégie de recherche.
        step(): Exécute une étape de la recherche.
        stop(): Vérifie si la recherche est terminée.
    """

    def __init__(self, robot, environnement):
        self.robot = robot
        self.environnement = environnement
        self.angle_step = 10  # Angle de chaque étape de rotation
        self.max_angle = 360  # Angle maximal à tourner
        self.current_angle = 0  # Angle actuellement parcouru
        self.trouver = False  # Indique si la balise a été trouvée
        self.avancer_strat = None  # Stratégie pour avancer une fois la balise trouvée
    
    def start(self):
        """Initialise la stratégie de recherche."""
        self.current_angle = 0
        self.trouver = False
        self.robot.reset_angle()
        self.tourner_strat = Tourner_reel(self.robot, self.angle_step, sens=True)  # Rotation vers la gauche
        self.tourner_strat.start()
    
    def step(self):
        """Exécute une étape de la recherche."""
        if self.trouver:
            self.avancer_strat.step()
        else:
            self.tourner_strat.step()
            if self.tourner_strat.stop():
                # Prendre une photo et traiter l'image pour détecter la balise
                image = self.robot.prendre_photo()
                time.sleep(1)
                x, y = get_position_balise(image)
                time.sleep(5)
                print("X : "+str(x)+" Y : "+str(y))
                if x != -1 and y != -1:
                    # Balise trouvée
                    self.trouver = True
                    self.avancer_strat = Avancer(self.robot, self.environnement, 1000)  # Distance à parcourir après avoir trouvé la balise
                    self.avancer_strat.start()
                else:
                    # Balise non trouvée, tourner de 10 degrés supplémentaires
                    self.current_angle += self.angle_step
                    if self.current_angle >= self.max_angle:
                        # Complété un tour complet
                        self.robot.set_vitesse(0, 0)
                    else:
                        # Continuer à tourner
                        self.tourner_strat = Tourner_reel(self.robot, self.angle_step, sens=True)
                        self.tourner_strat.start()
    
    def stop(self):
        """Vérifie si la recherche est terminée."""
        return self.trouver and self.avancer_strat.stop()
