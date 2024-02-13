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

def donner_image_robot(robot):
    robot_image = pygame.image.load("robot3.png")
    robot_image = pygame.transform.scale(robot_image,(robot.hauteur*2,robot.largeur*2))  # Redimensionner l'image
    return robot_image

def effacer_ecran(fenetre):
    fenetre.fill(BLANC)

def rotation(robot,robot_image):
    rotated_robot = pygame.transform.rotate(robot_image,-robot.get_angle()-45)  # Utilisez l'angle du robot ici
    return rotated_robot


def dessine(robot,robot2,robot_image,fenetre,environnement):
        rotated_robot = rotation(robot,robot_image)
        rotated_rect = rotated_robot.get_rect(center=(round(robot.x), round(robot.y)))
        pygame.draw.rect(fenetre,ROUGE,(round(robot2.x), round(robot2.y),20,20))
        for objet in environnement.liste_object:
            pygame.draw.rect(fenetre, ROUGE, (round(objet.x), round(objet.y), objet.largeur, objet.hauteur))
        fenetre.blit(rotated_robot, rotated_rect.topleft)

def rafraichissement():
    return pygame.display.flip()

def tracer_trait_derriere_robot(robot, fenetre):
    """Trace un trait derrière le robot en utilisant ses positions précédentes."""
    positions = robot.get_precedente_positions()
    if len(positions) > 1:
        pygame.draw.lines(fenetre, ROUGE, False, positions, 2)
