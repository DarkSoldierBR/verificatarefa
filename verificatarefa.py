import mss
import keyboard
import pyscreenshot as ImageGrab
import pyautogui
import PIL.ImageOps
import time
from PIL import Image
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

materia = ''
atividades_total = 0
materias_total = 0


def mouse_click(x, y):

    pyautogui.click(x, y)

    time.sleep(1)


def mouse_position():
    while True:
        print(ag.position())
        time.sleep(1)


def screenshot(left, top, width, height):
    image = pyautogui.screenshot(region=(left, top, width, height))
    inverted_image = PIL.ImageOps.invert(image)
    text = tess.image_to_string(inverted_image)
    #print("[SCREENSHOT TEXT]", text)

    return text


def verify(materia):
    i = 300
    atividade = screenshot(430, i, 550, 50)
    global materias_total
    global atividades_total

    if atividade == '':
        print('['+materia+'] Não há tarefas')
    elif 'Visualizado' in atividade or 'Nao entregue' in atividade:
        print('['+materia+'] Há tarefas pendentes')
        materias_total = materias_total + 1
        while 'Visualizado' in screenshot(430, i, 550, 50) or 'Nao entregue' in screenshot(430, i, 550, 50):
            atividades_total = atividades_total + 1
            print('[Atividade] ['+materia+']'+screenshot(430, i, 550, 50))
            i = i+50
    else:
        print('['+materia+'] Não há tarefas')


def main():
    i = 165
    p = 287
    limit = 0

    time.sleep(2)
    mouse_click(380, 150)

    while limit < 9:
        z = i+13
        i = i+47
        p = i+25
        materia = screenshot(153, z, 155, 50)
        time.sleep(1)
        mouse_click(95, i)
        mouse_click(139, p)
        mouse_click(878, 75)
        time.sleep(6)
        verify(materia)
        mouse_click(95, i)
        limit = limit+1

    # SCROLL 2 PARTE (ALTURA E EXPANSÃO MUDAM)
    i = 162
    limit = 0
    mouse_click(380, 525)

    while limit < 7:
        z = i+13
        i = i+47
        p = i+30
        materia = screenshot(153, z, 155, 50)
        time.sleep(1)
        mouse_click(95, i)
        time.sleep(1)
        mouse_click(139, p)
        mouse_click(878, 75)
        time.sleep(5)
        verify(materia)
        mouse_click(95, i)

        limit = limit+1

    if(atividades_total > 0):
        print('[TOTAL] Você tem '+str(atividades_total) +
              ' atividades em '+str(materias_total)+' matérias.')
    else:
        print("Parabêns! Você não tem tarefas pendentes")

    input("Pressione alguma tecla para sair")


main()
