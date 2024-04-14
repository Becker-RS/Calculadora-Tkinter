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

b_1 = Button(Frame_base, text="C", width=11,height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(Frame_base, text="%", width=5,height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_2.place(x=118, y=0)

b_3 = Button(Frame_base, text="/", width=5,height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)


b_4 = Button(Frame_base, text="7", width=5,height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_4.place(x=0, y=52)

b_5 = Button(Frame_base, text="8", width=5,height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)

b_6 = Button(Frame_base, text="9", width=5,height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)

b_7 = Button(Frame_base, text="*", width=5,height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)

janela.mainloop()
