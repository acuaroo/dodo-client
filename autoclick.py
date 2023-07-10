# make every second 1 click, using pynput
import pynput as pyn

from pynput.keyboard import Key
from pynput.mouse import Button

from time import sleep

keyboard = pyn.keyboard.Controller()
mouse = pyn.mouse.Controller()

# autoclick 1 second in a loop
while True:
    mouse.click(Button.left, 1)
    sleep(1)
    