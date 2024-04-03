

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
                                                                                                                                                                  