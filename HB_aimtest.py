from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#Color of center: (149, 195, 232)

while keyboard.is_pressed('q') == False:

    pic = pyautogui.screenshot(region=(280,280,1370,690))

    width, height = pic.size

    for x in range(0,width,30):
        for y in range(0,height,30):

            r,g,b = pic.getpixel((x,y))

            if g == 195:
                click(x+280,y+280)
                time.sleep(0.001)
                break
