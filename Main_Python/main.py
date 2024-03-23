import math
from model.simulation import *
import pygame
from model.thread import *
from model.simulation import *


controleur = Controleur()
#controleur.add_strategie(faire_carre)
controleur.add_strategie(fonce_mur)

run(environnement,robot,controleur)

