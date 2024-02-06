
import pygame
from model.environnement import Environnement
from model.robot import Robot

# Initialisation de Pygame
pygame.init()

#AVEC INTERFACE GRAPHIQUE ?
graphique="oui"

# Définition des variables
BLANC = (255,255,255)
FPS = 30
VITESSE = 5
ROUGE = (255, 0, 0)

# Paramètres de la fenêtre
largeur_fenetre = 400
hauteur_fenetre = 400

# Définition de l'environnement
environnement = Environnement(largeur_fenetre,hauteur_fenetre)

# Définition du robot avec une image

x,y=50,50 #position de depart du robot
long,large=30,30 #set taille du robot
direction_x,direction_y=1,1 #direction de depart

robot = Robot(x,y,long,large,direction_x,direction_y,environnement,1.)
robot2 = Robot(350,350,50,50,direction_x,direction_y,environnement,1.)
environnement.ajoute_object(robot)
environnement.ajoute_object(robot2)

if graphique == "oui":
    # Création de la fenêtre
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Simulation robot")

    # Donne une image au robot
    robot_image = pygame.image.load("robot2.png")
    robot_image = pygame.transform.scale(robot_image,(long*2,large*2))  # Redimensionner l'image

# Définition des actions et des variables 

teta=0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            graphique="non"
            pygame.quit()

    # Déplacement automatique du robot
    robot.avancer(100,VITESSE)
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
        pygame.time.Clock().tick(FPS)
    
    else :
        # Si l'interface graphique n'est pas activée,on effectue la simulation sans rien afficher
        action_a_faire=action(robot,pas,action_a_faire)
        pygame.time.Clock().tick(FPS)