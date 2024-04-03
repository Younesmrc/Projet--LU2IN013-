import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE
from model.constante import largeur_simu,hauteur_simu,BLANC,ROUGE

def creation_fenetre(largeur_simu,hauteur_simu):
    fenetre = pygame.display.set_mode((largeur_simu,hauteur_simu))
    pygame.display.set_caption("Simulation robot")
    return fenetre

def donner_image_robot(robot):
    robot_image = pygame.image.load("source/robot3.png")
    robot_image = pygame.transform.scale(robot_image,(robot.hauteur*2,robot.largeur*2))  # Redimensionner l'image
    return robot_image

def effacer_ecran(fenetre):
    fenetre.fill(BLANC)

def rotation(robot,robot_image):
    rotated_robot = pygame.transform.rotate(robot_image,-robot.get_angle()-45)  # Utilisez l'angle du robot ici
    return rotated_robot

def dessine(robot,robot_image,fenetre,environnement):
        rotated_robot = rotation(robot,robot_image)
        rotated_rect = rotated_robot.get_rect(center=(round(robot.x), round(robot.y)))
        for obstacle in environnement.liste_object[1:]:
            pygame.draw.rect(fenetre, ROUGE, (round(obstacle.x), round(obstacle.y), obstacle.largeur, obstacle.hauteur))
        fenetre.blit(rotated_robot, rotated_rect.topleft)


def rafraichissement():
    return pygame.display.flip()

def tracer_trait_derriere_robot(robot, fenetre):
    """Trace un trait derrière le robot en utilisant ses positions précédentes."""
    positions = robot.get_precedente_positions()
    if len(positions) > 1:
        pygame.draw.lines(fenetre, ROUGE, False, positions, 2)

def interface(robot,environnement,fenetre,robot_image):
        # Efface l'écran
        effacer_ecran(fenetre)

        # Dessine le robot avec son image redimensionnée et tournée
        dessine(robot,robot_image,fenetre,environnement)
        # Tracer un trait derrière le robot
        tracer_trait_derriere_robot(robot, fenetre)
        # Met à jour l'affichage
        rafraichissement()


def evenement(run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Vérifie si la touche pressée est Echap
                pygame.quit()