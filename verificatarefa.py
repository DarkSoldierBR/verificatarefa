import pyautogui
import PIL.ImageOps
import time
from PIL import Image
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

materia = ''
atividades_total = 0
materias_total = 0
atividades_pendentes = '\n \n================================================\n \n'


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

    return text


def verify(materia):
    i = 300
    atividade = screenshot(430, i, 550, 50)
    global materias_total
    global atividades_total
    global atividades_pendentes

    if atividade == '':
        print('['+materia+'] Não há tarefas')
    elif 'Visualizado' in atividade or 'Nao entregue' in atividade:
        print('['+materia+'] Há tarefas pendentes')
        materias_total = materias_total + 1
        while 'Visualizado' in screenshot(430, i, 550, 50) or 'Nao entregue' in screenshot(430, i, 550, 50):
            atividade = screenshot(430, i, 550, 50)
            data = atividade[0:6]
            titulo = atividade[7:]
            atividades_total = atividades_total + 1

            atividades_pendentes = atividades_pendentes + '[Atividade] ['+materia+'] '+'['+data+'] '+titulo '\n'
            print('[Atividade] ['+materia+'] '+'['+data+'] '+titulo)
            i = i+50
    else:
        print('['+materia+'] Não há tarefas')


def run():
    i = 165
    p = 287
    limit = 0

    time.sleep(2)
    mouse_click(380, 150)
    while limit < 9:
        z = i+13
        i = i+47
        p = i+25
        time.sleep(1)
        mouse_click(145, i)
        materia = screenshot(153, z, 155, 50)
        mouse_click(139, p)
        mouse_click(878, 75)
        time.sleep(6)
        verify(materia)
        mouse_click(145, i)
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
        mouse_click(145, i)
        time.sleep(1)
        mouse_click(139, p)
        mouse_click(878, 75)
        time.sleep(5)
        verify(materia)
        mouse_click(145, i)
        limit = limit+1

    print(atividades_pendentes)
    if(atividades_total > 0):
        print('[TOTAL] Você tem '+str(atividades_total) +
              ' atividades em '+str(materias_total)+' matérias.')
    else:
        print("Parabêns! Você não tem tarefas pendentes")

    log_file = open("log.txt","w")
    log_file.write(atividades_pendentes)
    input("Pressione alguma tecla para sair")

run()