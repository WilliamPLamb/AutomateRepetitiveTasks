#! /usr/bin/env python3

import pyautogui as pag

from time import sleep

print("Press Ctrl-X to start recording")
print("Press Ctrl-X to stop recording")
print("Press Ctrl-V to start playback")
print("Press Ctrl-C to quit")


#print("Press Ctrl-X to start and stop recording")
#print("Press Ctrl-V to start playback")

#Start

try:
    while True:
        sleep(0.05)
except KeyboardInterrupt:
    print("\nStarting Recording")

#Record
#class to store data
class dataStor:
    waitTime = 0.0f
    x = 0
    y = 0
    duration = 0.0f
    action = ""
    button = ""
    message = ""

    def doAction(self):
        sleep(waitTime)
        if action == "":
        if action == "click":
            pag.click(x,y)
        if action == "rightClick":
            pag.moveTo(x,y)
            pag.click(button='right')
        if action == "moveTo":
            pag.moveTo(x,y,duration, pag.easeInElastic)
        if action == "press":
            pag.press(button)
        if action == "typewrite":
            pag.typewrite(message)

#array to store data
actions[]

#get position first time
x,y = pag.position()
action = dataStor()
action.x = x
action.y = y
action = "moveTo"

actions.append(action)

try:
    while True:
        #Make timer for wait

        appendActionFlag = false;
        action = dataStor()
        #check whether mouse has changed position
        xNew, yNew = pag.position()
        if x == xNew && y == yNew:
            #position hasn't changed, don't do anything
            action.x = x
            action.y = y
        else:
            #position has changed
            appendActionFlag = true;
            action.x = xNew
            action.y = yNew

        #Figure out how to register what events just happened and write to action


        sleep(0.05)
except KeyboardInterrupt:
    print("\nDone")

#Paste actions back
