from Main_Python.model.reel import *
from Main_Python.model.simulation import *
from Main_Python.controller import *
try :
    from Main_Python.irl.RobotReel import Robot2IN013
except ImportError:
    from Main_Python.irl.mockup import Robot2I013Mockup
	
#test
graphique=True
environnement = Environnement(LARGEUR_ENVIRONNEMENT,HAUTEUR_ENVIRONNEMENT)
robot_version = 1 # 1 : simulation 2 : robot reel autre : robot mockup

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
avancer=Avancer(robot,environnement,100)
tourner = Tourner_D(robot,environnement,90)
faire_carrer = Sequentiel()
faire_carrer.strategies=[avancer,tourner]*4
controleur.add_strategie(faire_carrer)



simulation = Simulation(controleur,robot,environnement,graphique)
reel = Reel(controleur,robot)

if robot_version == 1 :
    simulation.run_simulation()
else :
    reel.run_reel()