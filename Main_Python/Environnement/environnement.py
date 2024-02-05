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
