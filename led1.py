import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

gpio.setup(2, gpio.OUT)

while (True):

    gpio.output(2, 1)

    time.sleep(0.5)

    gpio.output(2, 0)

    time.sleep(0.5)