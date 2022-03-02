import RPi.GPIO as gpio
from time import sleep 

gpio.cleanup()
gpio.setmode(gpio.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]

#         7  6  5  4  3  2  1  0
number = [0, 0, 0, 1, 0, 0, 0, 1]

dac    = [26, 19, 13, 6, 5, 11, 9, 10]

gpio.setup(dac, gpio.OUT)

gpio.output(dac, number)

sleep(10)

gpio.output(dac, 0)

gpio.cleanup()