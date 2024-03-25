from model.simulation import run_simulation
from model.constante import *
from model.strategie.strategies import *
from model.strategie.controleur import Controleur

# On détermine quel robot on utilise (1 => robot simulé / 2 => robot réel)
robot_version = 1 

if robot_version == 1:
    robot = Robot(robot_x,robot_y,robot_longueur,robot_largeur,direction_x,direction_y,environnement,1.)
    graphique = True # True pour ouvrir la fenetre false sinon

elif robot_version == 2:
    graphique = False # True pour ouvrir la fenetre false sinon
    from model.irl.mockup import Robot2I013Mockup
    from model.irl.robotadaptateur import RobotAdaptateur
    from model.irl.RobotReel import Robot2IN013
    
    robot_reel = Robot2IN013()
    robot = RobotAdaptateur(robot_reel,robot_x,robot_y,direction_x,direction_y,environnement)

else:
    print("Version de robot non prise en charge")
    exit(1)


# Definition des strategies
avancer = Avancer(robot,environnement,float('inf'))
tournerdroite = Tourner_D(robot,environnement,90)
avancer_tourner = Sequentiel(robot,environnement)
avancer_tourner.strats = [avancer,tournerdroite]*5

controleur = Controleur()
controleur.add_strategie(avancer_tourner)


run_simulation(controleur,graphique,robot)