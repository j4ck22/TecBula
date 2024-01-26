import tkinter.messagebox
from tkinter import *
from JanelaDePesquisa import pesquisa as pq
from centralizarfunction import centralizar
from tkinter import messagebox as ms
import sqlite3

master = Tk()
master.title('Tec Bula')
master.iconbitmap(default='icone.ico')
master.geometry('350x612')
master.resizable(height=False, width=False)
master.config(bg='white')
centralizar(350,612,master)
#IMAGENS DA INTERFACE
im1 = PhotoImage(file = 'LOGO2.png')
im2 = PhotoImage(file = 'BEMVINDO.png')
im3 = PhotoImage(file = 'tbula.png')
imagembotao1 = PhotoImage(file = 'botaobula.png')
imagembotao2 = PhotoImage(file = 'botaoalarme.png')


#Funções botões
def Bula():
    master.destroy()
    pq()

def Alarme():
    masteralarme = Tk()
    masteralarme.title('Bulas')
    masteralarme.iconbitmap(default='icone.ico')
    masteralarme.geometry('350x612')
    masteralarme.resizable(height=False, width=False)
    masteralarme.config(bg='white')

    master.destroy()
#Labels
lab1 = Label(master, image=im1, bg='white')
lab1.pack()
lab1.place(width=300, height=500, x=18, y=-42)
lab2 = Label(master, image=im2, bg='white')
lab2.pack()
lab2.place(x=-20, y=-5)
lab3 = Label(master, image=im3, bg='white')
lab3.pack()
lab3.place(x=-40, y=310)
#Buttons

botaoBulas = Button(master, bd=0, bg='white', image=imagembotao1, command=Bula )
botaoBulas.place(width=252,height=65, x=45, y=435)
botaoalarme = Button(master, bd=0, bg='white', image=imagembotao2, command=Alarme)
botaoalarme.place(width=252,height=65, x=45, y=500)

# MAIN LOOP DA INTERFACE
master.mainloop()