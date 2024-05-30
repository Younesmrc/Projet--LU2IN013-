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
from Main_Python.simu3d.interface3d import *


environnement.robot = r
controleur = Controleur()
avancer=Avancer(r,environnement,100)
tourner = Tourner_reel(r,90,True)
faire_carrer = Sequentiel()
faire_carrer.strategies=[avancer,tourner]*4+[avancer]+[avancer,tourner]*4
controleur.add_strategie(faire_carrer)

thread_controler = threading.Thread(target=run_controleur_3d, args=(controleur,environnement))
thread_env = threading.Thread(target=run_environnement_3d, args=(environnement,))
thread_env.start()
time.sleep(3)
thread_controler.start()
app.run()
