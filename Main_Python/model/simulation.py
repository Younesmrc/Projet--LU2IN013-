import pygame
from .environnement import Environnement
from .robot import Robot
from .objet import Objet
from .interface import *
from .strategie.strategies import *
from .strategie.controleur import *
from .constante import *



def run_simulation(controleur,graphique,robot):

    if graphique :
        pygame.init()
        fenetre=creation_fenetre(largeur_simu,hauteur_simu)
        robot_image=donner_image_robot(robot)  
    
    #ajout du robot dans l'environnement
    environnement.robot=robot
    environnement.ajoute_object(robot)

    # Definition obstacle
    obstacle = Objet(350,350,50,50)
    obj1= Objet(50,120,50,50)
    obj2= Objet(200,100,50,50)
    obj3= Objet(350,100,50,50)
    
    obj5= Objet(50,350,50,50)
    #environnement.ajout_obj_rand()

    environnement.ajoute_object(obj1)
    environnement.ajoute_object(obj2)
    environnement.ajoute_object(obj3)
    environnement.ajoute_object(obj5)
    environnement.ajoute_object(obstacle)
    robot.dessine=True


    #Definition du controleur
    controleur = controleur

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

        