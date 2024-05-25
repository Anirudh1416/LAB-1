import time
time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico!")

from Dinorunnergame import *

myplayer1 = Player()

myplayer1.testDisplay()