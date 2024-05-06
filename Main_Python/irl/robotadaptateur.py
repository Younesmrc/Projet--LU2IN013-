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

        self.angle_parcouru = 0
        self.distance_parcouru = 0

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

    def update_distance(self):
        """Déplace le robot en fonction des vitesses spécifiées pour les roues gauche et droite.

        Args:
            vitesse_gauche (float): Vitesse de la roue gauche.
            vitesse_droite (float): Vitesse de la roue droite.
        """

        angle_gauche,angle_droit = self.robot.get_motor_position()
        #PRINT ANGLE
        print("angle gauche :" + str(angle_gauche)+"angle droit :"+ str(angle_droit))

        #CALCULE DISTANCE
        #distance_lineaire_parcouru_rd = self.rayon_roue * math.radians(self.robot.get_motor_position()[0])
        #distance_lineaire_parcouru_rg = self.rayon_roue * math.radians(self.robot.get_motor_position()[1])
        distance_lineaire_parcouru_rd = self.robot.WHEEL_CIRCUMFERENCE * (angle_gauche / 360)
        distance_lineaire_parcouru_rg = self.robot.WHEEL_CIRCUMFERENCE * (angle_droit/ 360)

        #PRINT DISTANCE 
        print("distance gauche "+str(distance_lineaire_parcouru_rg)+" distance droit : "+ str(distance_lineaire_parcouru_rd))


        distance_totale_parcourue = (distance_lineaire_parcouru_rd + distance_lineaire_parcouru_rg) / 2.0
        self.distance_parcouru+=distance_totale_parcourue

        #ROTATION
        
        #rotation = self.calcul_rotation(angle_gauche,angle_droit)
        #self.angle_parcouru+=rotation
        rotation = (distance_lineaire_parcouru_rd - distance_lineaire_parcouru_rg) / self.largeur
        self.angle_parcouru += (rotation*180/math.pi)
        
        #misa a jour direction position... ---------------------------------------------------------------------------------

        # Mise à jour de la direction du robot
        nouvelle_direction_x = self.direction_x * math.cos(rotation) - self.direction_y * math.sin(rotation)
        nouvelle_direction_y = self.direction_x * math.sin(rotation) + self.direction_y * math.cos(rotation)

        # Normalisation de la nouvelle direction
        norme = math.sqrt(nouvelle_direction_x ** 2 + nouvelle_direction_y ** 2)
        nouvelle_direction_x /= norme
        nouvelle_direction_y /= norme

        # Nouvelles coordonnées en fonction de la direction et de la vitesse
        nouveau_x = self.x + distance_totale_parcourue * nouvelle_direction_x 
        nouveau_y = self.y + distance_totale_parcourue * nouvelle_direction_y 

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
        return self.angle_parcouru


    def get_precedente_positions(self):
        """Renvoie les positions précédentes du robot."""
        return self.positions_precedentes.copy()


    def detection_obstacle(self):
        return self.robot.get_distance()

    def get_distance(self):
        """Calcul la distance global parcouru par le robot.

        Args: 
            None

        Returns:
            double: retoure la distance parcouru des roues du robot en fonction de ses roues
        """

        return self.distance_parcouru
      
    def reset(self):
        # Remise à zéro de l'angle des roues
        self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT, self.robot.read_encoders()[0])
        self.robot.offset_motor_encoder(self.robot.MOTOR_RIGHT, self.robot.read_encoders()[1])

    def reset_angle(self):
        self.reset()
        self.angle_parcouru = 0

    def reset_distance(self):
        self.reset()
        self.distance_parcouru = 0

    def condition_angle(self,angle_vise):
        return self.angle_parcouru <= angle_vise
    
    def calcul_rotation(self,angle_gauche, angle_droite):
        # Convertir les angles en radians
        angle_gauche_rad = math.radians(angle_gauche)
        angle_droite_rad = math.radians(angle_droite)
        
        # Calculer les distances parcourues par chaque roue
        distance_gauche = angle_gauche_rad * self.rayon_roue
        distance_droite = angle_droite_rad * self.rayon_roue
        
        # Calculer la différence de distance
        difference_distance = distance_droite - distance_gauche
        
        # Calculer l'angle de rotation en radians
        angle_rotation_rad = difference_distance / self.rayon_roue
        
        # Retourner l'angle de rotation en degrés
        return math.degrees(angle_rotation_rad)
    
    def calcul_nouveau_vecteur(x, y, angle_rotation):
        # Conversion de l'angle de rotation en radians
        angle_rotation_rad = math.radians(angle_rotation)
        
        # Calcul des nouveaux composants x et y du vecteur
        nouveau_x = x * math.cos(angle_rotation_rad) - y * math.sin(angle_rotation_rad)
        nouveau_y = x * math.sin(angle_rotation_rad) + y * math.cos(angle_rotation_rad)
        
        # Retourne les nouveaux composants x et y
        return nouveau_x, nouveau_y
