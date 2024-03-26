from model.thread import *
from model.objet import Objet
from model.strategie.strategies import *
from model.strategie.controleur import Controleur
from model.irl.robotadaptateur import RobotAdaptateur
try :
    from model.irl.RobotReel import Robot2IN013
except :
    from model.irl.mockup import Robot2I013Mockup
	


environnement = Environnement(largeur_environnement, hauteur_environnement, deltat)
robot_version = 1

if robot_version == 1:
    robot = Robot(robot_x, robot_y, robot_longueur, robot_largeur, direction_x, direction_y,environnement,robot_rayon)
elif robot_version == 2:      
    robot_reel = Robot2IN013()
    robot = RobotAdaptateur(robot_reel,robot_x,robot_y, direction_x, direction_y,environnement)
else :
     robot_mockup = Robot2I013Mockup()
     robot = RobotAdaptateur(robot_mockup,robot_x,robot_y, direction_x, direction_y,environnement)

#ajout robot et obstacle
environnement.robot = robot
obstacle = Objet(350, 350, 50, 50)
environnement.ajoute_object(robot) #ajout en premier dans la liste
environnement.ajoute_object(obstacle)

#definition controleur
controleur = Controleur()
faire_carre= Sequentiel(robot,environnement)
faire_carre.strategies=[Avancer(robot,environnement,100),Tourner_D(robot,environnement,90)]*4
controleur.add_strategie(faire_carre)

run(environnement,robot,controleur)

