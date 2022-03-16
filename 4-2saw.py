import RPi.GPIO as gpio
from time import sleep 
from threading import Thread

gpio.setmode(gpio.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

gpio.setup(dac, gpio.OUT)

def dec_to_bin(num):
    return [int(bit) for bit in bin(num)[2:].zfill(8)]

T = 10.0

stop_thread = False
thread_stoped = False

def DoSaw():
    global thread_stoped
    global stop_thread
    global T

    try:
        while (not stop_thread):
            ampl = 255
            t = T / 256

            oldT = T

            while (ampl > 0):
                
                gpio.output(dac, dec_to_bin(ampl))

                sleep(t)

                if (oldT != T):
                    break

                ampl -= 1
    finally:
        thread_stoped = True

def ParseT(str):
    global T
    
    if (str.find("T ") == -1):
        return

    try:
        num = float(str[2:])
    except ValueError:
        print("Не известная команда")
    else:
        T = num

Thread(target=DoSaw).start()

try:
    while (True):

        buf = input("Введите команду:\n")

        if (buf == "exit"):
            break

        ParseT(buf)

        continue
        
finally:
    stop_thread = True

    while (not thread_stoped):
        sleep(1)

    gpio.output(dac, 0)
    gpio.cleanup()