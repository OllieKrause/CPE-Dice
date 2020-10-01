#dice example
from adafruit_circuitplayground import cp
import time
import random

brightness = 25

def dice():
    roll=(random.randint(1, 6)) #create randomization here
    if (roll==1):
        cp.pixels[1]=(brightness, 0, 0)
    if (roll==2):
        cp.pixels[2]=(brightness, 0, 0)
    if (roll==3):
        cp.pixels[3]=(brightness, 0, 0)
    if (roll==4):
        cp.pixels[4]=(brightness, 0, 0)
    if (roll==5):
        cp.pixels[5]=(brightness, 0, 0)
    if (roll==6):
        cp.pixels[6]=(brightness, 0, 0)

    time.sleep(2.0)
    cp.pixels.fill((0, 0, 0))

while True:
    if cp.shake():  #use the shake example code here
        dice()
        cp.red_led = True

    else:
        cp.red_led = False