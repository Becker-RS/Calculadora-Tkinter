from tkinter import *
from tkinter import ttk

cor1 = "#1e1f1e" #preto
cor2 = "#feffff" #branco
cor3 = "#38576b" #azul
cor4 = "#ECEFF1" #cinza
cor5 = "#FFAB40" #laranja


janela =Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=cor1)


Frame_tela = Frame(janela, width=235, height=50,bg= cor3)
Frame_tela.grid(row=0, column=0)

Frame_base = Frame(janela, width=235, height=268,)
Frame_base.grid(row=1, column=0)

b_1 = Button(Frame_base, text="C", width=11,height=2)
b_1.place(x=0, y=0)

b_2 = Button(Frame_base, text="%", width=5,height=2)
b_2.place(x=90, y=0)

b_3 = Button(Frame_base, text="/", width=5,height=2)
b_3.place(x=177, y=0)

janela.mainloop()
