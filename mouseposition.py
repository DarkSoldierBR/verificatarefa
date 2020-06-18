import pyautogui
import time

def mouse_position():
    while True:
        print(pyautogui.position())
        time.sleep(1)

mouse_position()