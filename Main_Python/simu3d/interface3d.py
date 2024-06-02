from ursina import *
from ursina import Entity
from ursina import EditorCamera
from Main_Python.controller.controleur import Controleur
from Main_Python.controller.strategies import *
from Main_Python.model.environnement import Environnement
from Main_Python.model.robot import Robot
from Main_Python.model.constante import *
import time
import threading
import math

app = Ursina()

environnement = Environnement(LARGEUR_ENVIRONNEMENT,HAUTEUR_ENVIRONNEMENT)
r = Robot(ROBOT_X, ROBOT_Y, ROBOT_LONGUEUR, ROBOT_LARGEUR, DIRECTION_X, DIRECTION_Y, environnement, ROBOT_RAYON)
environnement.robot = r

xpos = 9
zpos = 3
direction_x = 0.5
direction_z = -0.5

modele_rob = 'robotv4.stl'
balise_layer = 'balise.jpg'
robot = Entity(model=modele_rob, color=color.blue, position=(xpos,0,zpos),scale = 0.05,rotation_x = 90)
text1 = Text(text="Fleche haut = Zoom in\nFleche bas = Zoom out\n1= camera Pov\n2 = camera Top", position=(-0.6, 0.4), scale=2, enabled=False, color = color.red)
text2 = Text(text="POV CAM", position=(0.6, 0.45), scale=2,color = color.black, enabled=False)
viseur_pov = Text(text="+",position = (-0.04,0.05),color = color.black,scale = (5,5,5))
arene = Entity(model= 'plane',texture= 'grille.jfif',collider= 'mesh',scale= (1000,1,1000),position = (0,-5,0))
balise = Entity(model= 'cube',texture = balise_layer, position = (100,0,100),scale =(20,20,20))
Sky()
       
pov = 0

def change_camera(bouton):
    global text1,pov

    if bouton == "1" or bouton == '&':
        #Si l'utilisateur veut que la caméra soit en mode POV
        camera.position = (robot.x,0.1,robot.z)
        camera.rotation = (0,robot.rotation_z)
        text1.enabled = False
        text2.enabled = True
        viseur_pov.enabled = True
        camera.fov = 60
        pov = 1

    if bouton == "2" or bouton == "é":
        #Si l'utilisateur veut que la caméra soit en mode TOP
        camera.position = (robot.x,200,robot.z)
        camera.rotation = (90,90,0)
        camera.fov = 60
        text1.enabled = False
        text2.enabled = False
        viseur_pov.enabled = False
        pov = 0

    if bouton == "c":
        #Si l'utilisateur veut que la caméra soit en mode LIBRE
        camera2 = EditorCamera()
        camera.world_parent = camera2
        camera.position = (-100,100,-100)
        pov = 5

    if bouton == "0" or bouton == "à":
        #Si l'utilisateur veut que la caméra soit en mode MENU
        camera.position = (0,50,30)
        text1.enabled = True
        text2.enabled = False
        viseur_pov.enabled = False
        camera.fov = 120
        pov = 3

change_camera("0")


def tracé_robot(x,z):
    return Entity(model='cube', position=(x, -3, z), color=color.red,scale = (0.5,0.5,0.5))


def update():
    global direction_x, direction_z,r,robot

    robot.x = r.x
    robot.z = r.y
    print("x : "+str(robot.x)+",y :"+str(robot.z))
    if direction_x == 1 and direction_z == 0:
        robot.rotation_y = 0
    else:
        angle = math.atan2(r.direction_x, r.direction_y)
        angle_degrees = math.degrees(angle) - 90
        robot.rotation_y = angle_degrees

    # Gérer le changement de caméraS
    if held_keys['1'] or held_keys['&']:
        change_camera("1")
    if held_keys['2'] or held_keys['é']:
        change_camera("2")
    if held_keys['à'] or held_keys['0']:
        change_camera("0")
    if held_keys['c']:
        change_camera("c")
    if held_keys['s']:
        base.win.save_screenshot("screenshot.png")
        
    if held_keys['down arrow']:
        if pov == 1:
            camera.fov += 1
        if pov == 0:
            camera.y+=2
            camera.position = (camera.x,camera.y,camera.z)
    if held_keys['up arrow']:
        if pov == 1:
            camera.fov -= 1
        if pov == 0:
            camera.y-= 2
            camera.position = (camera.x,camera.y,camera.z)

    if pov == 1:
        camera.position = robot.position
        camera.rotation_y = robot.rotation_y + 90
    if pov == 0:
        camera.position = (robot.x,camera.y,robot.z)

    tracé_robot(robot.x,robot.z)


def run_controleur_3d(controleur,environnement):
    """
    boucle du controleur
    """
    controleur.start()
    while not controleur.stop():
        if not environnement.controle_collisions():
            controleur.step()
        time.sleep(1 / FPS_CONTROLEUR)



def run_environnement_3d(environnement):
    """
    Boucle de l'environnement
    """
    while True:
        if not environnement.controle_positions():
            if not environnement.controle_collisions():
                environnement.update(FPS_ENVIRONNEMENT)
