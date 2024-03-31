from .mockup import Robot2I013Mockup
import math
import time


class RobotAdaptateur:
    def __init__(self,robot,x,y,direction_x,direction_y,environnement):
        self.robot = robot
        self.x = x
        self.y = y
        self.largeur = self.robot.WHEEL_BASE_WIDTH
        self.hauteur = 100 # A VOIR ?
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.environnement = environnement


        # Créer les roues avec un rayon de rRoue
        self.rayon_roue = self.robot.WHEEL_BASE_WIDTH /2.0 #diametre/2
        self.vitesse_droite=0
        self.vitesse_gauche = 0
        self.temps_passe = time.time()
		
        self.positions_precedentes = []

    def set_vitesse(self,vitesse_gauche,vitesse_droite):
        self.robot.set_motor_dps(self.robot.__getattr__("MOTOR_LEFT"),vitesse_gauche)
        self.robot.set_motor_dps(self.robot.__getattr__("MOTOR_RIGHT"),vitesse_droite)
        self.vitesse_gauche=vitesse_gauche
        self.vitesse_droit=vitesse_droite

        
    def update_temps_passe(self):
        """Met à jour le temps passé depuis la dernière mise à jour pour la stratégie rond ."""
        temps_actuel = time.time()
        temps_passe = temps_actuel - self.temps_passe
        self.temps_passe = temps_actuel
        return temps_passe

    def update_position(self):
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
        nouveau_x = self.x + vitesse_lineaire * nouvelle_direction_x 
        nouveau_y = self.y + vitesse_lineaire * nouvelle_direction_y 

        # Mise à jour des coordonnées et de la direction
        self.x = nouveau_x
        self.y = nouveau_y
        self.direction_x = nouvelle_direction_x
        self.direction_y = nouvelle_direction_y


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


    def detection_obstacle(self, obstacle_liste):
        return self.robot.get_distance()

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