import time
import random
from model.obstacle import Obstacle


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