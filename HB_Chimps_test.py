from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import numpy as np
import cv2
import pytesseract
import re

#region=(300,230,1300,750)

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\clano_kvwtbnf\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

max = 4

while pyautogui.pixel(1072,632)[0] == 255:
    time.sleep(0.1)

time.sleep(0.1)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def find_number_pos(max_num):
    num_pos = {}

    screenshot = pyautogui.screenshot(region=(300,230,1300,750))
    screenshot_np = np.array(screenshot)
    screenshot_cv2 = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)
        
    gray = cv2.cvtColor(screenshot_cv2, cv2.COLOR_BGR2GRAY)
    # Apply thresholding
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

    pic = thresh

    cv2.imwrite(r"C:\Users\clano_kvwtbnf\Desktop\python fun\chimps.png", pic)

    #text = pytesseract.image_to_string(pic, config='--psm 6')

    for number in range(1, max_num + 1):
        #config1 = '--psm 6 -c tessedit_char_whitelist=0123456789'
        data = pytesseract.image_to_data(pic, config='--psm 6', output_type=pytesseract.Output.DICT)

        #print(text)
        #print(data)

        for i, text in enumerate(data['text']):
            if text == str(number):
                x, y = data['left'][i], data['top'][i]
                num_pos[number] = (x, y)
                break  # Assuming only one occurrence of each number is present

    return num_pos



while keyboard.is_pressed('q') == False:

    for i, (j, k) in find_number_pos(max).items():
        print(i, j, k)
        click(300+j, 230+k)
        time.sleep(0.25)

    time.sleep(0.1)

    click(952,808)

    time.sleep(0.1)

    max += 1

    
