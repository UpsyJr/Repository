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
            for index in range(0,10):
                GPIO.output(22, True)
                sleep(5)
                GPIO.output(22,False)
                sleep(3)
        elif selection == 2:
            for index in range(0,10):
                GPIO.output(22, False)
                sleep(5)
                GPIO.output(22,True)
                sleep(5)
        elif selection == 4:
            GPIO.output(22,True)
            sleep(10)
            GPIO.output(22,False)
            sleep(3)
                # ctrl + c for keyboard interupt
    except KeyboardInterrupt:
        selection = int(input("Input 3: "))
        if selection == 3:
            print("exiting")
            sys.exit()
# GPIO.output(26, True) # the true is turning the lamp on false is off


