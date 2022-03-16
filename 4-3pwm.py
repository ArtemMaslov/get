import RPi.GPIO as gpio
from time import sleep
from threading import Thread

gpio.setmode(gpio.BCM)

pin = [2, 25]

stop_thread = False
thread_stoped = False

gpio.setup(pin, gpio.OUT)

T = 0.1
t = 0.05

def print_voltage():
    global T
    global t
    print("Напряжение на выходе V = {:.4f} В".format(3.3 * t / T))

def DoPWM():
    global thread_stoped
    global stop_thread
    global T
    global t

    try:
        while (not stop_thread):
            gpio.output(pin, 1)

            sleep(t)

            gpio.output(pin, 0)

            if (T > t):
                sleep(T - t)
    finally:
        thread_stoped = True

def ParseT(str):
    global T
    global t
    
    if (str.find("T ") != -1):
        try:
            num = float(str[2:])
        except ValueError:
            print("Не известная команда")
        else:
            if (num < 0):
                print ("Число должно быть не отрицательным")
                return 

            if (num < t):
                print ("duty time не может быть больше периода")
                return

            T = num
            print_voltage()

    elif (str.find("t ") != -1):
        try:
            num = float(str[2:])
        except ValueError:
            print("Не известная команда")
        else:
            if (num < 0):
                print ("Число должно быть не отрицательным")
                return 

            if (num > T):
                print ("duty time не может быть больше периода")
                return
            
            t = num
            print_voltage()

    else:
        print("Не известная команда")

Thread(target=DoPWM).start()

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

    gpio.output(pin, 0)
    gpio.cleanup()