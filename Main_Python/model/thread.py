import time
import threading
from .constante import *
from .interface import *
from .simulation import *

# Drapeau pour indiquer aux autres threads qu'ils doivent se terminer
thread_stop_flag = threading.Event()

def run_controler(controleur, environnement):
    controleur.start()
    while not thread_stop_flag.is_set():
        if not controleur.stop():
            if not environnement.controle_collisions():
                controleur.step()
        else:
            break
        time.sleep(1/FPS)

def run_env(environnement):
    while not thread_stop_flag.is_set():
        if not environnement.controle_positions():
            if not environnement.controle_collisions():
                environnement.update(FPS)

def run_interface(robot, environnement, obstacle, fenetre, robot_image):
    while not thread_stop_flag.is_set():
        if graphique:
            evenement()
            interface(robot, environnement, obstacle, fenetre, robot_image)
            print(robot.x)
            time.sleep(1/FPS)

def run(environnement, robot,controleur):
    global thread_stop_flag  # Définissez le drapeau comme global

    thread_stop_flag.clear()  # Assurez-vous qu'il est effacé avant de démarrer les threads

    thread_controler = threading.Thread(target=run_controler, args=(controleur, environnement))
    thread_env = threading.Thread(target=run_env, args=(environnement,))
    if graphique:
        thread_interface = threading.Thread(target=run_interface, args=(robot, environnement, obstacle, fenetre, robot_image))

    thread_controler.start()
    thread_env.start()
    thread_interface.start()

    # Attendez que le contrôleur se termine
    thread_controler.join()

    # Une fois le contrôleur terminé, activez le drapeau pour indiquer aux autres threads qu'ils doivent se terminer
    thread_stop_flag.set()

    # Attendez que les autres threads se terminent
    thread_env.join()
    if graphique:
        thread_interface.join()
