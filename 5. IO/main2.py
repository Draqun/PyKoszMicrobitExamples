from microbit import *

# There are 19 pins for your disposal, numbered 0-16 and 19-20.
# Pins 17 and 18 are not available.
# For more look https://microbit-micropython.readthedocs.io/en/latest/pin.html

pin1.write_analog(15)
pin2.write_analog(650)

display.clear()

while True:
    if pin0.read_analog() <= 1:
        display.scroll("1")
    elif pin0.read_analog() > 1 and pin0.read_analog() <= 250:
        display.scroll("2")
    elif pin0.read_analog() > 250 and pin0.read_analog() <= 500:
        display.scroll("3")
    elif pin0.read_analog() > 500 and pin0.read_analog() <= 750:
        display.scroll("4")
    elif pin0.read_analog() > 750 and pin0.read_analog() <= 1023:
        display.scroll("5")
    else:
        display.scroll("Unknown")
    sleep(1000)
