from Main_Python.model.constante import *
from Main_Python.model.obstacle import Obstacle
from Main_Python.controller.strategies import Avancer,Tourner_D,FonceMur,Tourner_G,Sequentiel,Boucle
from Main_Python.controller.controleur import Controleur
from Main_Python.irl.robotadaptateur import RobotAdaptateur
from Main_Python.model.simulation import Simulation
from Main_Python.model.reel import Reel
from Main_Python.model.environnement import Environnement
from Main_Python.model.robot import Robot
try :
    from robot2IN013 import Robot2IN013
except ImportError:
    from Main_Python.irl.mockup import Robot2I013Mockup
	
#test
graphique=True
environnement = Environnement(LARGEUR_ENVIRONNEMENT,HAUTEUR_ENVIRONNEMENT)
robot_version = 2 # 1 : simulation 2 : robot reel autre : robot mockup

if robot_version == 1:
    robot = Robot(ROBOT_X, ROBOT_Y, ROBOT_LONGUEUR, ROBOT_LARGEUR, DIRECTION_X, DIRECTION_Y, environnement, ROBOT_RAYON)
elif robot_version == 2: 
    graphique=False     
    robot_reel = Robot2IN013()
    robot = RobotAdaptateur(robot_reel, ROBOT_X, ROBOT_Y, DIRECTION_X, DIRECTION_Y,environnement)
else :
     graphique=False
     robot_mockup = Robot2I013Mockup()
     robot = RobotAdaptateur(robot_mockup,ROBOT_X, ROBOT_Y, DIRECTION_X, DIRECTION_Y,environnement)

#ajout robot et obstacle
environnement.robot = robot
environnement.ajoute_object(robot) #ajout en premier dans la liste
obstacle = Obstacle(350, 350, 50, 50)
environnement.ajoute_object(obstacle)

#

#definition controleur
controleur = Controleur()
avancer=Avancer(robot,environnement,300)
controleur.add_strategie(avancer)



simulation = Simulation(controleur,robot,environnement,graphique)
reel = Reel(controleur,robot)

if robot_version == 1 :
    simulation.run_simulation()
else :
    reel.run_reel()