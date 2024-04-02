import math


class Robot2I013Mockup():
    """
        Une image de l'api robot pour tester si on a une parfaite utilisation des fonctions
    """

    WHEEL_BASE_WIDTH = 100
    WHEEL_DIAMETER = 50

    def __init__(self):
        self.MOTOR_LEFT = 0
        self.MOTOR_RIGHT = 0

    def set_led(self, led, red, green, blue):
        pass

    def get_voltage(self):
        pass

    def set_motor_dps(self, port, dps):
        print("SET MOTOR DPS")

    def get_motor_position(self):
        return (0, 0)

    def offset_motor_encoder(self, port, offset):
        pass

    def get_distance(self):
        return 100

    def servo_rotate(self, position):
        pass

    def stop(self):
        pass

    def get_image(self):
        pass

    def __getattr__(self,dps):
        return 1