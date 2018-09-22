#! /usr/bin/env python3
# William Lamb
# 9/22/18
# williamplamb@gmail.com

#From pynput docs: https://pynput.readthedocs.io/en/latest/keyboard.html#monitoring-the-keyboard

from pynput import keyboard

print("Starting Program");

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        print("\nQuitting");
        quit();
