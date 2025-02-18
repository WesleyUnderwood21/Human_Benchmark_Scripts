from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#pyautogui.displayMousePosition()

#bottom left to top right snake way
#tile 1 X:  756 Y:  848
#tile 2 X:  966 Y:  870
#tile 3 X: 1167 Y:  854
#tile 4 X: 1149 Y:  653
#tile 5 X:  955 Y:  650
#tile 6 X:  768 Y:  653
#tile 7 X:  757 Y:  445
#tile 8 X:  956 Y:  466
#tile 9 X: 1151 Y:  455

#X:  344 Y:  561 RGB: (255, 255, 255)

#4.2 got 56

while pyautogui.pixel(344,561)[0] == 255:
    time.sleep(0.1)

time.sleep(0.5)

y = 1

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    Sequence = []

    while len(Sequence) != y and keyboard.is_pressed('w') == False:
        try:
            if pyautogui.locateOnScreen('sequence.png', region=(600,300,700,700), confidence=0.8) != None:
                n=0 
        except pyautogui.ImageNotFoundException:
            #print(len(Sequence))
            if pyautogui.pixel(756, 848)[0] == 255:
                Sequence.append(1)
                time.sleep(0.42)
            if pyautogui.pixel(966, 870)[0] == 255:
                Sequence.append(2)
                time.sleep(0.42)
            if pyautogui.pixel(1167, 854)[0] == 255:
                Sequence.append(3)
                time.sleep(0.42)
            if pyautogui.pixel(1149, 653)[0] == 255:
                Sequence.append(4)
                time.sleep(0.42)
            if pyautogui.pixel(955, 650)[0] == 255:
                Sequence.append(5)
                time.sleep(0.42)
            if pyautogui.pixel(768, 653)[0] == 255:
                Sequence.append(6)
                time.sleep(0.42)
            if pyautogui.pixel(757, 445)[0] == 255:
                Sequence.append(7)
                time.sleep(0.42)
            if pyautogui.pixel(956, 466)[0] == 255:
                Sequence.append(8)
                time.sleep(0.42)
            if pyautogui.pixel(1151, 455)[0] == 255:
                Sequence.append(9)
                time.sleep(0.42)
                    
    time.sleep(0.3)    
    print(len(Sequence))
    #print(Sequence)

    for x in Sequence:
        if x == 1:
            click(756, 848)
        elif x == 2:
            click(966, 870)
        elif x == 3:
            click(1167, 854)
        elif x == 4:
            click(1149, 653)
        elif x == 5:
            click(955, 650)
        elif x == 6:
            click(768, 653)
        elif x == 7:
            click(757, 445)
        elif x == 8:
            click(956, 466)
        elif x == 9:
            click(1151, 455)

    y += 1
    
    time.sleep(0.5)

