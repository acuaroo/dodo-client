import pynput as pyn 

from pynput.keyboard import Key
from pynput.mouse import Button
from pynput.mouse import Listener

from time import sleep

# format: [amount, "gamepass name"]
gamepasses = [
    [75, "75 robux"],
    [150, "sus"],
    [250, "sus"],
    [500, "sus"],
    [1000, "sus"],
    [2000, "sus"],
    [5000, "sus"],
    [10000, "sus"],
    [50000, "sus"],
    [100000, "sus"],
    [200000, "sus"],
    [1000000, "sus"],
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
    3: "wow! enjoy your food :)",
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

        sleep(1.8)
    
    count = 0

    sleep(1)