from tkinter import *
from tkinter import ttk

"""Cores utilizadas"""

cor1 = "#1e1f1e"  # preto
cor2 = "#feffff"  # branco
cor3 = "#38576b"  # azul
cor4 = "#ECEFF1"  # cinza
cor5 = "#FFAB40"  # laranja

"""configurações de tamanho e cor de Background"""

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=cor1)

"""Display da  Calculadora"""

Frame_tela = Frame(janela, width=235, height=50, bg=cor3)
Frame_tela.grid(row=0, column=0)

Frame_base = Frame(janela, width=235, height=268)
Frame_base.grid(row=1, column=0)

todos_valores = ""
valor_texto = StringVar()

"""Define valor de resultado no display"""


def display_valor(event):
    global todos_valores

    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)


app_scream = Label(Frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief="flat", anchor="e", bd=0,
                   justify=RIGHT, font=('Ivy 18 '), bg='#37474F', fg=cor2)
app_scream.place(x=0, y=0)

"""Calcular"""


def calcular():
    global todos_valores
    resultado = str(eval(todos_valores))
    valor_texto.set(resultado)
    todos_valores = ""


app_label = Label(Frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e",
                  justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

b_1 = Button(Frame_base, command=lambda: display_valor('%'), text="C", width=11, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(Frame_base, command=lambda: display_valor('%'), text="%", width=5, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(Frame_base, command=lambda: display_valor('/'), text="/", width=5, height=2, bg=cor5, fg=cor2,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(Frame_base, command=lambda: display_valor('7'), text="7", width=5, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(Frame_base, command=lambda: display_valor('8'), text="8", width=5, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(Frame_base, command=lambda: display_valor('9'), text="9", width=5, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)
b_7 = Button(Frame_base, command=lambda: display_valor('*'), text="*", width=5, height=2, bg=cor5, fg=cor2,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)

b_8 = Button(Frame_base, command=lambda: display_valor('4'), text="4", width=5, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(Frame_base, command=lambda: display_valor('5'), text="5", width=5, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(Frame_base, command=lambda: display_valor('6'), text="6", width=5, height=2, bg=cor4,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)
b_11 = Button(Frame_base, command=lambda: display_valor('-'), text="-", width=5, height=2, bg=cor5, fg=cor2,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)

b_12 = Button(Frame_base, command=lambda: display_valor('1'), text="1", width=5, height=2, bg=cor4,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(Frame_base, command=lambda: display_valor('2'), text="2", width=5, height=2, bg=cor4,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(Frame_base, command=lambda: display_valor('3'), text="3", width=5, height=2, bg=cor4,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)
b_15 = Button(Frame_base, command=lambda: display_valor('+'), text="+", width=5, height=2, bg=cor5, fg=cor2,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)

b_16 = Button(Frame_base, command=lambda: display_valor('0'), text="0", width=11, height=2, bg=cor4,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(Frame_base, command=lambda: display_valor('.'), text=".", width=5, height=2, bg=cor4,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)
b_18 = Button(Frame_base, command=lambda: display_valor('='), text="=", width=5, height=2, bg=cor5, fg=cor2,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)



janela.mainloop()
