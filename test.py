import mss
import keyboard
import pyscreenshot as ImageGrab
import pyautogui
import PIL.ImageOps
import time
from PIL import Image
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from termcolor import colored, cprint

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def screenshot(left, top, width, height):
    image = pyautogui.screenshot(region=(left, top, width, height))
    inverted_image = PIL.ImageOps.invert(image)
    text = tess.image_to_string(inverted_image)

    inverted_image.show()

    #print("[SCREENSHOT TEXT]", text)

    print(bcolors.WARNING+text)

# i = 175
# z = i+20

# screenshot(153, z, 160, 30)

print('\033[93m Você tem tarefas')


print('asdasdnadadbasda')

print(colored('hello', 'red'), colored('world', 'green'))

#cprint('Hello, World!', 'green', 'on_red')

input("Pressione alguma tecla para sair")

