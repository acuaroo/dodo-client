import pynput as pyn 
import pytesseract as pytes
import numpy as np

import random
import mss
import re

from pynput.keyboard import Key
from pynput.mouse import Button

from time import sleep

keyboard = pyn.keyboard.Controller()
mouse = pyn.mouse.Controller()

phrases = ["amazing pets, come buy some!", "get yourself a unicorn today!", "we have pets ranging from dogs to unicorns!", "best pet shop in the world :)", "come buy a pet!", "buy a pet!", "adopt one of our cute pets :)"]
phrase_time = (15, 25)
type_speed = 10

donate_phrases = ["omg thanks! enjoy your pet :)", "wow! enjoy your pet!", "omg thanks! do you like your pet?", "thanks! come again soon"]
donate_location = {'top': 310, 'left': 10, 'width': 600, 'height': 20}

username = "dull_dude32"
other_keyword = "tipped"

tesseract_location = open("assets/tesseract_path", "r").read()
tesseract_location = r'{}'.format(tesseract_location)

pytes.pytesseract.tesseract_cmd = tesseract_location

def say(message):
    sleep(len(message) / type_speed)

    keyboard.press("/")
    sleep(0.1)
    keyboard.release("/")

    keyboard.type(message)
    sleep(0.05)

    keyboard.press(Key.enter)
    sleep(0.1)
    keyboard.release(Key.enter)

def wiggle(duration):
    for i in range(duration):
        keyboard.press("a")
        sleep(0.1)
        keyboard.release("a")

        keyboard.press("d")
        sleep(0.1)
        keyboard.release("d")

def look_for_donations():
    with mss.mss() as sct:
        im = np.asarray(sct.grab(donate_location))
        text = pytes.image_to_string(im)

        if username in text and other_keyword in text:
            return True
        else:
            return False


def main_cycle():
    previous_amount = 0
    cycle = 0
    next_phrase = random.randint(*phrase_time)

    while True:
        sleep(1)
        cycle += 1

        if look_for_donations():
            phrase = random.choice(donate_phrases)
            print(phrase)
            say(phrase)

            sleep(random.randint(4, 8))
            sleep(10)

        if cycle >= next_phrase:
            mouse.click(Button.left, 1)
            cycle = 0

            next_phrase = random.randint(*phrase_time)
            phrase = random.choice(phrases)
            print(phrase)

            say(phrase)


sleep(1)
main_cycle()
