from microbit import *

own_image = Image(
    "05050:"
    "05050:"
    "00500:"
    "50005:"
    "05550"
)

while True:
    display.clear()
    display.scroll("TeXt")
    sleep(2000)
    display.clear()
    display.show(Image.HAPPY)
    sleep(2000)
    display.clear()
    display.show(own_image)
    sleep(2000)
