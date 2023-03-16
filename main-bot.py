import pynput as pyn 
import numpy as np

import random

from pynput.keyboard import Key
from pynput.mouse import Button

from time import sleep

keyboard = pyn.keyboard.Controller()
mouse = pyn.mouse.Controller()

#pet <font color="#DB63FF"><i>rescue shelter!</i></font>

phrases = ["amazing pets, come adopt some!", "get yourself a unicorn today!", "we have pets ranging from dogs to unicorns!", "best pet shop in the world :)", "come adopt a pet!", "adopt a pet!", "adopt one of our cute pets :)"]
phrase_time = (25, 35)
type_speed = 10

donate_phrases = ["omg thanks! enjoy your pet :)", "wow! enjoy your pet!", "omg thanks! do you like your pet?", "thanks! come again soon"]

# donate_location = {'top': 195, 'left': 10, 'width': 400, 'height': 20}
# donate_location2 = {'top': 195, 'left': 965, 'width': 400, 'height': 20}
# donate_location3 = {'top': 597, 'left': 965, 'width': 400, 'height': 20}

mouse_positions = {
    1: (100, 300),
    2: (1200, 700),
    3: (1200, 300),
}

donation_locations = {
    1: {'top': 195, 'left': 10, 'width': 400, 'height': 20},
    2: {'top': 195, 'left': 965, 'width': 400, 'height': 20},
    3: {'top': 597, 'left': 965, 'width': 400, 'height': 20},
}

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



def main_cycle():
    previous_amount = 0
    cycle = 0
    current_position = 1

    phrase_set = 0

    next_phrase = random.randint(*phrase_time)

    while True:
        current_position += 1

        if current_position > 3:
            current_position = 1

        mouse.position = mouse_positions[current_position]
        mouse.click(Button.left, 1)

        sleep(1)
        
        cycle += 1

        if cycle >= next_phrase:
            mouse.click(Button.left, 1)
            phrase_set += 1

            if phrase_set == 3:
                cycle = 0
                phrase_set = 0

                next_phrase = random.randint(*phrase_time)
                
            #cycle = 0
            
            phrase = random.choice(phrases)

            print(phrase)

            say(phrase)


sleep(1)
main_cycle()
