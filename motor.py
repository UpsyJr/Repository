import RPi.GPIO as GPIO
from time import sleep
import sys

# assigning motor pins
motor_pins = (17,18,27)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
# if we are defining more than one GPIO channel as I/O we have to use:
GPIO.setup(motor_pins, GPIO.OUT)

motor_direction = int(input("choose motor direction 1,2,3: "))
while True:
    try:
        if motor_direction == 1:
            print("MOTOR is running clock wise")
            GPIO.output(motor_pins, (GPIO.HIGH, GPIO.LOW, GPIO.LOW))
            sleep(0.02)
            GPIO.output(motor_pins, (GPIO.HIGH, GPIO.HIGH, GPIO.LOW))
            sleep(0.02)
            GPIO.output(motor_pins, (GPIO.LOW, GPIO.HIGH, GPIO.LOW))
            sleep(0.02)
        elif motor_direction == 2 :
            print("MOTOR is running anti-clock wise")
            GPIO.output(motor_pins, (GPIO.HIGH, GPIO.LOW, GPIO.LOW))
            sleep(0.02)
            GPIO.output(motor_pins, (GPIO.LOW, GPIO.LOW, GPIO.HIGH))
            sleep(0.02)
            GPIO.output(motor_pins, (GPIO.LOW, GPIO.HIGH, GPIO.LOW))
            sleep(0.02)

    # CTRL + C for keyboard interupt

    except KeyboardInterrupt:
        motor_direction = int(input("3? - Quit: "))

        if motor_direction == 3:
            print("Motor stopped")
            sys.exit(0)
