from PIL import Image
import PIL.ImageOps
import pyautogui
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import time


def screenshot(left, top, width, height):
    image = pyautogui.screenshot(region=(left, top, width, height))
    inverted_image = PIL.ImageOps.invert(image)

    text = tess.image_to_string(inverted_image)
    print("[TEXT]", text)

    return inverted_image


def main():
    i = 300
    z = 0
    while z < 3:
        time.sleep(2)
        screenshot(430, i, 550, 50).show()
        i = i+50
        z = z+1


main()
