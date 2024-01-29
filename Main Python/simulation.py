import pygame
from Environnement.environnement import Environnement
from Robot.robot import Robot




# Initialisation de Pygame
pygame.init()

# Définition des couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
FPS = 30

# Paramètres de la fenêtre
largeur_fenetre = 400
hauteur_fenetre = 400

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Déplacement automatique du carré")

#definition robot
robot=Robot(50,50,25,50,1,1)

#definition environnement
environnement=Environnement(400,400,fenetre)

