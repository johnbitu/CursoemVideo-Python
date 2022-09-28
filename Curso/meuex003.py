from tkinter import *
from tkinter import messagebox
def _init_(self):
window = Tk()

self.botão = Button(window,text='clique aqui',command=self.hello_world)

self.botão.pack()

window.title('test')
window.geometry('800x400')

def hello_world(self):
    messagebox.showinfo('deu certo pohaaaaa!!!!')

gui = MinhaGUI()

window.mainloop()