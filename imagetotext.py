import pytesseract as tess 
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
import mss 
import time
import pyautogui as ag
import pyscreenshot as ImageGrab
import keyboard

text = ''
title = ''

def verify():
    if "Visualizado" or "Não entregue" in convert_text('teams_notas_shot.png'):
        verify = ("há tarefas pendentes")
    else:
        verify = ("Não há não tarefas pendentes")
   # print("[Verify]",verify)
    return verify
        
def screenshot(left,top,width,height,name):
    with mss.mss() as sct:
        monitor = { "left": left,"top": top,"width": width, "height": height}
        sct_img = sct.grab(monitor)
        output = name.format(**monitor)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    

def convert_text(name):
    img = Image.open(name)
   # print("[Screenshot] ",img)
    text = tess.image_to_string(img)
    #print("[TEXT]",text)

    return text


def mouse_position():
    while True:
        print(ag.position())
        time.sleep(1)

def mouse_click(x,y):
#    print(x,',',y)
    ag.click(x,y)
#    print(ag.position())    
    time.sleep(1)
    

def main():
    i=165
    p=287
    limit = 0
    
    while limit<9:  
        z=i+13
        i=i+47
        p=i+25
        screenshot(153,z,155,50,'title.png')
        time.sleep(1)
        mouse_click(95,i)
        time.sleep(1)
        mouse_click(139,p)
        mouse_click(878,75)
        time.sleep(5)
        screenshot(880,i,80,300,'teams_notas_shot.png')
        time.sleep(1)
        print('[Verify] Na matéria',convert_text('title.png'),verify())
        time.sleep(1)
        mouse_click(95,i)
        limit=limit+1
        
    limit = 0    
    while limit<6:
        ag.scroll(40)   

main()
