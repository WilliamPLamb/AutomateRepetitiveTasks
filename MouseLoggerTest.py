#! /usr/bin/env python3
# William Lamb
# 9/22/18
# williamplamb@gmail.com

# From pynput docs: https://pynput.readthedocs.io/en/latest/keyboard.html#monitoring-the-keyboard

from pynput import mouse

# Function Definitions

def on_move(x, y):
    print('Pointer moved to {0}'.format((x, y)));

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)));
    if not pressed:
        # Stop listener
        return False;

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)));

# Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as mouseListener:
    try:
        print("Starting program")
        mouseListener.join();
    except KeyboardInterrupt:
        print("\nExiting Program");
        quit();
