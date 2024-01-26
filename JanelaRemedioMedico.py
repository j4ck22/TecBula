from tkinter import *
from JanelaDePesquisa import *
from JanelaRemedioPaciente import *
from centralizarfunction import *
def medico1():
    masterm = Tk()
    masterm.title('Bula Medico')
    masterm.iconbitmap(default='icone.ico')
    masterm.geometry('600x612')
    masterm.resizable(height=False, width=False)
    masterm.config(bg='white')
    centralizar(600, 612, masterm)

    #funções
    def voltar():
        masterm.destroy()
        pesquisa()

    def paciente2():
        masterm.destroy()
        paciente()

    #Imagens
    botaovoltar = PhotoImage(file='voltar.png')
    med = PhotoImage(file='Medicamento2.png')
    profissional = PhotoImage(file='profissionalLABEL.png')
    botaopaci = PhotoImage(file='pacientebotao.png')
    mecacao = PhotoImage(file='Mecacao.png')
    compom = PhotoImage(file='compoMed.png')
    intem = PhotoImage(file='interMED.png')
    precau = PhotoImage(file='PrecauMed.png')

    #labels
    label = Label(masterm, bg='white', image=med)
    label.pack()
    label.place(x=170, y=-5)

    labelprof = Label(masterm, bg='white', image=profissional)
    labelprof.pack()
    labelprof.place(x=320, y=49)

    labelmec = Label(masterm, bg='white', image=mecacao)
    labelmec.pack()
    labelmec.place(x=35, y=120)

    labelcomp = Label(masterm, bg='white', image=compom)
    labelcomp.pack()
    labelcomp.place(x=37, y=230)

    labelinter = Label(masterm, bg='white', image=intem)
    labelinter.pack()
    labelinter.place(x=39, y=351)

    labelpre = Label(masterm, bg='white', image=precau)
    labelpre.pack()
    labelpre.place(x=37, y=465)

    #botões
    botaovolt = Button(masterm, bd=0, bg='white', image=botaovoltar, command=voltar)
    botaovolt.place(width=80, height=45, x=10, y=1)

    botaopac = Button(masterm, bd=0, bg='white', image=botaopaci, command=paciente2)
    botaopac.place(width=125, height=45, x=150, y=57)

    masterm.mainloop()


if __name__ == '__main__':
    medico1()