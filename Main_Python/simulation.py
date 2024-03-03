import pygame
from model.environnement import Environnement
from model.robot import Robot
from model.objet import Objet
from model.interface import *
from model.strategie.strats import Avancer
from model.strategie.faire_carre import FaireCarre
from model.strategie.faire_rond import TracerRond
from model.strategie.fonce_mur import FonceMur

def run_simulation(FPS,graphique,largeur_env,hauteur_env,largeur_simu,hauteur_simu,x,y,long,large,direction_x,direction_y,rayon, vitesse_lineaire,vitesse_angulaire):

    # Définition de l'environnement
    environnement = Environnement(largeur_env,hauteur_env)

    # Definition du robot
    robot = Robot(x,y,long,large,direction_x,direction_y,environnement,1.)

    # Definition controleur
    controleur1 = FaireCarre(robot,environnement,100,'D')
    controleur2 = FonceMur(robot,environnement)
    controleur3 = TracerRond(robot,environnement,rayon,vitesse_lineaire, vitesse_angulaire)

    # Definition obstacle
    obstacle = Objet(350,350,50,50)
    environnement.ajoute_object(robot)
    environnement.ajout_obj_rand()
    environnement.ajoute_object(obstacle)
    liste_obstacles = environnement.liste_object[1:] #ajout de tout sauf le robot

    if graphique :
        pygame.init()
        fenetre=creation_fenetre(largeur_simu,hauteur_simu)
        robot_image=donner_image_robot(robot)


    # Démarrer la stratégie
    controleur1.start()

    while True:
        #si le robot a fait une collision avec les bordures ont arretes
        if not environnement.controle_positions():
            # stratégie
            if not controleur1.stop():
                #si le robot a fait une collision avec un objects ont arretes
                if not environnement.controle_collisions():
                    robot.update_position()
                    controleur1.step()


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
        