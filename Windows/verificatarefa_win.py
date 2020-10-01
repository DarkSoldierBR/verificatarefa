import time
import pyautogui
import PIL.ImageOps
import pyautogui as ag
import time
from PIL import Image
import pytesseract as tess
import re
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

materia = ''
atividades_total = 0
materias_total = 0
atividades_pendentes = '\n \n================================================\n \n'

prints=0

def mouse_click(x, y):
    pyautogui.click(x, y)

def mouse_position():
    while True:
        print(ag.position())
        time.sleep(1)


def screenshot(left, top, width, height):
    global prints
    image = pyautogui.screenshot(region=(left, top, width, height))
    inverted_image = PIL.ImageOps.invert(image)
    prints=prints+1
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
            print('atividade: '+atividade)
            data_check = re.findall(r'\d+', str(atividade[0:6]))
            data_check=len(data_check)

            if(data_check>1):
                data = atividade[0:6]
                titulo = atividade[7:]
            else:
                data = atividade[0:4]
                titulo = atividade[5:]
            atividades_total = atividades_total + 1
            atividades_pendentes = atividades_pendentes + '[Atividade] ['+materia+'] '+'['+data+'] '+titulo+'\n'
            print('[Atividade] ['+materia+'] '+'['+data+'] '+titulo)
            i = i+50
    else:
        print('['+materia+'] Não há tarefas')


def run():
    inicio = time.time()
    i = 263 #Parametro inical matéria
    limit = 0

    input("Pressione alguma tecla para iniciar")
    time.sleep(1)
    while limit < 9:     
        z = i+13 #Parametro print Matéria
        i = i+47 #Parametro click da Matéria
        p = i+25 #Parametro click do canal
        mouse_click(145, i)
        mouse_click(139, p)
        time.sleep(2)
        mouse_click(878, 75)
        time.sleep(6)
        materia = screenshot(153, z, 155, 50)
        verify(materia)
        mouse_click(145, i)
        limit = limit+1

    # SCROLL 2 PARTE (ALTURA E EXPANSÃO MUDAM)
    i = 103 #Parametro inical matéria
    limit = 0
    mouse_click(380, 525) #Click Scroll

    while limit < 7:
        z = i+13 #Parametro print Matéria
        i = i+47 #Parametro click da Matéria
        p = i+30 #Parametro click do canal
        mouse_click(145, i)
        mouse_click(139, p)
        time.sleep(2)
        mouse_click(878, 75)
        time.sleep(6)
        materia = screenshot(153, z, 155, 50)
        verify(materia)
        mouse_click(145, i)
        limit = limit+1

    print(atividades_pendentes)
    if(atividades_total > 0):
        print('[TOTAL] Você tem '+str(atividades_total) +
              ' atividades em '+str(materias_total)+' matérias.')
    else:
        print("Parabêns! Você não tem tarefas pendentes")
    print("Total de screenshots tiradas: "+str(prints))
    fim = time.time()
    total = (fim-inicio)
    total= str(total)
    total = total[0:6]
    tempominutos = (float(total))/60
    tempominutos=str(tempominutos)[0:4]
    print("Tempo de execução: " +tempominutos+" minutos " +"("+total+" segundos)")
    input("Pressione alguma tecla para sair")

run()
#mouse_position()
log_file = open("log.txt","w")
log_file.write(atividades_pendentes)