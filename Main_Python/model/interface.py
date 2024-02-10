import pygame
from .environnement import Environnement
from .robot import Robot

BLANC = (255,255,255)
FPS = 30
ROUGE = (255, 0, 0)

def creation_fenetre(environnement):
    fenetre = pygame.display.set_mode((environnement.largeur,environnement.hauteur))
    pygame.display.set_caption("Simulation robot")
    return fenetre