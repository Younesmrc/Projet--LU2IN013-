
import pygame
from model.environnement import Environnement
from model.robot import Robot
from model.objet import Objet
from model.interface import *
from model.strategie.controleur import Controleur


# Initialisation de Pygame
pygame.init()

#AVEC INTERFACE GRAPHIQUE ?
graphique=True

# Définition des variables

BLANC = (255,255,255)
FPS = 30
ROUGE = (255, 0, 0)

# Paramètres de la fenêtre
largeur_env = 1000
hauteur_env = 1000
largeur_simu = 500
hauteur_simu = 500

# Définition de l'environnement
environnement = Environnement(largeur_env,hauteur_env)

# Définition du robot avec une image

x,y=150,150 #position de depart du robot
long,large=30,30 #set taille du robot
direction_x,direction_y=1,1 #direction de depart

robot = Robot(x,y,long,large,direction_x,direction_y,environnement,1.)

#DEFINITION VITESSE

robot.set_vitesse(2,1)


obstacle = Objet(350,350,50,50)
environnement.ajoute_object(robot)
environnement.ajout_obj_rand()
environnement.ajoute_object(obstacle)
liste_obstacles = environnement.liste_object[1:]

# Définition des actions et des variables 
if graphique :
    fenetre=creation_fenetre(largeur_simu,hauteur_simu)
    robot_image=donner_image_robot(robot)

controleur = Controleur(robot, environnement)
# Démarrer la stratégie
controleur.start()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            graphique=False
            pygame.quit()

    # Déplacement automatique du robot
    environnement.controle_positions()

    # Boucle de la stratégie
    if not controleur.stop():
        controleur.step()

    # Test de la détection d'un obstacle 
    robot.detection_obstacle(liste_obstacles)

    if graphique :
        # Efface l'écran
        effacer_ecran(fenetre)

        # Dessine le robot avec son image redimensionnée et tournée
        dessine(robot,obstacle,robot_image,fenetre,environnement)
        # Tracer un trait derrière le robot
        tracer_trait_derriere_robot(robot, fenetre)
        # Met à jour l'affichage
        rafraichissement()

        # Contrôle la vitesse de la boucle
        environnement.update(FPS)
        
    
    
    else :
        # Si l'interface graphique n'est pas activée,on effectue la simulation sans rien afficher
        environnement.update(FPS)
    