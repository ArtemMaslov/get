import RPi.GPIO as gpio
from time import sleep 

gpio.cleanup()
gpio.setmode(gpio.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]
pattern = [0, 0, 0, 0, 0, 0, 0, 0]

gpio.setup(leds, gpio.OUT)

gpio.output(leds,0)

for st2 in range(0, 3):
#while (True):
    for st in range(0, 8):
        
        for st1 in range(0,8):
            pattern[st1] = 0
        
        pattern[st] = 1

        gpio.output(leds, pattern)

        sleep(0.2)

gpio.output(leds, 1)

sleep(1)

gpio.output(leds, 0)

gpio.cleanup()