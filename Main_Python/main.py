import math
from simulation import *
import pygame

FPS = 60

graphique = True #true pour ouvrir la fenetre false sinon

#vitesse des updates du robot :
deltat=2

#taille de l'environnement
largeur_environnement = 500
hauteur_environnement = 500
#taille de la fenetre de simulation
largeur_simu = 500
hauteur_simu = 500

#Definition variables du robot

robot_x,robot_y = (150,150)  
robot_longueur,robot_largeur = (30,30) 
direction_x,direction_y = (1,0)

#variable pour la stratégie rond 
rayon = 10
vitesse_lineaire = 1
vitesse_angulaire = math.radians(5)


run_simulation(FPS,graphique,largeur_environnement,hauteur_environnement,largeur_simu,hauteur_simu,robot_x,robot_y,robot_longueur,robot_largeur,direction_x,direction_y,rayon, vitesse_lineaire,vitesse_angulaire,deltat)