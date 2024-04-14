from tkinter import *
from tkinter import ttk

cor1 = "#1e1f1e" #preto
cor2 = "#feffff" #branco
cor3 = "#38576b" #azul
cor4 = "#ECEFF1" #cinza
cor5 = "#FFAB40" #Laranja




janela =Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=cor1)


Frame_tela = Frame(janela, width=235, height=50,)
Frame_tela.grid(row=0, column=0)

janela.mainloop()
