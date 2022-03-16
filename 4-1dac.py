import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

gpio.setup(dac, gpio.OUT)

def dec_to_bin(num):
    return [int(bit) for bit in bin(num)[2:].zfill(8)]

def print_voltage(num):
    print("Напряжение на выходе V = {:.3f} В".format(num / 256.0))

try:
    while (True):
        print("Введите десятичное число:\n")

        str = input()

        if (str == "exit"):
            break

        try:
            num = int(str)
        except ValueError:
            print("Ошибка ввода! Введенная строка \"", str, "\" не является десятичным числом.", sep = '')
        else:
            if (num < 0):
                print("Введёное число должно быть не отрицательным.")
                continue

            if (num > 255):
                print("Введёное число должно быть меньше 256.")
                continue

            gpio.output(dac, dec_to_bin(num))

            print_voltage(num)

finally:
    gpio.output(dac, 0)
    gpio.cleanup()