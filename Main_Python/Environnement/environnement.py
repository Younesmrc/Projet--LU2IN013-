class Environnement:
    """Classe Environnement répertoriant le nécessaire pour créer un environnement

    """
    def __init__(self, largeur, hauteur, liste_object=[]):
        self.largeur = largeur
        self.hauteur = hauteur
        self.liste_object = liste_object

    def ajoute_object(self, obj):
        """Ajoute un objet à la liste d'objets de l'environnement.

        Args:
            obj: L'objet à ajouter (par exemple, un robot).

        """
        self.liste_object.append(obj)

    def controle_positions(self):
        """Contrôle les positions des objets par rapport aux bordures de la fenêtre.

        Cette méthode peut être appelée périodiquement pour mettre à jour les positions
        des objets dans l'environnement et s'assurer qu'ils restent dans les limites de la fenêtre.

        """
        for obj in self.liste_object:
            # Contrôle des bordures pour l'objet (par exemple, un robot)
            if obj.x < 0:
                obj.x = 0
            elif obj.x > self.largeur - obj.largeur:
                obj.x = self.largeur - obj.largeur

            if obj.y < 0:
                obj.y = 0
            elif obj.y > self.hauteur - obj.hauteur:
                obj.y = self.hauteur - obj.hauteur

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
                                # Gestion de la collision (ajustement de la position proche de la bordure)
                                self.ajuster_position(obj, autre_obj)

    def ajuster_position(self, obj, autre_obj):
        """Ajuste la position de l'objet pour éviter une collision avec un autre objet.

        Args:
            obj (objet): Objet à ajuster.
            autre_obj (objet): Objet avec lequel une collision est détectée.

        Returns:
            None
        """
        # Calcul des nouvelles coordonnées proches de la bordure
        new_x = obj.x
        new_y = obj.y

        # Si la collision est en X
        if obj.x < autre_obj.x:
            new_x = autre_obj.x - obj.largeur
        elif obj.x > autre_obj.x:
            new_x = autre_obj.x + autre_obj.largeur

        # Si la collision est en Y
        if obj.y < autre_obj.y:
            new_y = autre_obj.y - obj.hauteur
        elif obj.y > autre_obj.y:
            new_y = autre_obj.y + autre_obj.hauteur

        # Mise à jour des coordonnées de l'objet
        obj.x = new_x
        obj.y = new_y


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