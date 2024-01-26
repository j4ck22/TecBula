from tkinter import *
from JanelaDePesquisa import *
from TESTE import *
from centralizarfunction import *

def paciente():
    masterm = Tk()
    masterm.title('Bula Paciente')
    masterm.iconbitmap(default='icone.ico')
    masterm.geometry('620x750')
    masterm.resizable(height=False, width=False)
    masterm.config(bg='white')
    centralizar(620, 750, masterm)

    #Funcoes
    def voltar():
        masterm.destroy()
        pesquisa()

    def medico2():
        masterm.destroy()
        medico1()


    #imagens
    botaovoltar = PhotoImage(file='voltar.png')
    med = PhotoImage(file='Medicamento2.png')
    botaomedc = PhotoImage(file='profissionalbotao.png')
    pacientel = PhotoImage(file='PacienteLabel.png')
    indic = PhotoImage(file='indicPaciente.png')
    poso = PhotoImage(file='posoPaciente.png')
    efec = PhotoImage(file='EfeitosCPaciente.png')
    contra = PhotoImage(file='contraPac.png')

    #labels
    label = Label(masterm, bg='white', image=med)
    label.pack()
    label.place(x=180, y=35)

    # labelprof = Label(masterm, bg='white', image=pacientel)
    # labelprof.pack()
    # labelprof.place(x=142, y=49)

    labelindc = Label(masterm, bg='white', image=indic)
    labelindc.pack()
    labelindc.place(x=35, y=100)

    labelposo = Label(masterm, bg='white', image=poso)
    labelposo.pack()
    labelposo.place(x=36, y=240)

    labelefec = Label(masterm, bg='white', image=efec)
    labelefec.pack()
    labelefec.place(x=34, y=400)

    labelcontra = Label(masterm, bg='white', image=contra)
    labelcontra.pack()
    labelcontra.place(x=35, y=565)

    #botoes
    botaovolt = Button(masterm, bd=0, bg='white', image=botaovoltar, command=voltar)
    botaovolt.place(width=80, height=45, x=10, y=1)

    # botaopac = Button(masterm, bd=0, bg='white', image=botaomedc, command=medico2)
    # botaopac.place(width=125, height=45, x=330, y=56)


    masterm.mainloop()

if __name__ == '__main__':
    paciente()