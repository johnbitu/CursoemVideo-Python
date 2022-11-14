# BIBLIOTECAS
from tkinter import *
from tkinter import ttk
from tkinter.font import *


# CORES
azulescuro = '#38576b'
azulclaro = '#1f619c'
preto = '#000000'
laranja = '#e3971e'
branca = '#ffffff'


# GEOMETRIA
janela = Tk()
janela.title('Calculadora')
janela.geometry('209x332')
janela.resizable(0,0)
janela.config(bg=preto)


# VARIAVEIS
todos_valores = ''
valor_text = StringVar()


# ENTRADA DE VALORES
def input_valores(event):

    global todos_valores
    todos_valores = todos_valores + str(event)
    valor_text.set(todos_valores)


# CALCULOS
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_text.set(str(resultado))
    todos_valores = str(resultado)


# LIMPAR TELA
def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_text.set('')


# FRAMES
frame_tela = Frame(janela, width=235, height=50,bg=azulescuro)
frame_tela.grid(row=0,column=0)
frame_corpo = Frame(janela, width=235, height=280, bg=preto)
frame_corpo.grid(row=1,column=0)


# LABELS
valor_text = StringVar()
app_label = Label(frame_tela,textvariable=valor_text,font = 'Ivy 12 bold ',width=19,height=3,padx=7,relief= FLAT,anchor='e',justify=RIGHT,bg=azulescuro,activebackground=azulescuro,fg=branca,activeforeground=branca,).place(x=0,y=0)


######## BOTÕES ########

# OPERADORES
b_clean = Button(frame_corpo,command=limpar_tela,text='C',overrelief=RIDGE).place(x=2,y=2,width=102,height=54)
b_porcento = Button(frame_corpo,command = lambda: input_valores('%'),text='%',overrelief=RIDGE,bg=laranja,activebackground=laranja).place(x=106,y=2,width=50,height=54)
b_divisao = Button(frame_corpo,command = lambda: input_valores('/'),text='/',overrelief=RIDGE,bg=laranja,activebackground=laranja).place(x=158,y=2,width=50,height=54)
b_multiplicar = Button(frame_corpo,command = lambda: input_valores('*'),text='*',overrelief=RIDGE,bg=laranja,activebackground=laranja).place(x=158,y=58,width=50,height=54)
b_virgula = Button(frame_corpo,command = lambda: input_valores('.'),text=',',overrelief=RIDGE).place(x=106,y=226,width=50,height=54)
b_igual = Button(frame_corpo,command =calcular,text='=',overrelief=RIDGE,bg=laranja,activebackground=laranja).place(x=158,y=226,width=50,height=54)
b_subtracao = Button(frame_corpo,command = lambda: input_valores('-'),text='-',overrelief=RIDGE,bg=laranja,activebackground=laranja).place(x=158,y=114,width=50,height=54)
b_adicao = Button(frame_corpo,command = lambda: input_valores('+'),text='+',overrelief=RIDGE,bg=laranja,activebackground=laranja).place(x=158,y=170,width=50,height=54)


# NUMEROS
num9 = Button(frame_corpo,command = lambda: input_valores('9'),text='9',overrelief=RIDGE).place(x=106,y=58,width=50,height=54)
num8 = Button(frame_corpo,command = lambda: input_valores('8'),text='8',overrelief=RIDGE).place(x=54,y=58,width=50,height=54)
num7 = Button(frame_corpo,command = lambda: input_valores('7'),text='7',overrelief=RIDGE).place(x=2,y=58,width=50,height=54)  
num6 = Button(frame_corpo,command = lambda: input_valores('6'),text='6',overrelief=RIDGE).place(x=106,y=114,width=50,height=54)
num5 = Button(frame_corpo,command = lambda: input_valores('5'),text='5',overrelief=RIDGE).place(x=54,y=114,width=50,height=54)
num4 = Button(frame_corpo,command = lambda: input_valores('4'),text='4',overrelief=RIDGE).place(x=2,y=114,width=50,height=54) 
num3 = Button(frame_corpo,command = lambda: input_valores('3'),text='3',overrelief=RIDGE).place(x=106,y=170,width=50,height=54)
num2 = Button(frame_corpo,command = lambda: input_valores('2'),text='2',overrelief=RIDGE).place(x=54,y=170,width=50,height=54)
num1 = Button(frame_corpo,command = lambda: input_valores('1'),text='1',overrelief=RIDGE).place(x=2,y=170,width=50,height=54) 
num0 = Button(frame_corpo,command = lambda: input_valores('0'),text='0',overrelief=RIDGE).place(x=2,y=226,width=102,height=54)






janela.mainloop()