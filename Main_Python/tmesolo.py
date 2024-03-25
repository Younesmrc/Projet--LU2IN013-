from model.simulation import run_simulation
from model.constante import *
from model.strategie.strategies import *
from model.strategie.controleur import Controleur
from model.objet import *

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
avancer = Avancer(robot,environnement,100)
tournerdroite = Tourner_D(robot,environnement,90)
fairecarre = Sequentiel(robot,environnement)
fairecarre.strats = [avancer,tournerdroite]*4
foncemur = FonceMur(robot,environnement,1)



def q1_1():
    controleur = Controleur()
    controleur.add_strategie(fairecarre)
    environnement.ajoute_object(robot)
    obstacle = Objet(350,350,30,30)
    environnement.ajoute_object(obstacle)
    obstacle = Objet(50,50,30,30)
    environnement.ajoute_object(obstacle)
    obstacle = Objet(350,50,30,30)
    environnement.ajoute_object(obstacle)
    obstacle = Objet(30,350,30,30)
    environnement.ajoute_object(obstacle)
    obstacle = Objet(200,30,30,30)
    environnement.ajoute_object(obstacle)
    run_simulation(controleur,graphique,robot)


def q1_3():
    controleur = Controleur()
    controleur.add_strategie(fairecarre)
    environnement.ajoute_object(robot)
    robot.dessine(False)
    run_simulation(controleur,graphique,robot)

def q1_4():
    motif = Motif(robot,environnement,10)
    controleur = Controleur()
    controleur.add_strategie(motif)
    environnement.ajoute_object(robot)
    run_simulation(controleur,graphique,robot)


def q2_1():
    avancer = Avancer(robot,environnement,100)
    controleur = Controleur()
    controleur.add_strategie(avancer)
    environnement.ajoute_object(robot)
    obstacle = Ballon(200,150,30,30,0,0,0)
    environnement.ajoute_object(obstacle)
    run_simulation(controleur,graphique,robot)


def q2_3():
    environnement.ajoute_object(robot)
    ballon = Ballon(200,200,30,30,0,0,0)
    environnement.ajoute_object(ballon)
    avancer = CogneBallon(robot,ballon,environnement)
    controleur = Controleur()
    controleur.add_strategie(avancer)
    run_simulation(controleur,graphique,robot)

q2_3()