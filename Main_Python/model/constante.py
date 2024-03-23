FPS = 100

# On détermine quel robot on utilise (1 => robot simulé / 2 => robot réel)
robot_version = 1 

if robot_version == 1:
    graphique = True # True pour ouvrir la fenetre false sinon

elif robot_version == 2:
    graphique = False # True pour ouvrir la fenetre false sinon

else:
    print("Version de robot non prise en charge")


# Vitesse des updates du robot :
deltat=2

# Taille de l'environnement
largeur_environnement = 500
hauteur_environnement = 500

# Taille de la fenetre de simulation
largeur_simu = 500
hauteur_simu = 500

# Definition variables du robot

robot_x,robot_y = (150,150)  
robot_longueur,robot_largeur = (30,30) 
direction_x,direction_y = (1,1)