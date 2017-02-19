from microbit import *

while True:
    display.clear()
    sleep(100)
    if button_a.is_pressed() and not button_b.is_pressed():
        display.scroll("A is pressed")
    elif button_b.is_pressed() and not button_a.is_pressed():
        display.scroll("B is pressed")
    elif button_a.is_pressed() and button_b.is_pressed():
        display.scroll("Both buttons are pressed")
    else:
         display.scroll("Press any button")
            