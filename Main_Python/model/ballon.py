from . import Robot
import math
class Ballon(Robot):
    def __init__(self, x, y, taille, direction_x, direction_y, environnement, rayon_roue, vitesse_droite=1, vitesse_gauche=1):
        super().__init__(x, y, taille, taille, direction_x, direction_y, environnement, rayon_roue, vitesse_droite, vitesse_gauche)

    def cogner(self, robot):
        
        self.vitesse_gauche += 2*robot.vitesse_gauche
        self.vitesse_droite += 2*robot.vitesse_droite

    def update(self, dt):
        
        norme_vitesse = max(0, math.sqrt(self.vitesse_gauche ** 2 + self.vitesse_droite ** 2) - dt * (0.01 * (self.vitesse_gauche ** 2 + self.vitesse_droite ** 2) - 0.06*math.sqrt(self.vitesse_gauche ** 2 + self.vitesse_droite ** 2)))
        if norme_vitesse == 0:
            self.vitesse_gauche = 0
            self.vitesse_droite = 0
        
        
        super().update(dt)

        return (self.x, self.y)
