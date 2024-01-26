from tkinter import *
from centralizarfunction import *
from JanelaDeAlarmes import *

def cadpagina():
    master = Tk()
    master.title('Registro de alarme')
    master.iconbitmap(default='icone.ico')
    master.geometry('355x612')
    master.resizable(height=False, width=False)
    master.config(bg='white')
    centralizar(379,612,master)

    #imagens
    cadastalarme = PhotoImage(file='CadUmAlarme.png')
    botCad = PhotoImage(file = 'botCadastrar.png')
    linhanome = PhotoImage(file = 'linhaNome.png')
    linhadosagem = PhotoImage(file = 'linhadosagem.png')
    linhahora = PhotoImage(file = 'linhaHoraAlarme.png')
    botaodacaixa = PhotoImage(file = 'botaocaixa.png')
    botaovoltar = PhotoImage(file='voltar.png')

    #funcoes
    def back():
        master.destroy()
        cadastrar()
    #botões
    botcadastrar = Button(master, bd=0, bg='white', image=botCad)
    botcadastrar.place(x=85, y=485)

    botaocaixa = Button(master, bd=0, bg='white', image=botaodacaixa)
    botaocaixa.place(width=50, height=40,x=318, y=385)

    botaovolt = Button(master, bd=0, bg='white', image=botaovoltar, command=back)
    botaovolt.place(width=78, height=45, x=0, y=550)
    #labels
    label1 = Label(master, bg='white', image=cadastalarme)
    label1.pack()
    label1.place(x=20, y=2)

    labelnome = Label(master, bg='white', image=linhanome)
    labelnome.pack()
    labelnome.place(x=-5, y=78)

    labeldosagem = Label(master, bg='white', image=linhadosagem)
    labeldosagem.pack()
    labeldosagem.place(x= -5, y=210)

    labellinha= Label(master, bg='white', image=linhahora)
    labellinha.pack()
    labellinha.place(x=-5, y=340)

    # textonome = Label(master, text='nome', font=('Times 19'), bg='white')
    # textonome.pack()
    # textonome.place(x=6, y=77)
    #entrada de texto
    entrada1 = Entry(master, bd=0, bg='#f0f0f0', font=('Calibri', 15), justify=LEFT, )
    entrada1.place(width=357, height=30, x=10, y=118)

    entrada2 = Entry(master, bd=0, bg='#f0f0f0', font=('Calibri', 15), justify=LEFT, )
    entrada2.place(width=357, height=30, x=10, y=250)

    # entrada3 = Entry(master, bd=0, bg='#f0f0f0', font=('Calibri', 15), justify=LEFT, )
    # entrada3.place(width=357, height=30, x=10, y=381)

    master.mainloop()

if __name__ == '__main__':
    cadpagina()