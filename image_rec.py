from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

while keyboard.is_pressed('q') == False:
    try:
        if pyautogui.locateOnScreen('sequence.png', region=(600,300,700,700), confidence=0.8) != None:
            print("I can see it")
        else:
            print("I am unable to see it")
    except pyautogui.ImageNotFoundException:
        print("I am unable to see it")
    time.sleep(0.5)
