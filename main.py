# https://neal.fun/perfect-circle/

import pyautogui as pag
from math import cos, sin, pi
from time import sleep

origin_x = 1137.5
origin_y = 539.5
r = 420

x_coordinates = []
y_coordinates = []
for angle in range(0, 360):
    if angle % 6 == 0:
        x_coordinates.append(origin_x + (r * cos(2 * pi * angle / 360)))
        y_coordinates.append(origin_y + (r * sin(2 * pi * angle / 360)))

sleep(1)
pag.moveTo(
    origin_x + (r * cos(0)),
    origin_y + (r * sin(0))
)
sleep(0.1)
pag.mouseDown()
sleep(0.1)

for i in range(len(x_coordinates)):
    pag.moveTo(x_coordinates[i], y_coordinates[i])

pag.mouseUp()