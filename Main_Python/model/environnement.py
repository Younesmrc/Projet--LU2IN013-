import time
import random
from model.objet import Objet


class Environnement:
    """Classe Environnement répertoriant le nécessaire pour créer un environnement

    """
    def __init__(self, largeur, hauteur,deltat,robot=None, liste_object=[]):
        self.largeur = largeur
        self.hauteur = hauteur
        self.robot = robot
        self.liste_object = liste_object
        self.deltat=deltat
        self.temps_passe = time.time()

    def ajoute_object(self, obj):
        """Ajoute un objet à la liste d'objets de l'environnement.

        Args:
            obj: L'objet à ajouter (par exemple, un robot).

        """
        self.liste_object.append(obj)

    def ajout_obj_rand(self):
        """Ajoute un nombre aléatoire d'objets à l'environnement et les place aléatoirement."""

        n = int(random.random()*10)+1 #création du nombre d'objet dans la simu (entre 1 et 10)
        print("ajout de ",n," objets dans la simulation")
        
        for i in range(n):
            largeur = int(random.random()*50)+10
            hauteur = int(random.random()*50)+10 #valeur aleatoire entre 10 et 50 pour la hauteur et largeur
            
            x = random.random() * self.largeur - largeur
            y = random.random() * self.hauteur - hauteur
            
            nouvel_objet = Objet(x, y, largeur, hauteur)
            self.ajoute_object(nouvel_objet)

    def controle_positions(self):
        """Contrôle les positions des objets par rapport aux bordures de la fenêtre.

        Cette méthode peut être appelée périodiquement pour mettre à jour les positions
        des objets dans l'environnement et s'assurer qu'ils restent dans les limites de la fenêtre.

        """
        for obj in self.liste_object:
            # Contrôle des bordures pour l'objet (par exemple, un robot)
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
            """Vérifie les collisions entre le robot et les autres objets de l'environnement.

            Cette méthode peut être appelée périodiquement pour détecter les collisions
            entre le robot et les autres objets de l'environnement.

            """
            for obj in self.liste_object:
                # Vérifie la collision avec le robot
                if type(obj).__name__ == "Robot":
                    for autre_obj in self.liste_object:
                        # Vérifie la collision avec d'autres objets de l'environnement (sauf le robot lui-même)
                        if autre_obj != obj:
                            if self.collision(obj, autre_obj):
                                # Il y a une collision
                                print("Il y a eu une collision en (x:", round(obj.x,2), "y:", round(obj.y,2), ") avec", type(autre_obj).__name__)
                                return True
                                
                            
            return False

    def collision(self, obj1, obj2):
        """Vérifie la collision entre deux objets rectangulaires.

        Args:
            obj1 (objet): Premier objet.
            obj2 (objet): Deuxième objet.

        Returns:
            bool: True si les objets entrent en collision, False sinon.
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