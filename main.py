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

"""Display da  Calculadora"""

Frame_tela = Frame(janela, width=235, height=50,bg= cor3)
Frame_tela.grid(row=0, column=0)

Frame_base = Frame(janela, width=235, height=268,)
Frame_base.grid(row=1, column=0)

app_label = Label(Frame_tela, text="1234565789", width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
app_label.place(x=0,y=0)
 
b_1 = Button(Frame_base, text="C", width=11, height=2, bg=cor4,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(Frame_base, text="%", width=5, height=2, bg=cor4,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(Frame_base, text="/", width=5, height=2, bg=cor5, fg=cor1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)
 
b_4 = Button(Frame_base, text="7", width=5, height=2, bg=cor4,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(Frame_base, text="8", width=5, height=2, bg=cor4,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(Frame_base, text="9", width=5, height=2, bg=cor4,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)
b_7 = Button(Frame_base, text="*", width=5, height=2, bg=cor5, fg=cor1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)
 
b_8 = Button(Frame_base, text="4", width=5, height=2, bg=cor4,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(Frame_base, text="5", width=5, height=2, bg=cor4,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(Frame_base, text="6", width=5, height=2, bg=cor4,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)
b_11 = Button(Frame_base, text="-", width=5, height=2, bg=cor5, fg=cor1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)
 
b_12 = Button(Frame_base, text="1", width=5, height=2, bg=cor4,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(Frame_base, text="2", width=5, height=2, bg=cor4,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(Frame_base, text="3", width=5, height=2, bg=cor4,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)
b_15 = Button(Frame_base, text="+", width=5, height=2, bg=cor5, fg=cor1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)
 
b_16 = Button(Frame_base, text="0", width=11, height=2, bg=cor4,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(Frame_base, text=".", width=5, height=2, bg=cor4,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)
b_18 = Button(Frame_base, text="=", width=5, height=2, bg=cor5, fg=cor1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)


janela.mainloop()
