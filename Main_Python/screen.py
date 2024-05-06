from robot2IN013 import Robot2IN013 as R
from PIL import Image
from time import sleep
import numpy as np

r = R()

r.servo_rotate(90) #mettre la cam au milieu
sleep(1)

img = r.get_image()
img = np.array(img)

img = Image.fromarray(img)
img.save("image.png")