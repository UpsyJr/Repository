import RPi.GPIO as GPIO
from time import sleep
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.OUT)  # we are using this pin to produce the light

selection = int(input("Choose mode 1 - 2 - 3: "))

while True:
    try:
        if selection == 1:
            while index < 10:
                GPIO.output(22, True)
                sleep(5)
                GPIO.output(22, False)
                sleep(3)
                index += 1
        elif selection == 2:
            while index < 10:
                GPIO.output(22, False)
                sleep(5)
                GPIO.output(22, True)
                sleep(5)
                index += 1
        elif selection == 4:
            GPIO.output(22, False)
            sleep(7)
            GPIO.output(22, True)
            sleep(2)
            # ctrl + c for keyboard interupt
    except KeyboardInterrupt:
        selection = int(input("Input 3: "))
        if selection == 3:
            GPIO.output(22, True)
            print("exiting")
            sys.exit()
# GPIO.output(26, True) # the true is turning off the lamp on false is turning on
