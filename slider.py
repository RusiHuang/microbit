# Write your code here :-)
from microbit import *
import random
display.show(Image.SQUARE)
for x in range(4):
    for y in range(4):
        display.set_pixel(x, y, 9)

lights = 0
#display.scroll(str(pin2.read_analog()))
#display.show(Image.HAPPY)
while True:

    #display.scroll(str(int(pin2.read_analog() / 2)))
    for i in range(int(pin2.read_analog() / 16)):
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        display.set_pixel(x, y, 0)
    if pin2.read_analog() <= 437.5:
        for x in range(5):
            for y in range(5):
                display.set_pixel(x, y, 9)
