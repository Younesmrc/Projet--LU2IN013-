import pygame
from .environnement import Environnement
from .robot import Robot
from .objet import Objet
from .interface import *
from .strategie.strategies import *
from .strategie.controleur import *
from .constante import *

def get_environnement():
    return Environnement(largeur_environnement, hauteur_environnement, deltat)
    
def get_robot(robot_version):
    if robot_version == 1:
            robot = Robot(robot_x, robot_y, robot_longueur, robot_largeur, direction_x, direction_y, get_environnement(), 1.)
    elif robot_version == 2:
            from .irl.mockup import Robot2I013Mockup
            from .irl.robotadaptateur import RobotAdaptateur
            from .irl.RobotReel import Robot2IN013
            
            robot_reel = Robot2IN013()
            robot = RobotAdaptateur(robot_reel,robot_x,robot_y, direction_x, direction_y, get_environnement())
    else:
            raise ImportError("Version de robot non prise en charge")
    
    # Définition du robot
environnement.robot = robot
    
# Définition strategie
faire_carre = Controleur()
faire_carre.strategies=[Avancer(robot,environnement,100),Tourner_D(robot,environnement,90)]*4
fonce_mur = FonceMur(robot,environnement)

# Définition obstacle
obstacle = Objet(350, 350, 50, 50)
environnement.ajoute_object(robot)
environnement.ajoute_object(obstacle)
liste_obstacles = environnement.liste_object[1:]  # Ajout de tout sauf le robot

if graphique:
    pygame.init()
    fenetre = creation_fenetre(largeur_simu, hauteur_simu)
    robot_image = donner_image_robot(robot)



    


