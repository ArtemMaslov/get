import RPi.GPIO as gpio
from time import sleep 
from threading import Thread

gpio.setmode(gpio.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
troyka = 17
comp = 4

gpio.setup(leds, gpio.OUT)
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial = 1)
gpio.setup(comp, gpio.IN)

def dec_to_bin(num):
    return [int(bit) for bit in bin(num)[2:].zfill(8)]

def bin_to_dec(bits):
    dec = 0
    code = 1
    for i in range(7, -1, -1):
        dec += bits[i] * code
        code *= 2
    return dec

def adc2():
    voltage = 8*[0]
    
    gpio.output(dac, 0)

    sleep(0.01)

    for st in range(0, 8):
        voltage[st] = 1

        gpio.output(dac[st], voltage[st])

        sleep(0.01)

        if (gpio.input(comp) == 0): # led is on
            voltage[st] = 0
            gpio.output(dac[st], voltage[st])

    dec = bin_to_dec(voltage)
    return dec

def adc1():
    voltage = 0
    while (voltage < 256):
        
        gpio.output(dac, dec_to_bin(voltage))

        sleep(0.001)

        if (gpio.input(comp) == 0): # led is on
            break
        voltage += 1
    return voltage

def ConvertVolume(number):
    active = int(number / 32)
    if (active > 8):
        active = 8
    bits = (8 - active) * [0] + active * [1]
    return bits

stop_thread = False
thread_stoped = False

def DoComp():
    global thread_stoped
    global stop_thread
    global T

    try:
        while (not stop_thread):
            
            dec = adc1()
            print("Adc Volage = {:.3} v, volage code = {}".format(dec / 256.0 * 3.3, dec))

            gpio.output(leds, ConvertVolume(dec + 6))
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