from tkinter import *
from centralizarfunction import centralizar

janela = Tk()
janela.title('Inserir Bulas')
janela.resizable(width=0, height=0)
janela.iconbitmap(default='icone.ico')
janela.config(background='#626464')
centralizar(350,312,janela)

nomer = Entry(janela, bg='white',font=('Calibri', 11), justify=LEFT)
nomer.place(width=145,height=24,x=120,y=4)

entradanome = Entry(janela, bg='white',font=('Calibri', 11), justify=LEFT)
entradanome.place(width=265,height=24,x=30,y=55)

entradanome2 = Entry(janela, bg='white',font=('Calibri', 11), justify=LEFT)
entradanome2.place(width=265,height=24,x=30,y=105)

entradanome3 = Entry(janela, bg='white',font=('Calibri', 11), justify=LEFT)
entradanome3.place(width=265,height=24,x=30,y=155)

entradanome4 = Entry(janela, bg='white',font=('Calibri', 11), justify=LEFT)
entradanome4.place(width=265,height=24,x=30,y=205)

botao = Button(janela, background='white', text='INSERIR')
botao.pack()
botao.place(x=145, y=275)

indiclabel = Label(janela, bg='#626464', text='Indicação', font=('Calibri', 15))
indiclabel.pack()
indiclabel.place(x=30, y=25)

indiclabel = Label(janela, bg='#626464', text='Posologia', font=('Calibri', 15))
indiclabel.pack()
indiclabel.place(width=90,height=25,x=27, y=80)

nomelabel = Label(janela, bg='#626464', text='Nome', font=('Calibri', 15))
nomelabel.pack()
nomelabel.place(width=72,height=25,x=35, y=2)

janela.mainloop()
