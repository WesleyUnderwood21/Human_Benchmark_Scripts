from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

sleep(2)

#Position X:  868 Y:  855 RGB: ( 75, 219, 106)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


while keyboard.is_pressed('q') == False:

        if pyautogui.pixel(868, 855)[0] == 75:
            click(868, 855)
