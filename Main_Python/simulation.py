
import pygame
from model.environnement import Environnement
from model.robot import Robot
from model.objet import Objet
from model.interface import *
from model.strategie.controleur import Controleur


# Initialisation de Pygame
pygame.init()

# AVEC INTERFACE GRAPHIQUE ?
graphique=True

# Définition des variables
FPS = 30


#taille de l'environnement 
largeur_env = 1000
hauteur_env = 1000


# Définition de l'environnement
environnement = Environnement(largeur_env,hauteur_env)

# Définition du robot 
x,y=150,150 #position de depart du robot
long,large=30,30 #set taille du robot
direction_x,direction_y=1,1 #direction de depart
robot = Robot(x,y,long,large,direction_x,direction_y,environnement,1.)

# Definition obstacle
obstacle = Objet(350,350,50,50)
environnement.ajoute_object(robot)
environnement.ajout_obj_rand()
environnement.ajoute_object(obstacle)
liste_obstacles = environnement.liste_object[1:]

# Definition controleur

controleur = Controleur(robot,environnement,100)

if graphique :
    #taille de fenetre pygame
    largeur_simu = 500
    hauteur_simu = 500
    fenetre=creation_fenetre(largeur_simu,hauteur_simu)
    robot_image=donner_image_robot(robot)


# Démarrer la stratégie
controleur.start()

while True:

    environnement.controle_positions()
    # stratégie
    if not controleur.stop():
        controleur.step()

    # Test de la détection d'un obstacle 
    robot.detection_obstacle(liste_obstacles)

    if graphique :
        #recherche evenement pygame    
        evenement()
        #affichage dessin etc...
        interface(robot,environnement,obstacle,fenetre,robot_image)
        # Contrôle la vitesse de la boucle
        environnement.update(FPS)
    else :
        # Si l'interface graphique n'est pas activée,on effectue la simulation sans rien afficher
        environnement.update(FPS)
    