# https://neal.fun/perfect-circle/

# imports
import pyautogui as pag
from math import cos, sin, pi
from time import sleep

# config
origin_x = 1137.5
origin_y = 539.5
r = 420
smoothness = 6 # how many points around the circle to move the cursor to. higher = smoother but takes longer, so might run out of time and fail

# generate coordinates to move to
x_coordinates = []
y_coordinates = []
for angle in range(0, 360):
    if angle % smoothness == 0:
        x_coordinates.append(origin_x + (r * cos(2 * pi * angle / 360)))
        y_coordinates.append(origin_y + (r * sin(2 * pi * angle / 360)))

# draw the circle
sleep(1)
pag.moveTo(origin_x + r, origin_y)
sleep(0.1)
pag.mouseDown()
sleep(0.1)
for i in range(len(x_coordinates)): pag.moveTo(x_coordinates[i], y_coordinates[i])
pag.mouseUp()
