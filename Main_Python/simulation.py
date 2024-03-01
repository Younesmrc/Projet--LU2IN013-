import pygame
from model.environnement import Environnement
from model.robot import Robot
from model.objet import Objet
from model.interface import *
from model.strategie.controleur import FaireCarre

def run_simulation(FPS,graphique,largeur_env,hauteur_env,largeur_simu,hauteur_simu,x,y,long,large,direction_x,direction_y,distance):

    # Définition de l'environnement
    environnement = Environnement(largeur_env,hauteur_env)

    # Definition du robot
    robot = Robot(x,y,long,large,direction_x,direction_y,environnement,1.)

    # Definition controleur

    controleur = FaireCarre(robot,environnement,distance)


    # Definition obstacle
    obstacle = Objet(350,350,50,50)
    environnement.ajoute_object(robot)
    environnement.ajout_obj_rand()
    environnement.ajoute_object(obstacle)
    liste_obstacles = environnement.liste_object[1:]

    if graphique :
        pygame.init()
        fenetre=creation_fenetre(largeur_simu,hauteur_simu)
        robot_image=donner_image_robot(robot)


    # Démarrer la stratégie
    controleur.start()

    while True:

        environnement.controle_positions()
        # stratégie
        if not controleur.stop():
            robot.update_position()
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
        