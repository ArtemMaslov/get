import RPi.GPIO as gpio
from time import sleep 
from threading import Thread

gpio.setmode(gpio.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
troyka = 17
comp = 4

gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial = 1)
gpio.setup(comp, gpio.IN)

def dec_to_bin(num):
    return [int(bit) for bit in bin(num)[2:].zfill(8)]

def adc(number):
    print("Adc Volage = {:.2} v, volage code = {}".format(number / 256.0 * 3.3, number))

stop_thread = False
thread_stoped = False

def DoComp():
    global thread_stoped
    global stop_thread
    global T

    try:
        while (not stop_thread):
            
            volage = 0
            while (volage < 256):
                
                gpio.output(dac, dec_to_bin(volage))

                sleep(0.01)
                
                if (gpio.input(comp) == 0):
                    adc(volage)
                    break
                
                volage += 1
    finally:
        thread_stoped = True

Thread(target = DoComp).start()

try:
    while (True):

        buf = input("Введите команду:\n")

        if (buf == "exit"):
            break

        continue
        
finally:
    stop_thread = True

    while (not thread_stoped):
        sleep(1)

    gpio.output(dac, 0)
    gpio.output(troyka, 0)
    gpio.cleanup()