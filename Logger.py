#! /usr/bin/env python3
# William Lamb
# 9/22/18
# williamplamb@gmail.com

#######################################
# Define imports

# import pyautogui as pag
from pynput import keyboard
from pynput import mouse
# from time import sleep

#######################################
# Define functions

# DEBUG boolean for testing
debug = bool(False);

# Boolean to send log data or not
logging = bool(False);

# Boolean to flag quit
quitFlag = bool(False);

# Array to hold currently-pressed keys
keysPressed = [];

# Mouse logger
def on_move(x, y):
    # Check if keys to quit have been pressed
    checkQuit();
    if(quitFlag):
        return False;
    if(logging):
        print('Pointer moved to {0}'.format((x, y)));

def on_click(x, y, button, pressed):
    # Check if keys to quit have been pressed
    checkQuit();
    if(quitFlag):
        return False;
    if(logging):
        print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)));
        # Original code to stop mouse logger
        # if not pressed:
        #     # Stop listener
        #     return False;

def on_scroll(x, y, dx, dy):
    # Check if keys to quit have been pressed
    checkQuit();
    if(quitFlag):
        return False;
    if(logging):
        print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)));

# Keyboard logger
# Check to turn logging on/off
def checkLogging():
    if(keyboard.Key.ctrl in keysPressed and 'x' in keysPressed):
        global logging; # Need global keyword before assignment
        logging = not logging;
        if logging:
            print("Logging\n");
        else:
            print("Not Logging\n");

def checkQuit():
    if(keyboard.Key.ctrl in keysPressed and 'c' in keysPressed):
        global quitFlag;
        quitFlag = True;
        # print("quitFlag triggered\n")


def on_press(key):
    # Add key to pressed list
    try: # In case key is alphanumeric
        keysPressed.append(key.char);
    except AttributeError: # In case key is special
        keysPressed.append(key);

    # Check whether to turn on/off logging
    checkLogging();
    # Check whether to quit or not
    checkQuit();
    if(quitFlag):
        return False;

    # DEBUG: look at keysPressed list
    if(debug):
        print("keysPressed length: ");
        print(len(keysPressed));
        print("\n");
        for item in keysPressed:
            print("keysPressed: ");
            print(item);
            print("type: ");
            print(type(item));
        print("\n");
    # endDebug
    # TODO add checkLogging function in
    # Send key to log
    if(logging):
        try:
            print('alphanumeric key {0} pressed'.format(key.char));
        except AttributeError:
            print('special key {0} pressed'.format(key));

def on_release(key):
    # Remove key from pressed list
    global keysPressed; # Need global because assignment would mistake for local variable of same name
    try: # In case key is alphanumeric
        keysPressed = list(filter(lambda a: a != key.char, keysPressed));
    except AttributeError: # In case key is special
        keysPressed = list(filter(lambda a: a != key, keysPressed));
    # DEBUG: look at keysPressed list
    if(debug):
        print("keysPressed length: ");
        print(len(keysPressed));
        print("\n");
        for item in keysPressed:
            print("keysPressed: ");
            print(item);
        print("\n");
    # endDebug
    if(logging):
        print('{0} released'.format(key));
        # Original code to stop keyboard logger
        # if key == keyboard.Key.esc:
        #     # Stop listener
        #     return False;


#######################################
# Start program

# Instructions

print("Press Ctrl-X to start logging")
print("Press Ctrl-X to stop logging")
print("Press Ctrl-V to start playback")
print("Press Ctrl-C to quit at any time")

 # If I don't want to break formatting then I should use contextlib.ExitStack as seen here: https://stackoverflow.com/questions/31039022/python-multi-line-with-statement
# Construct keyboard and mouse listeners
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as kListener, mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as mListener:
    # Log with keyboard interrupt as exception
    try:
        print("Listeners Started")
        kListener.join();
        mListener.join();

        # while True:
        #     sleep(0.05);
        #     if()

    except KeyboardInterrupt:
        print("\nExiting Program");
        quit();

# Playback

#######################################




#######################################
#######################################
#######################################
# Old code...useful?

#Record
#class to store data
# class dataStor:
#     waitTime = 0.0f
#     x = 0
#     y = 0
#     duration = 0.0f
#     action = ""
#     button = ""
#     message = ""
#
#     def doAction(self):
#         sleep(waitTime)
#         if action == "":
#         if action == "click":
#             pag.click(x,y)
#         if action == "rightClick":
#             pag.moveTo(x,y)
#             pag.click(button='right')
#         if action == "moveTo":
#             pag.moveTo(x,y,duration, pag.easeInElastic)
#         if action == "press":
#             pag.press(button)
#         if action == "typewrite":
#             pag.typewrite(message)
#
# #array to store data
# actions[]
#
# #get position first time
# x,y = pag.position()
# action = dataStor()
# action.x = x
# action.y = y
# action = "moveTo"
#
# actions.append(action)
#
# try:
#     while True:
#         #Make timer for wait
#
#         appendActionFlag = false;
#         action = dataStor()
#         #check whether mouse has changed position
#         xNew, yNew = pag.position()
#         if x == xNew && y == yNew:
#             #position hasn't changed, don't do anything
#             action.x = x
#             action.y = y
#         else:
#             #position has changed
#             appendActionFlag = true;
#             action.x = xNew
#             action.y = yNew
#
#         #Figure out how to register what events just happened and write to action
#
#
#         sleep(0.05)
# except KeyboardInterrupt:
#     print("\nDone")
#
# #Paste actions back
