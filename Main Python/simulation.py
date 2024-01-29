import pygame
from Environnement.environnement import Environnement
from Robot.robot import Robot

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
BLANC = (255,255,255)
FPS = 30

# Paramètres de la fenêtre
largeur_fenetre = 400
hauteur_fenetre = 400

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Déplacement automatique du carré")

# Définition du robot avec une image
robot_image = pygame.image.load("1.png")
robot_image = pygame.transform.scale(robot_image,(25,25))  # Redimensionner l'image
robot = Robot(50,50,25,25,1,1)

# Définition de l'environnement
environnement = Environnement(400,400,fenetre)

# Définition de l'action
pas=10
i=0

def action(robot):
    global i
    if i == 0:
        if robot.avancer_vers(100,100):
            i += 1
    if i == 1:
        if robot.avancer_vers(150,100):
            i += 1
    if i == 2:
        if robot.avancer_vers(150,150):
            i += 1
    if i == 3:
        if robot.avancer_vers(100,150):
            i = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Déplacement automatique du robot
    action(robot)

    # Efface l'écran
    environnement.fenetre.fill(BLANC)

    # Rotation de l'image du robot
    rotated_robot = pygame.transform.rotate(robot_image,45)  # Utilisez l'angle du robot ici

    # Dessine le robot avec son image redimensionnée et tournée
    rotated_rect = rotated_robot.get_rect(center=(round(robot.x), round(robot.y)))
    environnement.fenetre.blit(rotated_robot, rotated_rect.topleft)

    # Met à jour l'affichage
    pygame.display.flip()

    # Contrôle la vitesse de la boucle
    pygame.time.Clock().tick(FPS)
