from .mockup import Robot2I013Mockup


class RobotAdaptateur:
    def __init__(self, robot_mockup):
        self.robot_mockup = robot_mockup

    def set_vitesse(self, vitesse_gauche, vitesse_droite):
        self.robot_mockup.set_motor_dps(self.robot_mockup.MOTOR_LEFT, vitesse_gauche)
        self.robot_mockup.set_motor_dps(self.robot_mockup.MOTOR_RIGHT, vitesse_droite)

    def set_led(self, led, rouge, vert, bleu):
        return

    def get_distance(self):
        return


    def stop(self):
        return
