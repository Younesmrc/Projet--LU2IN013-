
import pygame
from model.environnement import Environnement
from model.robot import Robot
from model.inter import *

# Initialisation de Pygame
pygame.init()

#AVEC INTERFACE GRAPHIQUE ?
graphique=True

# Définition des variables

VITESSE_MOTEUR_DROIT = 1
VITESSE_MOTEUR_GAUCHE = 2

BLANC = (255,255,255)
FPS = 30
ROUGE = (255, 0, 0)

# Paramètres de la fenêtre
largeur_fenetre = 400
hauteur_fenetre = 400

# Définition de l'environnement
environnement = Environnement(largeur_fenetre,hauteur_fenetre)

# Définition du robot avec une image

x,y=150,150 #position de depart du robot
long,large=30,30 #set taille du robot
direction_x,direction_y=1,1 #direction de depart

robot = Robot(x,y,long,large,direction_x,direction_y,environnement,1.)
robot2 = Robot(350,350,50,50,direction_x,direction_y,environnement,1.)
environnement.ajoute_object(robot)
environnement.ajoute_object(robot2)

# Définition des actions et des variables 
if graphique :
    fenetre=creation_fenetre(environnement)
    robot_image=donner_image_robot(robot)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            graphique="non"
            pygame.quit()

    # Déplacement automatique du robot
    robot.update_position(VITESSE_MOTEUR_GAUCHE,VITESSE_MOTEUR_DROIT)
    environnement.controle_positions()
    environnement.controle_collisions()

    if graphique == "oui":
        # Efface l'écran
        fenetre.fill(BLANC)

        # Rotation de l'image du robot
        rotated_robot = pygame.transform.rotate(robot_image,teta)  # Utilisez l'angle du robot ici

        # Dessine le robot avec son image redimensionnée et tournée
        rotated_rect = rotated_robot.get_rect(center=(round(robot.x), round(robot.y)))
        pygame.draw.rect(fenetre,ROUGE,(round(robot2.x), round(robot2.y),20,20))
        fenetre.blit(rotated_robot, rotated_rect.topleft)

        # Met à jour l'affichage
        pygame.display.flip()

        # Contrôle la vitesse de la boucle
        environnement.update(FPS)
    
    else :
        # Si l'interface graphique n'est pas activée,on effectue la simulation sans rien afficher
        environnement.update(FPS)
    