import RPi.GPIO as gpio
from time import sleep 

gpio.cleanup()
gpio.setmode(gpio.BCM)

leds = [21, 20, 16, 12, 7,  8, 25, 24]

aux =  [22, 23, 27, 18, 15, 14, 3, 2]

gpio.setup(leds, gpio.OUT)
gpio.setup(aux, gpio.IN)

gpio.output(leds, 0)
#while (True):
#    for st in range(0,8):
#        gpio.output(leds[st], gpio.input(aux[st]))



gpio.cleanup()