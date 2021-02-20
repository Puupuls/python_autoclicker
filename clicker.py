# Running:
# python clicker.py [clicking interval]

from pynput.mouse import Button, Controller  # pip install pynput
from pynput import keyboard
from time import sleep

import sys

mouse = Controller()
paused = True
exit_loop = False
def on_press(key):
    try:
        if key.char == 'A':
            global paused
            paused = not paused
            if paused:
            	print('Pausing!')
            else:
            	print('Unpausing!')
        if key.char == 'Q':
            global exit_loop
            exit_loop = True
            print("Exiting!")
            sys.exit()
    except AttributeError:
        pass
        # print('special key {0} pressed'.format( key))
        
def on_release(key):
    # print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        pass
        #return False

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
try:
    interval = int(sys.argv[1])
except Exception as e:
    interval = 1

print(f'Interval {interval} seconds')
print(f'Press SHIFT+A to start or pause')
print(f'Press SHIFT+Q to exit')
while not exit_loop:
    if not paused:
        mouse.click(Button.left, 1)
    sleep(interval)
