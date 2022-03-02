import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)


outPin = 17
inPin  = 27
gpio.setup(outPin, gpio.OUT)

gpio.setup(inPin, gpio.IN)

while(True):
    gpio.output(outPin, gpio.input(inPin))

    print("in: ", gpio.input(inPin))
    print("out:", gpio.input(outPin))

    time.sleep(0.1)