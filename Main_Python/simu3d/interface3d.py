from ursina import *
from ursina import Entity
import time
import threading
import math

app = Ursina()


FPS_INTERFACE = 60
FPS_CONTROLEUR = 30
FPS_ENVIRONNEMENT = 100

BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)
NOIR = (0, 0, 0)

# Taille de l'environnement
LARGEUR_ENVIRONNEMENT = 500
HAUTEUR_ENVIRONNEMENT = 500

# Taille de la fenetre de simulation
LARGEUR_SIMU = 500
HAUTEUR_SIMU = 500

# Definition variables du robot

ROBOT_X, ROBOT_Y = (150, 150)  
ROBOT_LONGUEUR, ROBOT_LARGEUR = (30, 30) 
DIRECTION_X, DIRECTION_Y = (1, 1)
ROBOT_RAYON = 1.0

class Controleur():
    """
        La classe de controleur : Le controleur sert à gerer les strategies du robot
        * Il sert à sélectionner la startegie à executer

        La structure : 
        C'est un conteneur de strategies

        A chaque appel à sa methode step il test si la startegie courrante est non terminée si c'est le cas il la lance

    """

    def __init__(self):
        # La liste des startegies
        self.strategies = []

        # La startegie courrante
        self.current_strat = -1

    def add_strategie(self, strategie):
        """
        Startegie -> None
        Permer d'ajouter une startegie à la liste
        """
        self.strategies.append(strategie)

    def select_strategie(self, index):
        """
        int -> None
        Pemer de sélectionner une startegie à executer parmis toutes les startegies sauvegardées
        """
        if index < 0 or index > len(self.strategies):
            return

        self.strategies[self.current_strat].start()
        self.current_strat = index
    
    def start(self):
        """ Initialise le contrôleur en réinitialisant l'indice de stratégie courant."""
        self.cur = -1

    def step(self):
        """ Exécute une étape de la stratégie en cours ou passe à la suivante si nécessaire."""
        if self.stop():
            return
        
        if self.cur < 0 or self.strategies[self.cur].stop():
            self.cur += 1
            self.strategies[self.cur].start()
            self.strategies[self.cur].step()
        
        elif self.cur < len(self.strategies):
            self.strategies[self.cur].step()

    def stop(self):
        """ Vérifie si l'exécution des stratégies est terminée."""
        return self.cur == len(self.strategies) - 1 and self.strategies[self.cur].stop()   
    
class Avancer:
    """
    Représente une action pour faire avancer un robot dans un environnement donné.

    Attributs:
        distance (float): La distance totale à parcourir.
        robot (Robot): L'objet robot à contrôler.
        environnement: L'environnement dans lequel le robot opère.

    Méthodes:
        start(): Initialise la distance parcourue par le robot.
        step(): Déplace le robot vers l'avant d'un petit pas.
        stop(): Vérifie si le robot a parcouru la distance spécifiée.

    """
    def __init__(self, robot, environnement, distance):
        self.distance = distance
        self.robot = robot
        self.environnement = environnement

    def start(self):
        """Initialise la distance parcourue."""
        self.robot.set_vitesse(30, 30) 
        self.robot.reset_distance()

    def step(self):
        """Déplace le robot vers l'avant d'un petit pas."""

        self.robot.update_distance()
        self.robot.reset()

        if self.stop():
            return
        
        self.robot.set_vitesse(30, 30) 
       

    def stop(self):
        """Vérifie si le robot a parcouru la distance spécifiée."""
        if self.robot.get_distance() > self.distance :
            self.robot.reset_distance()
            return True
        return False
    
class Tourner_D:
    """
    Classe représentant une action pour faire tourner un robot vers la droite dans un environnement donné.

    Attributs:
        robot (Robot): L'objet robot à contrôler.
        environnement: L'environnement dans lequel le robot opère.
        angle (float): L'angle de rotation à effectuer en degrés.
        cur (int): Compteur courant du nombre de step effectué
        angle_vise(float): Angle voulu par le robot par rapport à son angle de départ

    Méthodes:
        start(): Initialise l'angle parcouru par le robot.
        step(): Effectue un petit pas de rotation vers la droite.
        stop(): Vérifie si l'angle de rotation spécifié est atteint.

    """
    
    def __init__(self, robot, environnement, angle):
        self.angle = angle
        self.robot = robot
        self.environnement = environnement
        self.cur = 0
        self.angle_vise = 0
        self.angle_parcouru = 0
        
    def start(self):
        """ Initialise l'angle parcouru par le robot."""
        self.cur = 0 # Initialisation du compteur à 0
        self.robot.set_vitesse(-1, 1)  # Rotation vers la droite
        self.angle_vise = (self.robot.get_angle() + self.angle) % 360 # Calcul de l'angle final


    def step(self):
        """ Effectue un petit pas de rotation vers la droite."""

        self.robot.update_distance()
        self.angle_parcouru += self.robot.angle_parcouru
        self.robot.reset()
        # Calcul de l'angle restant par rapport à l'angle réel du robot
        angle_restant = (self.angle_vise - self.robot.get_angle()) % 360
        # Calcul de la vitesse angulaire en fonction du nombre de step
        if self.cur != 0:
            vitesse_angulaire = (self.angle - angle_restant) / self.cur
        else:
            vitesse_angulaire = 0
        # Si l'angle restant à parcourir est plus petit que le pas de rotation, on ajuste le pas
        if vitesse_angulaire > angle_restant :
            self.robot.set_vitesse(-0.05, 0.05)

        # Augmentation du compteur
        self.cur += 1
        
    def stop(self):
        """ Vérifie si l'angle de rotation spécifié est atteint."""
        return self.robot.condition_angle(self.angle_vise)


class Tourner_G:
    """
    Classe représentant une action pour faire tourner un robot vers la gauche dans un environnement donné.

    Attributs:
        robot (Robot): L'objet robot à contrôler.
        environnement: L'environnement dans lequel le robot opère.
        angle (float): L'angle de rotation à effectuer en degrés.
        cur (int): Compteur courant du nombre de step effectué
        angle_vise(float): Angle voulu par le robot par rapport à son angle de départ

    Méthodes:
        start(): Initialise l'angle parcouru par le robot.
        step(): Effectue un petit pas de rotation vers la gauche.
        stop(): Vérifie si l'angle de rotation spécifié est atteint.

    """
    
    def __init__(self, robot, environnement, angle):
        self.angle = angle
        self.robot = robot
        self.environnement = environnement
        self.cur = 0
        self.angle_vise = 0
        self.angle_parcouru = 0
        
    def start(self):
        """ Initialise l'angle parcouru par le robot."""
        self.cur = 0 # Initialisation du compteur à 0
        self.robot.set_vitesse(1, -1)  # Rotation vers la gauche
        self.angle_vise = (self.robot.get_angle() - self.angle) % 360 # Calcul de l'angle final
        print("Angle visé au début de la rotation ",self.angle_vise)

    def step(self):
        """ Effectue un petit pas de rotation vers la gauche."""
        self.robot.update_distance()
        self.angle_parcouru += self.robot.angle_parcouru
        self.robot.reset()
        # Calcul de l'angle restant par rapport à l'angle réel du robot
        angle_restant = (self.robot.get_angle() - self.angle_vise) % 360

        # Calcul de la vitesse angulaire en fonction du nombre de step
        if self.cur != 0:
            vitesse_angulaire = ((self.angle - angle_restant) / self.cur)
        else:
            vitesse_angulaire = 0

        # Si l'angle restant à parcourir est plus petit que le pas de rotation, on ajuste le pas
        if vitesse_angulaire > angle_restant :
            self.robot.set_vitesse(0.05, -0.05)

        # Augmentation du compteur
        self.cur += 1
        
    def stop(self):
        """ Vérifie si l'angle de rotation spécifié est atteint."""
        return self.robot.condition_angle(self.angle_vise)
    
class Sequentiel:
    """
    Classe représentant un contrôleur pour orchestrer les actions d'un robot dans un environnement donné.

    Attributs:
        robot (Robot): L'objet robot à contrôler.
        environnement: L'environnement dans lequel le robot opère.
        distance (float): La distance maximale à parcourir.
        tourner (str): Le sens dans lequel le robot doit tourner ("D" pour droite, "G" pour gauche).

    Méthodes:
        start(): Initialise le contrôleur.
        step(): Exécute une étape de la stratégie en cours.
        stop(): Vérifie si l'exécution des stratégies est terminée.

    """
    def __init__(self):
        # La liste des startegies
        self.strategies = []

        # La startegie courrante
        self.current_strat = -1
    
    def start(self):
        """ Initialise le contrôleur en réinitialisant l'indice de stratégie courant."""
        self.cur = -1

    def step(self):
        """ Exécute une étape de la stratégie en cours ou passe à la suivante si nécessaire."""
        if self.stop():
            return
        
        if self.cur < 0 or self.strategies[self.cur].stop():
            self.cur += 1
            self.strategies[self.cur].start()
            self.strategies[self.cur].step()
        
        elif self.cur < len(self.strategies):
            self.strategies[self.cur].step()

    def stop(self):
        """ Vérifie si l'exécution des stratégies est terminée."""
        return self.cur == len(self.strategies) - 1 and self.strategies[self.cur].stop()   


class Robot:
    """Classe Robot répertoriant les fonctionnalités permettant de simuler un robot

    Attributs:
        :x (float): La coordonnée x actuelle du robot.
        :y (float): La coordonnée y actuelle du robot.
        :largeur (float): La largeur du robot.
        :hauteur (float): La hauteur du robot.
        :direction_x (float): La composante x du vecteur de direction du robot.
        :direction_y (float): La composante y du vecteur de direction du robot.
        :environnement (Environnement): L'environnement dans lequel le robot évolue.
        :rayon_roue (float): Le rayon des ses roues.

    Methodes:
        __init__(self, x, y, largeur, hauteur, direction_x, direction_y, environnement, rayon_roue):
            Initialise un obstacle Robot avec les coordonnées, la taille, la direction, l'environnement et le rayon des roues spécifiés.

        __str__(self):
            Renvoie une représentation sous forme de chaîne de la position actuelle du robot.

        update_position(self, vitesse_gauche, vitesse_droite):
            Déplace le robot en fonction des vitesses spécifiées pour les roues gauche et droite.

        get_angle(self):
            Renvoie l'angle en degrés du robot dans le plan où 0 degré pointe vers la droite.

        get_precedente_positions(self):
            Renvoie les positions précédentes du robot.

        detection_obstacle(self, obstacle):
            Vérifie s'il y a un obstacle devant le robot, renvoie la distance à laquelle se situe l'objet ou None sinon.
    """

    def __init__(self, x, y, largeur, hauteur, direction_x, direction_y, environnement, rayon_roue, vitesse_droite=1, vitesse_gauche=1):
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.environnement = environnement
        # Créer les roues avec un rayon de rRoue
        self.rayon_roue = rayon_roue
        self.vitesse_droite=vitesse_droite
        self.vitesse_gauche = vitesse_gauche

        self.angle_parcouru = 0
        self.distance_parcouru = 0

        self.positions_precedentes = []
        


    def __str__(self):
        return "(" + str(round(self.x, 2)) + "," + str(round(self.y, 2)) + ")"

    def update_position(self,deltat=1):
        """Déplace le robot en fonction des vitesses spécifiées pour les roues gauche et droite.

        Args:
            vitesse_gauche (float): Vitesse de la roue gauche.
            vitesse_droite (float): Vitesse de la roue droite.
        """
        # Calcul de la vitesse linéaire du robot (moyenne des vitesses des roues)
        vitesse_lineaire = (self.vitesse_gauche + self.vitesse_droite) / 2.0

        # Calcul de la rotation du robot (différence des vitesses des roues)
        rotation = (self.vitesse_droite - self.vitesse_gauche) * self.rayon_roue / self.largeur

        # Mise à jour de la direction du robot
        nouvelle_direction_x = self.direction_x * math.cos(rotation) - self.direction_y * math.sin(rotation)
        nouvelle_direction_y = self.direction_x * math.sin(rotation) + self.direction_y * math.cos(rotation)

        # Normalisation de la nouvelle direction
        norme = math.sqrt(nouvelle_direction_x ** 2 + nouvelle_direction_y ** 2)
        nouvelle_direction_x /= norme
        nouvelle_direction_y /= norme

        # Nouvelles coordonnées en fonction de la direction et de la vitesse
        nouveau_x = self.x + vitesse_lineaire * nouvelle_direction_x * deltat 
        nouveau_y = self.y + vitesse_lineaire * nouvelle_direction_y * deltat


        # Calcul de l'angle parcouru réel
        delta_x, delta_y = nouveau_x - self.x, nouveau_y - self.y
        angle_parcouru_reel = math.atan2(delta_y, delta_x) - math.atan2(self.direction_y, self.direction_x)
        self.angle_parcouru += angle_parcouru_reel

        # Mise à jour des coordonnées et de la direction
        self.x = nouveau_x
        self.y = nouveau_y
        self.direction_x = nouvelle_direction_x
        self.direction_y = nouvelle_direction_y

        #print(f"Position du robot : {self}")
        
        # Récupère la distance parcouru à chaque mouvement de position du robot.
        self.get_distance()

        self.positions_precedentes.append((self.x, self.y))

        # Affiche la distance parcouru dudepuis le premier déplacement
        #print("Distance parcouru : ", self.distance_parcouru)

    def get_angle(self):
        """Renvoie l'angle en degrés du robot dans le plan où 0 degré pointe vers la droite.

        Returns:
            float: Angle en degrés du robot dans le plan.
        """
        # Utilisation de la fonction atan2 pour obtenir l'angle par rapport à l'axe horizontal (droite)
        angle_radians = math.atan2(self.direction_y, self.direction_x)
        # Conversion de l'angle en radians en degrés et ajout de 360 degrés pour obtenir une mesure positive
        angle_degres = math.degrees(angle_radians) + 360
        # Correction pour que l'angle soit dans l'intervalle [0, 360)
        angle_degres %= 360
        return angle_degres

    def get_precedente_positions(self):
        """Renvoie les positions précédentes du robot."""
        return self.positions_precedentes.copy()
    
    def set_vitesse(self,vg,vd):
        self.vitesse_gauche= vg
        self.vitesse_droite= vd

    def detection_obstacle(self, obstacle_liste):
        """Vérifie s'il y a un obstacle devant le robot, renvoie la distance à laquelle se situe l'obstacle ou None sinon.

        Args:
            obstacle_liste (Obstacle): Liste d'obstacle mis en paramètre

        Returns:
            float: Distance à laquelle le robot se trouve de l'obstacle
        """
        # Variables prenant la position du robot, le laser
        check_x = self.x
        check_y = self.y

        # Vérifier si le laser sort de l'environnement
        while 0 <= check_x <= self.environnement.largeur and 0 <= check_y <= self.environnement.hauteur:

            # Nouvelles coordonnées permettant de vérifier s'il y a un obstacle
            check_x = check_x + self.direction_x
            check_y = check_y + self.direction_y

            # Vérification des coordonnées par rapport à l'obstacle
            for obstacle in obstacle_liste:
                if obstacle.est_dans_obstacle(check_x, check_y):

                    # Calcul de la distance du point par rapport au point du robot
                    distance = round(math.sqrt((check_x - self.x)**2 + (check_y - self.y), 2)**2)
                    print("La distance entre l'obstacle et le robot est de ", distance)

                    return distance

        distance = round(math.sqrt((check_x - self.x)**2 + (check_y - self.y)**2))
        print("La distance entre l'obstacle et le robot est de ", distance)
        return distance

    def get_distance(self):
        """Calcul la distance global parcouru par le robot.

        Args: 
            None

        Returns:
            None
        """

        # Vérifie que la liste n'est pas vide (que l'on se trouve dans le premier déplacement du robot)
        if self.positions_precedentes != []:
            # Calcul de la distance parcouru totale
            tot = self.distance_parcouru + math.sqrt((self.x - self.positions_precedentes[-1][0])**2 + (self.y - self.positions_precedentes[-1][1])**2)
        
        else:
            tot = 0

        # Met à jour la distance parcouru du robot
        self.distance_parcouru = tot 
        return self.distance_parcouru
    
    def update_distance(self):
        pass

    def reset_distance(self):
        self.distance_parcouru = 0

    def reset(self):
        pass

    def condition_angle(self,angle_vise):
        return round(self.get_angle()) >= round(angle_vise)

class Environnement:
    """Classe Environnement répertoriant le nécessaire pour créer un environnement

    """
    def __init__(self, largeur, hauteur,robot=None, liste_object=[]):
        self.largeur = largeur
        self.hauteur = hauteur
        self.robot = robot
        self.liste_object = liste_object
        self.temps_passe = time.time()

    def ajoute_object(self, obj):
        """Ajoute un obstacle à la liste d'obstacles de l'environnement.

        Args:
            obj: L'obstacle à ajouter (par exemple, un robot).

        """
        self.liste_object.append(obj)

    def ajout_obj_rand(self):
        """Ajoute un nombre aléatoire d'obstacles à l'environnement et les place aléatoirement."""

        n = int(random.random()*10)+1 #création du nombre d'obstacle dans la simu (entre 1 et 10)
        print("ajout de ",n," obstacles dans la simulation")
        
        for i in range(n):
            largeur = int(random.random()*50)+10
            hauteur = int(random.random()*50)+10 #valeur aleatoire entre 10 et 50 pour la hauteur et largeur
            
            x = random.random() * self.largeur - largeur
            y = random.random() * self.hauteur - hauteur
            
            nouvel_obstacle = Obstacle(x, y, largeur, hauteur)
            self.ajoute_object(nouvel_obstacle)

    def controle_positions(self):
        """Contrôle les positions des obstacles par rapport aux bordures de la fenêtre.

        Cette méthode peut être appelée périodiquement pour mettre à jour les positions
        des obstacles dans l'environnement et s'assurer qu'ils restent dans les limites de la fenêtre.

        """
        for obj in self.liste_object:
            # Contrôle des bordures pour l'obstacle (par exemple, un robot)
            if obj.x < 0:
                return True
            elif obj.x > self.largeur - obj.largeur:
                return True
            if obj.y < 0:
                return True
            elif obj.y > self.hauteur - obj.hauteur:
                return True
            else:
                return False

    def controle_collisions(self):
            """Vérifie les collisions entre le robot et les autres obstacles de l'environnement.

            Cette méthode peut être appelée périodiquement pour détecter les collisions
            entre le robot et les autres obstacles de l'environnement.

            """
            for obj in self.liste_object:
                # Vérifie la collision avec le robot
                if type(obj).__name__ == "Robot":
                    for autre_obj in self.liste_object:
                        # Vérifie la collision avec d'autres obstacles de l'environnement (sauf le robot lui-même)
                        if autre_obj != obj:
                            if self.collision(obj, autre_obj):
                                # Il y a une collision
                                print("Il y a eu une collision en (x:", round(obj.x,2), "y:", round(obj.y,2), ") avec", type(autre_obj).__name__)
                                return True
                                
                            
            return False

    def collision(self, obj1, obj2):
        """Vérifie la collision entre deux obstacles rectangulaires.

        Args:
            obj1 (obstacle): Premier obstacle.
            obj2 (obstacle): Deuxième obstacle.

        Returns:
            bool: True si les obstacles entrent en collision, False sinon.
        """
        if (
            obj1.x < obj2.x + obj2.largeur
            and obj1.x + obj1.largeur > obj2.x
            and obj1.y < obj2.y + obj2.hauteur
            and obj1.y + obj1.hauteur > obj2.y
        ):
            return True
        else:
            return False
        
    def update(self,FPS):
        """
        self.robot.update_position(self.deltat) 
        time.sleep(1/FPS)
        """
        
        #methode avec le vrai delta
        temps_actuel = time.time()
        delta_t = temps_actuel - self.temps_passe
        self.temps_passe = temps_actuel
        self.robot.update_position(delta_t) 
        time.sleep(1/FPS)

environnement = Environnement(LARGEUR_ENVIRONNEMENT,HAUTEUR_ENVIRONNEMENT)
r = Robot(ROBOT_X, ROBOT_Y, ROBOT_LONGUEUR, ROBOT_LARGEUR, DIRECTION_X, DIRECTION_Y, environnement, ROBOT_RAYON)
environnement.robot = r

xpos = 2
zpos = 3
direction_x = 0.5
direction_z = -0.5

modele_rob = 'robotv4.stl'
balise_layer = 'balise.jpg'
robot = Entity(model=modele_rob, texture='white_cube', color=color.blue, position=(xpos,0,zpos),scale = 0.005,rotation_x = 90)
text1 = Text(text="Fleche gauche = rotation gauche \nFleche droite = rotation droite \nFleche haut = avancer\nFleche bas = reculer \n1= camera Pov\n2 = camera Top", position=(-0.3, 0.1), scale=2, enabled=False)
text2 = Text(text="POV CAM", position=(0.6, 0.45), scale=2,color = color.black, enabled=False)
viseur_pov = Text(text="+",position = (-0.04,0.05),color = color.black,scale = (5,5,5))
arene = Entity(model= 'plane',texture= 'grille.jpg',collider= 'mesh',scale= (1000,1,1000),position = (0,-5,0))
balise = Entity(model= 'cube',texture = balise_layer, position = (0,0,0))
Sky()

camera_pov_rotation = (0,90,0)
camera_pov_position = (robot.x+0.3,0.1,robot.z)
camera_top_rotation = (90,90,0)
camera_top_position = (robot.x,30,robot.z)
camera_menu_rotation = (45,50,-50)
       
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
        camera.fov = 90
        pov = 1

    if bouton == "2" or bouton == "é":
        #Si l'utilisateur veut que la caméra soit en mode TOP
        camera.position = (robot.x,30,robot.z)
        camera.rotation = (90,90,0)
        camera.fov = 60
        text1.enabled = False
        text2.enabled = False
        viseur_pov.enabled = False
        pov = 0

    if bouton == "0" or bouton == "à":
        #Si l'utilisateur veut que la caméra soit en mode MENU
        camera.position = camera_menu_rotation
        text1.enabled = True
        text2.enabled = False
        viseur_pov.enabled = False
        pov = 3

change_camera("0")

def tourner(angle_degres):
    global direction_x, direction_z

    angle_radians = math.radians(angle_degres)

    new_direction_x = direction_x * math.cos(angle_radians) - direction_z * math.sin(angle_radians)
    new_direction_z = direction_x * math.sin(angle_radians) + direction_z * math.cos(angle_radians)

    direction_x, direction_z = new_direction_x, new_direction_z



def update():
    global direction_x, direction_z,r,robot

    robot.x = r.x
    robot.z = r.y
    print(str(robot.x)+ " " + str(robot.y))

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
    if held_keys['up arrow']:
        if pov == 1:
            camera.fov += 1
        if pov == 0:
            camera.y+=1
            camera.position = (camera.x,camera.y,camera.z)
    if held_keys['down arrow']:
        if pov == 1:
            camera.fov -= 1
        if pov == 0:
            camera.y-=1
            camera.position = (camera.x,camera.y,camera.z)

    if pov == 1:
        camera.position = robot.position
    if pov == 0:
        camera.position = (robot.x,camera.y,robot.z)


def run_controleur(controleur,environnement):
    """
    boucle du controleur
    """
    controleur.start()
    while not controleur.stop():
        if not environnement.controle_collisions():
            controleur.step()
        time.sleep(1 / FPS_CONTROLEUR)



def run_environnement(environnement):
    """
    Boucle de l'environnement
    """
    while True:
        if not environnement.controle_positions():
            if not environnement.controle_collisions():
                environnement.update(FPS_ENVIRONNEMENT)


controleur = Controleur()
avancer=Avancer(r,environnement,100)
tourner = Tourner_D(r,environnement,90)
faire_carrer = Sequentiel()
faire_carrer.strategies=[avancer,tourner]*4
controleur.add_strategie(faire_carrer)

thread_controler = threading.Thread(target=run_controleur, args=(controleur,environnement))
thread_env = threading.Thread(target=run_environnement, args=(environnement,))
thread_env.start()
thread_controler.start()
app.run()

