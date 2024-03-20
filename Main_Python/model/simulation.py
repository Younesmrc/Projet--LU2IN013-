import pygame
from .environnement import Environnement
from .robot import Robot
from .objet import Objet
from .interface import *
from .strategie.strategies import *



def run_simulation(FPS,graphique,largeur_env,hauteur_env,largeur_simu,hauteur_simu,x,y,long,large,direction_x,direction_y,rayon, vitesse_lineaire,vitesse_angulaire,deltat,version_robot):

    # Définition de l'environnement
    environnement = Environnement(largeur_env,hauteur_env,deltat)
    
    if version_robot == 1:
        robot = Robot(x,y,long,large,direction_x,direction_y,environnement,1.)
    
    elif version_robot == 2:
        from .irl.mockup import Robot2I013Mockup
        from .irl.robotadaptateur import RobotAdaptateur
        from .irl.RobotReel import Robot2IN013
        
        robot_reel = Robot2IN013()
        robot = RobotAdaptateur(robot_reel,x,y,direction_x,direction_y,environnement)
    
    else:
        raise ImportError("Version de robot non prise en charge")



    
    #robot_mockup = Robot2I013Mockup()
    
    # Definition du robot
    environnement.robot=robot
    
    # Definition controleur
    controleur1 = FaireCarre(robot,environnement,100,'D')
    controleur2 = FonceMur(robot,environnement)

    CONTROLEUR_UTILISE = controleur1

    # Definition obstacle
    obstacle = Objet(350,350,50,50)
    environnement.ajoute_object(robot)
    #environnement.ajout_obj_rand()
    environnement.ajoute_object(obstacle)
    liste_obstacles = environnement.liste_object[1:] #ajout de tout sauf le robot

    if graphique :
        pygame.init()
        fenetre=creation_fenetre(largeur_simu,hauteur_simu)
        robot_image=donner_image_robot(robot)


    # Démarrer la stratégie
    CONTROLEUR_UTILISE.start()

    #Permet de contrôler le programme 
    running = True
    
    while running:
        #si le robot a fait une collision avec les bordures ont arretes
        if not environnement.controle_positions():
            # stratégie
            if not CONTROLEUR_UTILISE.stop():
                #si le robot a fait une collision avec un objects ont arretes
                if not environnement.controle_collisions():
                    environnement.update(FPS)
                    CONTROLEUR_UTILISE.step()


        if graphique :
            # Recherche evenement pygame    
            evenement()

            # Affichage dessin etc...
            interface(robot,environnement,obstacle,fenetre,robot_image)

        