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
        self.parcouru = 0
    
    def step(self):
        """Déplace le robot vers l'avant d'un petit pas."""
        
        # Met une vitesse arbitraire au robot
        self.robot.set_vitesse(1, 1) 

        # Calcul la distance parcouru en fonction de la vitesse
        self.parcouru += (self.robot.vitesse_gauche + self.robot.vitesse_droite) / 2  
        
        if self.stop():
            return
        
        # Rafraichissement du robot dans le cas où il rentre en collision
        if not self.environnement.controle_collisions():
            self.robot.update_position()  

    def stop(self):
        """Vérifie si le robot a parcouru la distance spécifiée."""
        return self.parcouru > self.distance
