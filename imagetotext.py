import mss
import keyboard
import pyscreenshot as ImageGrab
import pyautogui as ag
import time
from PIL import Image
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

resposta = ""
text = ''
title = ''
resultado = ''


def mouse_click(x, y):
    #    print(x,',',y)
    ag.click(x, y)
#    print(ag.position())
    time.sleep(1)


def mouse_position():
    while True:
        print(ag.position())
        time.sleep(1)


def screenshot(left, top, width, height, name):
    with mss.mss() as sct:
        monitor = {"left": left, "top": top, "width": width, "height": height}
        sct_img = sct.grab(monitor)
        output = name.format(**monitor)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)


def convert_text(name):
    img = Image.open(name)
   # print("[Screenshot] ",img)
    text = tess.image_to_string(img)
    print("[TEXT]", text)

    return text


def verify():
    result_conversion = convert_text('teams_notas_shot.png')
    print('result_conversion'+result_conversion)

    if 'Visualizado' in result_conversion:
        verify = (" há tarefas pendentes")
    elif 'Nao entregue' in result_conversion:
        verify = (" há tarefas pendentes")
    else:
         verify = (" não há não tarefas pendentes")

    print("[Verify]", verify)

    return verify


def main():
    i = 165
    p = 287
    limit = 0
    mouse_click(380, 150)

    while limit < 9:
        z = i+13
        i = i+47
        p = i+25
        screenshot(153, z, 155, 50, 'title.png')
        time.sleep(1)
        mouse_click(95, i)
        time.sleep(1)
        mouse_click(139, p)
        mouse_click(878, 75)
        time.sleep(5)
        screenshot(880, 300, 120, 300, 'teams_notas_shot.png')
        time.sleep(1)
        resposta = '[Verify] Na matéria ' + \
            convert_text('title.png')+verify()+'\n'
        print('[RESULTADO]', resposta)
        resultado =+ resposta
        time.sleep(1)
        mouse_click(95, i)
        limit = limit+1

    # SCROLL 2 PARTE (ALTURA E EXPANSÃO MUDAM)
    i = 162
    limit = 0
    mouse_click(380, 525)

    while limit < 7:
        z = i+13
        i = i+47
        screenshot(153, z, 155, 50, 'title.png')
        time.sleep(1)
        mouse_click(95, i)
        time.sleep(1)
        mouse_click(139, i)
        mouse_click(878, 75)
        time.sleep(5)
        screenshot(880, 300, 120, 300, 'teams_notas_shot.png')
        time.sleep(1)
        resposta = '[Verify] Na matéria ' + \
            convert_text('title.png')+verify()+'\n'
        print('[RESULTADO]', resposta)
        resultado = resultado + resposta
        time.sleep(1)
        mouse_click(95, i)

        limit = limit+1

    with open("Output.txt", "w") as text_file:
        text_file.write(str(resultado))


main()
# mouse_position()
