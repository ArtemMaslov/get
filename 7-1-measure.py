import RPi.GPIO as gpio
from time import sleep 
from time import time
from threading import Thread
import matplotlib as plt

gpio.setmode(gpio.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
troyka = 17
comp = 4

gpio.setup(leds, gpio.OUT)
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial = 0)
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

def adc():
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

value = []
startT = 0
stopT  = 0
dec = 0

try:
    startT = time()
    gpio.output(troyka, 1)

    while (dec < 0.97 * 256):
        
        dec = adc() / 256.0 * 3.3
        print("Adc Volage+ = {:.3} v, volage code = {}".format(dec, dec * 256 / 3.3))

        value.append(dec)

    gpio.output(troyka, 0)

    while (dec > 0.02 * 256):

        dec = adc()/ 256.0 * 3.3
        print("Adc Volage- = {:.3} v, volage code = {}".format(dec, dec * 256 / 3.3))
        
        value.append(dec)

    stopT = time()

    with open('measureData.txt', 'w') as f:
        f.write('\n'.join([str(val) for val in value]))

    expTime = stopT - startT

    with open('settings.txt', 'w') as f:
        f.write('Время измерения, с {:.6f}'.format(expTime))
        f.write('Шаг квантования, В {:.6f}'.format(3.3 / 256))

    print(expTime)
    print('Время измерения, с', expTime)
    print('Период измерения, с', expTime /  len(value))
    print('Частота дискр, Гц', len(value) / expTime)
    print('Шаг квантования, В', 3.3 / 256)
    
finally:
    gpio.output(dac, 0)
    gpio.output(troyka, 0)
    gpio.cleanup()