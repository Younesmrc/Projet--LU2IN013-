from simulation import *
import pygame

FPS = 30

graphique = True #true pour ouvrir la fenetre false sinon

#taille de l'environnement
largeur_environnement = 1000
hauteur_environnement = 1000
#taille de la fenetre de simulation
largeur_simu = 500
hauteur_simu = 500

#Definition variables du robot

robot_x,robot_y = (150,150)  
robot_longueur,robot_largeur = (30,30) 
direction_x,direction_y = (1,1)

distance = 100

run_simulation(FPS,graphique,largeur_environnement,hauteur_environnement,largeur_simu,hauteur_simu,robot_x,robot_y,robot_longueur,robot_largeur,direction_x,direction_y,distance)