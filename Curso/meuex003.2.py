import tkinter
from tkinter import *
from tkinter import messagebox


class MinhaGUI:
    def __init__(self):
        # janela principal
        self.janela_principal = Tk()

        # botão
        self.botao = Button(self.janela_principal, text='Clique aqui', command=self.hello_world)

        # botão na janela principal
        self.botao.pack()

        mainloop()

    def hello_world(self):
        messagebox.showinfo(title='teste', message='não é um teste boy')
        tkinter.messagebox.askquestion(title=None, message='Can I get a kiss?')
        messagebox.showwarning(title=None, message='ah então tu é né, era só um teste boy')


gui = MinhaGUI()
