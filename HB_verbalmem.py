from pyautogui import *
import pyautogui
import pytesseract
import re
import time
import keyboard
import random
import win32api, win32con

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\clano_kvwtbnf\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

time.sleep(2)

#seen = X:  849 Y:  727
#new  = X: 1046 Y:  720

num = 0
list = []

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

pic = pyautogui.screenshot(region=(450,510,950,150))

text = pytesseract.image_to_string(pic)

list.append(text)
click(1046,720)

time.sleep(0.01)

while keyboard.is_pressed('q') == False:

    pic = pyautogui.screenshot(region=(450,510,950,150))

    text = pytesseract.image_to_string(pic)

    for x in list:
        if x == text:
            click(849,727)
            num = 1
            break

    if num == 0:
        list.append(text)
        click(1046,720)

    num = 0

    time.sleep(0.01)
