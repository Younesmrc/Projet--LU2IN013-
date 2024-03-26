import time
import threading
from .constante import *
from .interface import *



def run_controler(controleur, environnement):
    controleur.start()
    while running:
        if not controleur.stop():
            if not environnement.controle_collisions():
                controleur.step()
        else:
            break
        time.sleep(1/FPS)

def run_env(environnement):
    while running:
        if not environnement.controle_positions():
            if not environnement.controle_collisions():
                environnement.update(FPS)

def run_interface(robot, environnement, fenetre, robot_image):
    while running:
        if graphique:
            evenement()
            interface(robot, environnement, fenetre, robot_image)
            print(robot.x)
            time.sleep(1/FPS)

def run(environnement, robot,controleur):
    global running  # Définissez le drapeau comme global

    running=True

    thread_controler = threading.Thread(target=run_controler, args=(controleur, environnement))
    thread_env = threading.Thread(target=run_env, args=(environnement,))
    if graphique:
        pygame.init()
        fenetre = creation_fenetre(largeur_simu, hauteur_simu)
        robot_image = donner_image_robot(robot)
        thread_interface = threading.Thread(target=run_interface, args=(robot, environnement, fenetre, robot_image))
        thread_interface.start()

    thread_controler.start()
    thread_env.start()

    #thread_controler.join()
    #thread_env.join()
    #if graphique:
        #thread_interface.join()
