from tkinter import *
#from JanelaDeAlarmes import *
from centralizarfunction import centralizar
from JanelaDePesquisa import *

def JanelaPrinc():

    janelaPrincipal = Tk()
    janelaPrincipal.title('Tec Bula')
    janelaPrincipal.iconbitmap(default='icone.ico')
    janelaPrincipal.geometry('350x612')
    janelaPrincipal.resizable(height=False, width=False)
    janelaPrincipal.config(bg='white')
    centralizar(350,612,janelaPrincipal)
    #IMAGENS DA INTERFACE
    im1 = PhotoImage(file = 'LOGO2.png')
    im2 = PhotoImage(file = 'BEMVINDO.png')
    im3 = PhotoImage(file = 'tbula.png')
    imagembotao1 = PhotoImage(file = 'botaobula.png')
    imagembotao2 = PhotoImage(file = 'botaoalarme.png')



    #Funções botões
    def Bula():
        janelaPrincipal.destroy()
        JanelaDePesquisa()


    # def Alarme():
    #     janelaPrincipal.destroy()
    #     cadastrar()

    #Labels
    lab1 = Label(janelaPrincipal, image=im1, bg='white')
    lab1.pack()
    lab1.place(width=300, height=500, x=18, y=-42)
    lab2 = Label(janelaPrincipal, image=im2, bg='white')
    lab2.pack()
    lab2.place(x=-20, y=-5)
    lab3 = Label(janelaPrincipal, image=im3, bg='white')
    lab3.pack()
    lab3.place(x=-40, y=310)
    #Buttons

    botaoBulas = Button(janelaPrincipal, bd=0, bg='white', image=imagembotao1, command=Bula )
    botaoBulas.place(width=252,height=65, x=45, y=465)
    # botaoalarme = Button(janelaPrincipal, bd=0, bg='white', image=imagembotao2, command=Alarme)
    # botaoalarme.place(width=252,height=65, x=45, y=500)
    # MAIN LOOP DA INTERFACE

    janelaPrincipal.mainloop()

if __name__ == '__main__':
    JanelaPrinc()
