import math
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

    def __init__(self, x, y, largeur, hauteur, direction_x, direction_y, environnement, rayon_roue):
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.environnement = environnement
        # Créer les roues avec un rayon de rRoue
        self.rayon_roue = rayon_roue

        self.positions_precedentes = []

    def __str__(self):
        return "(" + str(round(self.x, 2)) + "," + str(round(self.y, 2)) + ")"

    def update_position(self, vitesse_gauche, vitesse_droite):
        """Déplace le robot en fonction des vitesses spécifiées pour les roues gauche et droite.

        Args:
            vitesse_gauche (float): Vitesse de la roue gauche.
            vitesse_droite (float): Vitesse de la roue droite.
        """
        # Calcul de la vitesse linéaire du robot (moyenne des vitesses des roues)
        vitesse_lineaire = (vitesse_gauche + vitesse_droite) / 2.0

        # Calcul de la rotation du robot (différence des vitesses des roues)
        rotation = (vitesse_droite - vitesse_gauche) * self.rayon_roue / self.largeur

        # Mise à jour de la direction du robot
        nouvelle_direction_x = self.direction_x * math.cos(rotation) - self.direction_y * math.sin(rotation)
        nouvelle_direction_y = self.direction_x * math.sin(rotation) + self.direction_y * math.cos(rotation)

        # Normalisation de la nouvelle direction
        norme = math.sqrt(nouvelle_direction_x ** 2 + nouvelle_direction_y ** 2)
        nouvelle_direction_x /= norme
        nouvelle_direction_y /= norme

        # Nouvelles coordonnées en fonction de la direction et de la vitesse
        nouveau_x = self.x + vitesse_lineaire * nouvelle_direction_x
        nouveau_y = self.y + vitesse_lineaire * nouvelle_direction_y

        # Mise à jour des coordonnées et de la direction
        self.x = nouveau_x
        self.y = nouveau_y
        self.direction_x = nouvelle_direction_x
        self.direction_y = nouvelle_direction_y

        print(f"Position du robot : {self}")

        self.positions_precedentes.append((self.x, self.y))

    def get_angle(self):
        """Renvoie l'angle en degrés du robot dans le plan où 0 degré pointe vers
