import pygame
from .environnement import Environnement
from .robot import Robot
from .objet import Objet
from .interface import *
from .strategie.strategies import *
from .strategie.controleur import *
import threading



def run_simulation(FPS,graphique,largeur_env,hauteur_env,largeur_simu,hauteur_simu,x,y,long,large,direction_x,direction_y,deltat,version_robot):

    # Définition de l'environnement
    environnement = Environnement(largeur_env,hauteur_env,deltat)
    

    # Definition du robot
    if version_robot == 1:
        robot = Robot(x,y,long,large,direction_x,direction_y,environnement,1.)
        if graphique :
            pygame.init()
            fenetre=creation_fenetre(largeur_simu,hauteur_simu)
            robot_image=donner_image_robot(robot)  
    elif version_robot == 2:
        from .irl.mockup import Robot2I013Mockup
        from .irl.robotadaptateur import RobotAdaptateur
        from .irl.RobotReel import Robot2IN013
        
        robot_reel = Robot2IN013()
        robot = RobotAdaptateur(robot_reel,x,y,direction_x,direction_y,environnement)
    
    else:
        raise ImportError("Version de robot non prise en charge")

    
    #ajout du robot dans l'environnement
    environnement.robot=robot
    environnement.ajoute_object(robot)
    
    # Definition des strategies
    avancer = Avancer(robot,environnement,10000)
    tournerdroite = Tourner_D(robot,environnement,90)
    fairecarre = Sequentiel(robot,environnement)
    fairecarre.strats = [avancer,tournerdroite]*4
    foncemur = FonceMur(robot,environnement,100)

    #Definition du controleur
    controleur = Controleur()
    controleur.add_strategie(foncemur)

    # Definition obstacle
    obstacle = Objet(350,350,50,50)
    #environnement.ajout_obj_rand()
    environnement.ajoute_object(obstacle)

    # Démarrer la stratégie
    controleur.start()

    #Permet de contrôler le programme 
    running = True
    
    while running:
        #si le robot a fait une collision avec les bordures ont arretes
        if not environnement.controle_positions():
            # stratégie
            if not controleur.stop():
                #si le robot a fait une collision avec un objects ont arretes
                if not environnement.controle_collisions():
                    environnement.update(FPS)
                    controleur.step()


        if graphique :
            # Recherche evenement pygame    
            evenement()
            # Affichage dessin etc...
            interface(robot,environnement,obstacle,fenetre,robot_image)

        