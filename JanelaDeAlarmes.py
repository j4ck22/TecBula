from tkinter import *
from centralizarfunction import *
from JanelaDeCadastroDeAlarme import *


def cadastrar():
    masterm = Tk()
    masterm.title('Alarmes')
    masterm.iconbitmap(default='icone.ico')
    masterm.geometry('360x612')
    masterm.resizable(height=False, width=False)
    masterm.config(bg='white')
    centralizar(360, 612, masterm)
    #funcoes
    def cadastrar():
        masterm.destroy()
        cadpagina()

    def back():
        masterm.destroy()
        principal()

    #imagens
    listalarmes = PhotoImage(file= 'listaalarme.png')
    abaalarmes = PhotoImage(file ='abalarme.png')
    botaoaddalr = PhotoImage(file = 'botaoalarme.png')


    #labels
    labelalarme = Label(masterm, bg='white', image=listalarmes)
    labelalarme.pack()
    labelalarme.place(x=55, y=-3)

    labelabalarmes = Label(masterm, bg='white', image=abaalarmes)
    labelabalarmes.pack()
    labelabalarmes.place(x=11, y=40)
    #botões
    botaoalarme = Button(masterm, bd=0, bg='white', image=botaoaddalr, command=cadastrar)
    botaoalarme.place(height=65 ,width=250, x=54, y=515)


    masterm.mainloop()

if __name__ == '__main__':
    cadastrar()