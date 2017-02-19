# Dalek voice

from microbit import *
import speech
import random

# pitch - how high or low the voice sounds (0 = high, 255 = Barry White)
# speed - how quickly the device talks (0 = impossible, 255 = bedtime story)
# mouth - how tight-lipped or overtly enunciating the voice sounds
#   (0 = ventriloquist?s dummy, 255 = Foghorn Leghorn)
# throat - how relaxed or tense is the tone of voice
#   (0 = falling apart, 255 = totally chilled)

dalekWords = ["EXTERMINATE", "WHERE, IS, DOCTOR", "ALARM", "DALEK"]
numberOfDalekWords = len(dalekWords)

display.show(Image.HAPPY)

while True:
    speech.say(dalekWords[random.randrange(numberOfDalekWords)], pitch=64, speed=192, mouth=200, throat=64)
    sleep(2000)
