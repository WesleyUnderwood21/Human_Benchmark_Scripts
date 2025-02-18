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

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    pic = pyautogui.screenshot(region=(280,280,1370,690))

    width, height = pic.size

    text = pytesseract.image_to_string(pic)

    numbers = ' '.join(re.findall('\d+', text))

    print(numbers)

    while pyautogui.pixel(1069,438)[0] != 255:

        time.sleep(0.1)
    
    pyautogui.write(numbers, interval=0.1)
    pyautogui.press('enter')
    pyautogui.press('enter')

    time.sleep(0.2)