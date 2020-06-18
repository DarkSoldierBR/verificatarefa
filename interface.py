from tkinter import *
import tkinter.scrolledtext as scrolledtext
from verificatarefa import run
root = Tk()



class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        # Tilulo | Seção 1
        container1 = Frame(master, borderwidth=2, relief="groove")
        container1.pack(fill=X)

        text1 = Label(container1, text="Verifica Tarefa")
        text1.configure(font=("Times New Roman", 15, "bold"))
        text1.pack()


        #Botões | Seção 2
        container2 = Frame(master)
        container2.pack(ipadx=10)

        button_verify = Button(container2,text="Verificar",command=run);
        button_verify.pack(side=RIGHT,pady=10)

        button_stop = Button(container2,text="Parar")
        button_stop.pack(side=LEFT,pady=10)

        #ScrolledTexts | Seção 3
        container3 = Frame(master, borderwidth=2, relief="groove",width=40)
        container3.pack(fill=BOTH)

        text=scrolledtext.ScrolledText(container3)
        text['font']=('consolas', '12')
        text.pack(side=LEFT)

        atividades=scrolledtext.ScrolledText(container3)
        atividades['font']=('consolas', '12')
        atividades.pack(side=RIGHT)


        #text.insert

window_height=400
window_width=350

screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()

x_cordinate=int((screen_width/2) - (window_width/2))
y_cordinate=int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width,
              window_height, x_cordinate, y_cordinate))

Application(root)
root.title("Verifica Tarefa")
root.resizable(False, False)
root.mainloop()
