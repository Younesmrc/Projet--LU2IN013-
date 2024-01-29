import pygame
from Environnement.environnement import Environnement
from Robot.robot import Robot




# Initialisation de Pygame
pygame.init()

# Définition des couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
FPS = 30

# Paramètres de la fenêtre
largeur_fenetre = 400
hauteur_fenetre = 400

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Déplacement automatique du carré")

#definition robot
robot=Robot(50,50,25,50,1,1)

#definition environnement
environnement=Environnement(400,400,fenetre)

#definition action
  
pas=10
i=0
def action(robot):
     global i
     if i == 0 :
        if robot.avancer_vers(100,100) :
            i+=1
     if i == 1 :
        if robot.avancer_vers(150,100) :
            i+=1
     if i == 2 :
        if robot.avancer_vers(150,150) :
            i+=1
     if i == 3 :
        if robot.avancer_vers(100,150) :
            i=0



