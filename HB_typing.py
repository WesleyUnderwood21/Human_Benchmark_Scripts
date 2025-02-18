from pyautogui import *
import pyautogui
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import re
import io
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

    pic = pyautogui.screenshot(region=(240,540,1430,280))

    pic = pic.convert('L')

    pic = pic.filter(ImageFilter.SHARPEN)

    enhancer = ImageEnhance.Contrast(pic)
    pic = enhancer.enhance(2)

    width, height = pic.size

    text = pytesseract.image_to_string(pic)

    text = text.replace('\n', ' ')

    text[0] == ''

    #text[len(text)-1] == ''

    print(text)
    
    pyautogui.write(text, interval=0.01)

    time.sleep(3)
