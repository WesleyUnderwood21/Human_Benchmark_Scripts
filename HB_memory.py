from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import numpy as np
import cv2

#region until level 105=(650,350,600,600)

square = 'big_square.png'
template = cv2.imread(square)
width, height, _ = template.shape

y = 1

while pyautogui.pixel(1042,630)[0] == 255:
    time.sleep(0.1)

time.sleep(1)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


while keyboard.is_pressed('q') == False:

    if y < 105:
        pic = pyautogui.screenshot(region=(650,350,600,600))
    else:
        pic = pyautogui.screenshot(region=(640,320,620,660))
        
    pic.save(r"C:\Users\clano_kvwtbnf\Desktop\python fun\memory.png")
    memory = 'memory.png'

    image = cv2.imread(memory)

    print(template.size)

    res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

    match_locations = np.where(res >= 0.8)

    #print(match_locations)

    xy_coordinates = [(x,y) for y, x in zip(*match_locations)]

    while xy_coordinates == [] and keyboard.is_pressed('w') == False:
        old_width = int(template.shape[1])
        old_height = int(template.shape[0])
        
        new_width = int(template.shape[1] * 0.999)
        new_height = int(template.shape[0] * 0.999)

        change_width = old_width - new_width
        change_height = old_height - new_height

        a = change_width / 2
        b = change_height / 2

        new_width += round(a)
        new_height += round(b)

        template = cv2.resize(template, (new_width, new_height), interpolation=cv2.INTER_AREA)

        res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

        match_locations = np.where(res >= 0.8)

        print(template.size)

        xy_coordinates = [(x,y) for y, x in zip(*match_locations)]

    print(len(xy_coordinates))

    time.sleep(1.5)

    for x, y in xy_coordinates:
        click(660+x, 360+y)

    y += 1
        
    time.sleep(2.5)
