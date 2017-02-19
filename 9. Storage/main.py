# Install microfs to get repoert file
# https://microfs.readthedocs.io/en/latest/
from microbit import *
import speech
import os
import random

# Creating basic dictionary od Dalek words when not exist
if not "dalek_dictionary.txt" in os.listdir():
    # display.scroll("Cannot find Dalek dictionary")
    with open("dalek_dictionary.txt", "w") as f:
        f.write("EXTERMINATE!\n")
        f.write("WHERE, IS, DOCTOR\n")
        f.write("DOCTOR!\n")
        f.write("ALARM\n")
        f.write("DAHLEK")

# Dalek has waking up! Run! Run! Run!
display.scroll("Dalek's waking up")

# Initialize dictionary
dalekDictionary = []

# Read words from file
with open("dalek_dictionary.txt", "r") as f:
    dalekDictionary.extend(
        [word for word in f.read().split("\n") if len(word) > 0])

# Get dictionary size
dalekDictionarySize = len(dalekDictionary)

try:
    # Try open file for report
    with open("dalek_report.txt", "w") as f:
        # Get delta time beetwen code start and Dalek work
        deltaTime = running_time()
        while running_time() < 30000 + deltaTime:  # Work for 30s
            # Say somethink from dalek dictionary
            word = dalekDictionary[random.randrange(dalekDictionarySize)]
            speech.say(word)
            # Report what Dalek said
            f.write("{}: Dalek said: {}\n".format(running_time(), word))
            sleep(1000)
except BaseException as e:
    display.scroll(str(e))
    speech.say("ERROR!, ERROR!, ERROR!")
