from microbit import *

# There are 19 pins for your disposal, numbered 0-16 and 19-20.
# Pins 17 and 18 are not available.

while True:
    display.clear()
    display.scroll("Analog value: {}".format(pin0.read_analog()))
    display.clear()
    display.scroll("Digital value: {}".format(pin0.read_digital()))
    display.clear()
    sleep(5000)
