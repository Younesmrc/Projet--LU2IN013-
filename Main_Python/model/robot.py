import math
import time 
from model.objet import Objet

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
            Initialise un objet Robot avec les coordonnées, la taille, la direction, l'environnement et le rayon des roues spécifiés.

        __str__(self):
            Renvoie une représentation sous forme de chaîne de la position actuelle du robot.

        update_position(self, vitesse_gauche, vitesse_droite):
            Déplace le robot en fonction des vitesses spécifiées pour les roues gauche et droite.

        get_angle(self):
            Renvoie l'angle en degrés du robot dans le plan où 0 degré pointe vers la droite.

        get_precedente_positions(self):
            Renvoie les positions précédentes du robot.

        detection_obstacle(self, objet):
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

        # Mise à jour des coordonnées et de la direction
        self.x = nouveau_x
        self.y = nouveau_y
        self.direction_x = nouvelle_direction_x
        self.direction_y = nouvelle_direction_y

        print(f"Position du robot : {self}")
        
        # Calcul la distance parcouru à chaque mouvement de position du robot.
        self.calcul_distance()

        self.positions_precedentes.append((self.x, self.y))

        # Affiche la distance parcouru dudepuis le premier déplacement
        print("Distance parcouru : ", self.distance_parcouru)

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
        """Vérifie s'il y a un obstacle devant le robot, renvoie la distance à laquelle se situe l'objet ou None sinon.

        Args:
            obstacle_liste (Objet): Liste d'objet mis en paramètre

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
                    distance = round(math.sqrt(pow((check_x - self.x), 2) + pow((check_y - self.y), 2)), 2)
                    print("La distance entre l'obstacle et le robot est de ", distance)

                    return distance

        distance = round(math.sqrt(pow((check_x - self.x), 2) + pow((check_y - self.y), 2)), 2)
        print("La distance entre l'obstacle et le robot est de ", distance)
        return distance

    def calcul_distance(self):
        """Calcul la distance global parcouru par le robot.

        Args: 
            None

        Returns:
            None
        """

        # Vérifie que la liste n'est pas vide (que l'on se trouve dans le premier déplacement du robot)
        if self.positions_precedentes != []:
            # Calcul de la distance parcouru totale
            tot = self.distance_parcouru + math.sqrt( pow((self.x - self.positions_precedentes[-1][0]),2) + pow((self.y - self.positions_precedentes[-1][1]),2))
        
        else:
            tot = 0

        # Met à jour la distance parcouru du robot
        self.distance_parcouru = tot