from microbit import *

# Start calibrating
while not compass.is_calibrated():
    compass.clear_calibration()
    compass.calibrate()

# Try to keep the needle pointed in (roughly) the correct direction
while True:
    sleep(100)
    needle = ((15 - compass.heading()) // 30) % 12
    display.show(Image.ALL_CLOCKS[needle])