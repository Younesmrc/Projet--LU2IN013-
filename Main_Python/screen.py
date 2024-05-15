from robot2IN013 import Robot2IN013 as R
from PIL import Image
from time import sleep
import numpy as np
from Traitement_image import *
print("YOOOOOOOOOOO")
r = R()

r.start_recording()

sleep(1)

img = r.get_image()
print(img)
x,y = get_position_balise(img)
print(x)
print(y)
print("FINNNNNNNNNN")       