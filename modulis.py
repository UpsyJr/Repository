# Simple demo of continuous ADC conversion mode for channel 0 of the ADS1x15 ADC.
# Author: Tony DiCola
# License: Public Domain
import time
# Import the ADS1x15 module.
import Adafruit_ADS1x15
import adafruit_character_lcd.character_lcd as character_lcd
import sys
import RPi.GPIO as GPIO
import multiprocessing

ar = 3
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)


def r1():
    while ar > 1:
        global wtime, stime
        time.sleep(stime)
        GPIO.output(22, GPIO.LOW)
        time.sleep(mwtime)
        GPIO.output(22, GPIO.HIGH)


def r1stop():
    GPIO.output(22, GPIO.HIGH)


def prr():
    global ttime, proc, wtime, vid, rtime, mwtime, stime, rptime
    rptime = 0
    stime = 0
    rtime = 0
    wtime = 0
    mwtime = 0
    ttime = 0.011
    proc = 50
    vid = 1


prr()


def init():
    global mot
    mot = multiprocessing.Process(target=motor)
    mot.start()


def initproc():
    global mot
    mot = multiprocessing.Process(target=motor)
    mot.start()


# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()


# Use BCM GPIO references
# instead of physical pin numbers
def motorinit():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(True)  # Ignore warning for now

    # ENA PIN
    GPIO.setup(27, GPIO.OUT)
    GPIO.output(27, True)

    # STEP PIN
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(17, True)

    # DIR PIN
    GPIO.setup(18, GPIO.OUT)

    # Or create an ADS1015 ADC (12-bit) instance.
    # adc = Adafruit_ADS1x15.ADS1015()

    # Note you can change the I2C address from its default (0x48), and/or the I2C
    # bus by passing in these optional parameters:
    # adc = Adafruit_ADS1x15.ADS1015(address=0x49, busnum=1)

    # Choose a gain of 1 for reading voltages from 0 to 4.09V.
    # Or pick a different gain to change the range of voltages that are read:
    #  - 2/3 = +/-6.144V
    #  -   1 = +/-4.096V
    #  -   2 = +/-2.048V
    #  -   4 = +/-1.024V
    #  -   8 = +/-0.512V
    #  -  16 = +/-0.256V
    # See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
    GAIN = 1

    # Start continuous ADC conversions on channel 0 using the previously set gain
    # value.  Note you can also pass an optional data_rate parameter, see the simpletest.py
    # example and read_adc function for more infromation.
    adc.start_adc(0, gain=GAIN)


# Once continuous ADC conversions are started you can call get_last_result() to
# retrieve the latest result, orprr,init, stop_adc() to stop conversions.

# Note you can also call start_adc_difference() to take continuous differential
# readings.  See the read_adc_difference() function in differential.py for more
# information and parameter description.
i = 1


# Read channel 0 for 5 seconds and print out its values.
def ciklas():
    while i < 2:

        start = time.time()
        while (time.time() - start) <= 5.0:
            value = adc.get_last_result()
            # WARNING! If you try to read any other ADC channel during this continuous
            # conversion (like by calling read_adc again) it will disable the
            # continuous conversion!
            # Sleep for half a second.
            time.sleep(0.4)
            if (value > 30) and (value < 100):
                menu1()
            if (value > 9450) and (value < 10420):
                lcdmenu()


def ciklas1():
    global vid
    while i < 2:

        start = time.time()
        while (time.time() - start) <= 5.0:
            value = adc.get_last_result()
            # WARNING! If you try to read any other ADC channel during this continuous
            # conversion (like by calling read_adc again) it will disable the
            # continuous conversion!
            # Sleep for half a second.
            time.sleep(0.4)

            if (value > 30) and (value < 120):
                if vid == 0:
                    lcd.clear()
                    lcd.message('Mot. sustabdytas')
                    lcdmenu()
                mot.terminate()
                vid = vid - 1
                lcd.clear()
                lcd.message('Mot. Sustabdytas')
                time.sleep(1)
                lcdmenu()
            if (value > 15400) and (value < 16810):
                topmenu()
            if (value > 9450) and (value < 10420):
                lcdmenu2()
            if (value > 3900) and (value < 4500):
                topmenu()


def ciklas2():
    global vid
    while i < 2:

        start = time.time()
        while (time.time() - start) <= 5.0:
            value = adc.get_last_result()
            # WARNING! If you try to read any other ADC channel during this continuous
            # conversion (like by calling read_adc again) it will disable the
            # continuous conversion!
            # Sleep for half a second.
            time.sleep(0.4)
            if (value > 30) and (value < 120):
                if vid == 1:
                    lcd.clear()
                    lcd.message('Mot. Paleistas')
                    lcdmenu2()
                initproc()
                vid = vid + 1
                lcd.clear()
                lcd.message('Mot. Paleistas')
                time.sleep(1)
                lcdmenu2()
            if (value > 3900) and (value < 4500):
                lcdmenu()
            if (value > 9450) and (value < 10420):
                rieles()


def ciklasvp():
    global ttime, proc
    while i < 2:

        start = time.time()
        while (time.time() - start) <= 5.0:
            value = adc.get_last_result()
            # WARNING! If you try to read any other ADC channel during this continuous
            # conversion (like by calling read_adc again) it will disable the
            # continuous conversion!
            # Sleep for half a second.
            time.sleep(0.4)
            if (value > 3900) and (value < 4500):
                if (proc < 100):
                    mot.terminate()
                    proc += 5
                    ttime -= 0.001
                    time.sleep(0.1)
                    initproc()
                    menu1()
                lcd.clear()
                lcd.message("Pasiektos ribos!")
                time.sleep(1)
                menu1()
            if (value > 9450) and (value < 10520):
                if proc > 0:
                    mot.terminate()
                    proc -= 5
                    ttime += 0.001
                    time.sleep(0.1)
                    initproc()
                    menu1()
                lcd.clear()
                lcd.message('Pasiektos ribos!')
                time.sleep(1)
                menu1()
            if (value > 15700) and (value < 16810):
                topmenu()


def rieles():
    lcd.clear()
    lcd.message('Reles       >>\n')
    lcd.message('       ^         ')
    relciklas()


def rielmenu():
    lcd.clear()
    lcd.message('1 Rele.     >>\n')
    lcd.message('        v        ')
    relciklasmenu()


def rielmenu1a():
    lcd.clear()
    lcd.message('1Rel. D laik >>\n')
    lcd.message('        v        ')
    rielmenu1ac()


def rielmenu2():
    lcd.clear()
    lcd.message('2 Rele      >>\n')
    lcd.message('        v^       ')


# ciklas1()
def rielmenu1a1():
    lcd.clear()
    lcd.message('1Rel.P.laik >>\n')
    lcd.message('        v^       ')
    rielmenu1ap()


def rielmenu1a1m():
    lcd.clear()
    lcd.message('t= ')
    lcd.message(str(rtime))
    lcd.message('    <BACK')
    lcd.message('\nUP+        DOWN-')
    riel1ad()


def rielmenu1a1m1():
    lcd.clear()
    lcd.message('t= ')
    lcd.message(str(rptime))
    lcd.message('    <BACK')
    lcd.message('\nUP+        DOWN-')
    riel1ap()


def rielmenu1ap():
    while i < 2:

        start = time.time()
        while (time.time() - start) <= 5.0:
            value = adc.get_last_result()
            # WARNING! If you try to read any other ADC channel during this continuous
            # conversion (like by calling read_adc again) it will disable the
            # continuous conversion!
            # Sleep for half a second.
            time.sleep(0.4)

            if (value > 30) and (value < 120):
                rielmenu1a1m1()
            if (value > 15400) and (value < 16810):
                rielmenu1a1()


def riel1ap():
    global stime, rptime, r1p
    while i < 2:

        start = time.time()
        while (time.time() - start) <= 5.0:
            value = adc.get_last_result()
            # WARNING! If you try to read any other ADC channel during this continuous
            # conversion (like by calling read_adc again) it will disable the
            # continuous conversion!
            # Sleep for half a second.
            time.sleep(0.4)

            if (value > 3900) and (value < 4500):
                r1stop()
                r1p.terminate()
                rptime += 5
                stime += 5
                time.sleep(0.1)
                rinit()

                r1p.start()

                rielmenu1a1m()

            if (value > 9450) and (value < 10520):
                if rptime > 0 and stime > 0:
                    r1stop()
                    r1p.terminate()
                    rptime -= 5
                    stime -= 5
                    time.sleep(0.1)
                    rinit()

                    r1p.start()
                    rielmenu1a1m()
                lcd.clear()
                lcd.message('Pasiekta 0 riba!')
                time.sleep(1)
                rielmenu1a1m()
            if (value > 15400) and (value < 16810):
                rielmenu1a()


def riel1ad():
    global mwtime, rtime, r1p
    while i < 2:

        start = time.time()
        while (time.time() - start) <= 5.0:
            value = adc.get_last_result()
            # WARNING! If you try to read any other ADC channel during this continuous
            # conversion (like by calling read_adc again) it will disable the
            # continuous conversion!
            # Sleep for half a second.
            time.sleep(0.4)
            if (value > 3900) and (value < 4500):
                r1p.terminate()

                rtime += 5
                mwtime += 5
                time.sleep(0.1)

                rinit()
                r1p.start()
                rielmenu1a1m()

            if (value > 9450) and (value < 10520):
                if rtime > 0 and mwtime > 0:
                    r1p.terminate()
                    rtime -= 5
                    mwtime -= 5
                    time.sleep(0.1)

                    rinit()
                    r1p.start()
                    rielmenu1a1m()
                lcd.clear()
                lcd.message('Pasiekta 0 riba!')
                time.sleep(1)
                rielmenu1a1m()
            if (value > 15400) and (value < 16810):
                rielmenu1a()


def rinit():
    global r1p
    r1p = multiprocessing.Process(target=r1)


def rielmenu1ac():
    while i < 2:

        start = time.time()
        while (time.time() - start) <= 5.0:
            value = adc.get_last_result()
            # WARNING! If you try to read any other ADC channel during this continuous
            # conversion (like by calling read_adc again) it will disable the
            # continuous conversion!
            # Sleep for half a second.
            time.sleep(0.4)

            if (value > 30) and (value < 120):
                rielmenu1a1m()
            if (value > 15400) and (value < 16810):
                rielmenu()
            if (value > 9450) and (value < 10420):
                rielmenu1a1()


def relciklasmenu2():
    while i < 2:

        start = time.time()
        while (time.time() - start) <= 5.0:
            value = adc.get_last_result()
            # WARNING! If you try to read any other ADC channel during this continuous
            # conversion (like by calling read_adc again) it will disable the
            # continuous conversion!
            # Sleep for half a second.
            time.sleep(0.4)

            if (value > 3900) and (value < 4500):
                rielmenu()
            if (value > 30) and (value < 120):
                rielmenu2a()

            if (value > 9450) and (value < 10420):
                rielmenu3()
            if (value > 15400) and (value < 16810):
                rieles()


def relciklasmenu():
    while i < 2:

        start = time.time()
        while (time.time() - start) <= 5.0:
            value = adc.get_last_result()
            # WARNING! If you try to read any other ADC channel during this continuous
            # conversion (like by calling read_adc again) it will disable the
            # continuous conversion!
            # Sleep for half a second.
            time.sleep(0.4)

            if (value > 30) and (value < 120):
                rielmenu1a()
            if (value > 15400) and (value < 16810):
                rieles()
            if (value > 9450) and (value < 10420):
                rielmenu2()


def relciklas():
    while i < 2:

        start = time.time()
        while (time.time() - start) <= 5.0:
            value = adc.get_last_result()
            # WARNING! If you try to read any other ADC channel during this continuous
            # conversion (like by calling read_adc again) it will disable the
            # continuous conversion!
            # Sleep for half a second.
            time.sleep(0.4)

            if (value > 30) and (value < 120):
                rielmenu()

            if (value > 3900) and (value < 4500):
                topmenu()


def lcdmenu():
    lcd.clear()
    lcd.message('Stabdyti Mot. >>\n')
    lcd.message('       ^v        ')
    ciklas1()


def lcdmenu2():
    lcd.clear()
    lcd.message('Paleisti Mot. >>\n')
    lcd.message('        ^v       ')
    ciklas2()


def motor():
    motorinit()
    global ttime
    count = 1
    kartsuk = 1000
    while (count < kartsuk):
        GPIO.output(17, False)
        GPIO.output(17, True)
        time.sleep(ttime)


# Raspberry Pi pin configuration:
def lcdinit():
    lcd_rs = 25  # Note this might need to be changed to 21 for older revision Pi's.
    lcd_en = 24
    lcd_d4 = 16
    lcd_d5 = 12
    lcd_d6 = 21
    lcd_d7 = 20
    lcd_backlight = 4

    # Define LCD column and row size for 16x2 LCD.
    lcd_columns = 16
    lcd_rows = 2
    global lcd
    lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)


# Alternatively specify a 20x4 LCD.
# lcd_columns = 20
# lcd_rows    = 4


# prr()
# init()

# Initialize the LCD using the pins above.

def topmenu():
    lcd.clear()
    lcd.message('V.greitis     >>\n')
    lcd.message('        v        ')
    ciklas()


def menu1():
    lcd.clear()
    lcd.message('V=')
    lcd.message(str(proc))
    lcd.message('     < BACK')
    lcd.message('\nUP+        DOWN-')
    ciklasvp()


# Print a two line message
def start():
    global lcd
    lcdinit()

    lcd.message('Loading...')
    for x in range(0, 9):
        lcd.move_right()
        time.sleep(0.1)
    for x in range(0, 9):
        lcd.move_left()
        time.sleep(0.1)
    rinit()

    r1p.start()
    topmenu()


# topmenu()


# lcd.message("Sukiai ")
# lcd.message(str(kartsuk))
# lcd.message("\n")
# lcd.message("TarpasL ")
# lcd.message(str(ttime))


time.sleep(1)
init()

# Wait 5 seconds


# Stop continuous conversion.  After this point you can't get data from get_last_result!
