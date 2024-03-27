from model.simulation import run_simulation
from model.constante import *
from model.objet import Objet
from model.strategie.strategies import *
from model.strategie.controleur import Controleur
from model.irl.robotadaptateur import RobotAdaptateur
try :
    from model.irl.RobotReel import Robot2IN013
except :
    from model.irl.mockup import Robot2I013Mockup
	

graphique=True
environnement = Environnement(largeur_environnement, hauteur_environnement)
robot_version = 3 # 1 : simulation 2 : robot reel autre : robot mockup

if robot_version == 1:
    robot = Robot(robot_x, robot_y, robot_longueur, robot_largeur, direction_x, direction_y,environnement,robot_rayon)
elif robot_version == 2: 
    graphique=False     
    robot_reel = Robot2IN013()
    robot = RobotAdaptateur(robot_reel,robot_x,robot_y, direction_x, direction_y,environnement)
else :
     graphique=False
     robot_mockup = Robot2I013Mockup()
     robot = RobotAdaptateur(robot_mockup,robot_x,robot_y, direction_x, direction_y,environnement)

#ajout robot et obstacle
environnement.robot = robot
obstacle = Objet(350, 350, 50, 50)
environnement.ajoute_object(robot) #ajout en premier dans la liste
environnement.ajoute_object(obstacle)

#definition controleur
controleur = Controleur()
faire_carre= Sequentiel()
faire_carre.strategies=[Avancer(robot,environnement,100),Tourner_D(robot,environnement,90)]*4
avancer=Avancer(robot,environnement,float("inf"))
controleur.add_strategie(avancer)

run_simulation(environnement,robot,controleur,graphique)