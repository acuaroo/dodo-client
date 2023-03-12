import pynput as pyn 

from pynput.keyboard import Key
from pynput.mouse import Button
from pynput.mouse import Listener

from time import sleep

# format: [amount, "gamepass name"]
gamepasses = [
    [5, "dog"],
    [10, "cat"],
    [25, "fish"],
    [50, "tiger"],
    [100, "leopard"],
    [250, "monkey"],
    [500, "alligator"],
    [1000, "giraffe"],
    [2500, "octopus"],
    [5000, "unicorn"],
    [10000, "dragon"],
]

count = 0
gamepass_count = 0

keyboard = pyn.keyboard.Controller()
mouse = pyn.mouse.Controller()

simulate = [(470, 494), (1038, 621), (996, 724), (601, 428), (601, 427), (803, 511), (628, 966), (472, 662), (232, 470), (426, 453), (445, 511), (584, 671), (790, 221)]

input("[ press enter to begin, will stall for 5 seconds then start ]")

sleep(5)

type_events = {
    2: 1,
    11: 0,
    3: "wow! enjoy your pet :)",
}

for gamepass in gamepasses:
    gamepass_count += 1

    for position in simulate:
        count += 1

        mouse.position = position
        mouse.click(Button.left, 1)

        if count in type_events:
            event = type_events[count]

            final_text = ""

            if type(event) == int:
                final_text = str(gamepass[event])
            elif type(event) == str:
                final_text = event

            print(final_text)
            keyboard.type(final_text)
            

        print(count, position)

        sleep(1.7)
    
    count = 0

    sleep(1)