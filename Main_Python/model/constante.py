from model.environnement import Environnement

FPS = 60

# Vitesse des updates du robot :
deltat=2

# Taille de l'environnement
largeur_environnement = 500
hauteur_environnement = 500

# Taille de la fenetre de simulation
largeur_simu = 500
hauteur_simu = 500

# Definition variables du robot

robot_x,robot_y = (200,200)  
robot_longueur,robot_largeur = (30,30) 
direction_x,direction_y = (0,-1)


# Définition de l'environnement
environnement = Environnement(largeur_environnement,hauteur_environnement,deltat)
