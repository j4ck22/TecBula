from tkinter import *

from JanelaRemedioMedico import *
from centralizarfunction import *
from JanelaPrincipal import *
import JanelaDePesquisa



#variaveis globais

_idMedicamento = 0
Nome = 1
tipoMedicamento = 2
Indicacao = 3
Posologia = 4
efeitosColaterais = 5
Contraindicacoes = 6

class JanelaRemedioPaciente:

    def __init__(self, retornoBanco):

        self.arrayBanco = retornoBanco
        self.janelaRemedio = Tk()
        self.janelaRemedio.title('Bula Paciente')
        self.janelaRemedio.iconbitmap(default='icone.ico')
        self.janelaRemedio.geometry('600x612')
        self.janelaRemedio.resizable(height=False, width=False)
        self.janelaRemedio.config(bg='white')
        self.texto_Nome = StringVar(self.janelaRemedio, "")
        self.texto_Indic = StringVar(self.janelaRemedio, "")
        self.texto_Poso = StringVar(self.janelaRemedio, "")
        self.texto_Efe = StringVar(self.janelaRemedio, "")
        self.texto_Contra = StringVar(self.janelaRemedio, "")
        self.paginacao = StringVar(self.janelaRemedio, "1")
        self.pagina = 1
        self.coluna = 0
        self.label = Label()



        # imagens
        self.botaovoltar = PhotoImage(file='voltar.png')
        self.med = PhotoImage(file='Medicamento2.png')
        self.botaomedc = PhotoImage(file='profissionalbotao.png')
        self.pacientel = PhotoImage(file='PacienteLabel.png')
        self.indic = PhotoImage(file='indicPaciente.png')
        self.poso = PhotoImage(file='posoPaciente.png')
        self.efec = PhotoImage(file='EfeitosCPaciente.png')
        self.contra = PhotoImage(file='contraPac.png')
        self.botaonextp = PhotoImage(file='nextpag.png')
        self.botaobackp = PhotoImage(file='backpag.png')


    #Funcoes
    def voltar(self):
        self.janelaRemedio.destroy()
        JanelaDePesquisa()



    # def medico2(self):
    #     self.janelaRemedio.destroy()
    #     medico1()

    def nextpag(self):
        print(f"{self.pagina} {len(self.arrayBanco)}")
        if (self.pagina == len(self.arrayBanco)):

            self.janelaRemedio.mainloop()
        else:

            self.pagina += 1
            self.coluna += 1
            self.paginacao.set(self.pagina)
            self.label.destroy()
            self.JanelaRemedio()



    def backpag(self):
        print(f"{self.pagina} {len(self.arrayBanco)}")
        if (self.pagina == 1):

            self.janelaRemedio.mainloop()
        else:
            self.pagina -= 1
            self.coluna -= 1
            self.paginacao.set(self.pagina)
            self.label.destroy()
            self.JanelaRemedio()



    def JanelaRemedio(self):

        if (len(self.arrayBanco) > 1):

            # Centralizar

            centralizar(600, 612, self.janelaRemedio)
            win_width, win_height = 500, 612
            # labels

            self.label = Label(self.janelaRemedio, bg='white', image=self.med)
            self.label.pack()
            self.label.place(x=170, y=-5)

            # labelpaciente = Label(self.janelaRemedio, bg='white', image=self.pacientel)
            # labelpaciente.pack()
            # labelpaciente.place(x=225, y=49)

            self.texto_Nome.set(self.arrayBanco[self.coluna][Nome])
            self.label = Label(self.janelaRemedio, bg='white', fg='#786ce1',
                                 textvariable=self.texto_Nome,
                                 font=('Source Serif Pro Black', 20), anchor=CENTER, justify=LEFT)
            self.label.pack()
            self.label.place(x=41, y=75)

            self.label = Label(self.janelaRemedio, bg='white', image=self.indic)
            self.label.pack()
            self.label.place(x=35, y=120)

            self.texto_Indic.set(self.arrayBanco[self.coluna][Indicacao])
            self.label = Label(self.janelaRemedio, wraplength=win_width, bg='white', fg='black',
                               textvariable=self.texto_Indic,
                               font=('Calibre', 11), anchor=CENTER, justify=LEFT)
            self.label.pack()
            self.label.place(x=50, y=170)


            self.label = Label(self.janelaRemedio, bg='white', image=self.poso)
            self.label.pack()
            self.label.place(x=35, y=210)

            self.texto_Poso.set(self.arrayBanco[self.coluna][Posologia])
            self.label = Label(self.janelaRemedio, wraplength=win_width, bg='white', fg='black',
                               textvariable=self.texto_Poso,
                               font=('Calibre', 11), anchor=CENTER, justify=LEFT)
            self.label.pack()
            self.label.place(x=50, y=260)

            self.label = Label(self.janelaRemedio, bg='white', image=self.efec)
            self.label.pack()
            self.label.place(x=35, y=340)

            self.texto_Efe.set(self.arrayBanco[self.coluna][efeitosColaterais])
            self.label = Label(self.janelaRemedio, wraplength=win_width, bg='white', fg='black',
                               textvariable=self.texto_Efe,
                               font=('Calibre', 11), anchor=CENTER, justify=LEFT)
            self.label.pack()
            self.label.place(x=50, y=370)

            self.label = Label(self.janelaRemedio, bg='white', image=self.contra)
            self.label.pack()
            self.label.place(x=35, y=450)

            self.texto_Contra.set(self.arrayBanco[self.coluna][Contraindicacoes])
            self.label = Label(self.janelaRemedio, wraplength=win_width, bg='white', fg='black',
                                 textvariable=self.texto_Contra,
                                 font=('Calibre', 11), anchor=CENTER, justify=LEFT)
            self.label.pack()
            self.label.place(x=50, y=480)

            self.label = Label(self.janelaRemedio, wraplength=win_width, bg='white', fg='#786ce1',
                                 textvariable=self.paginacao,
                                 font=('Source Serif Pro Black', 11), anchor=CENTER, justify=CENTER)
            self.label.pack()
            self.label.place(x=300, y=570)


            # botoes

            botaovolt = Button(self.janelaRemedio, bd=0, bg='white', image=self.botaovoltar, command=self.voltar)
            botaovolt.place(width=80, height=45, x=10, y=1)

            botaonextp = Button(self.janelaRemedio, bd=0, bg='white', image=self.botaonextp, command=self.nextpag)
            botaonextp.place(width=20, height=36, x=320, y=570)

            botaobackp = Button(self.janelaRemedio, bd=0, bg='white', image=self.botaobackp, command=self.backpag)
            botaobackp.place(width=20, height=33, x=275, y=570)


            self.janelaRemedio.mainloop()

        else:

            #Centralizar

            centralizar(600, 612, self.janelaRemedio)
            win_width, win_height = 500, 612

            #labels

            self.label = Label(self.janelaRemedio, bg='white', image=self.med)
            self.label.pack()
            self.label.place(x=170, y=-5)

            # labelpaciente = Label(self.janelaRemedio, bg='white', image=self.pacientel)
            # labelpaciente.pack()
            # labelpaciente.place(x=225, y=49)

            self.texto_Nome.set(self.arrayBanco[self.coluna][Nome])
            self.label = Label(self.janelaRemedio, bg='white', fg='#786ce1',
                                 textvariable=self.texto_Nome,
                                 font=('Source Serif Pro Black', 20), anchor=CENTER, justify=LEFT)
            self.label.pack()
            self.label.place(x=41, y=75)

            self.label = Label(self.janelaRemedio, bg='white', image=self.indic)
            self.label.pack()
            self.label.place(x=35, y=120)

            self.texto_Indic.set(self.arrayBanco[self.coluna][Indicacao])
            self.label = Label(self.janelaRemedio, wraplength=win_width, bg='white', fg= 'black', textvariable=self.texto_Indic,
                                 font=('Calibre', 11), anchor=CENTER, justify=LEFT)
            self.label.pack()
            self.label.place(x=50, y=170)

            self.label = Label(self.janelaRemedio, bg='white', image=self.poso)
            self.label.pack()
            self.label.place(x=35, y=210)

            self.texto_Poso.set(self.arrayBanco[self.coluna][Posologia])
            self.label = Label(self.janelaRemedio, wraplength=win_width, bg='white', fg= 'black', textvariable=self.texto_Poso,
                                 font=('Calibre', 11), anchor=CENTER, justify=LEFT)
            self.label.pack()
            self.label.place(x=50, y=260)

            self.label = Label(self.janelaRemedio, bg='white', image=self.efec)
            self.label.pack()
            self.label.place(x=35, y=340)

            self.texto_Efe.set(self.arrayBanco[self.coluna][efeitosColaterais])
            self.label = Label(self.janelaRemedio, wraplength=win_width, bg='white', fg= 'black', textvariable=self.texto_Efe,
                                 font=('Calibre', 11), anchor=CENTER, justify=LEFT)
            self.label.pack()
            self.label.place(x=50, y=370)

            self.label = Label(self.janelaRemedio, bg='white', image=self.contra)
            self.label.pack()
            self.label.place(x=35, y=450)

            self.texto_Contra.set(self.arrayBanco[self.coluna][Contraindicacoes])
            self.label = Label(self.janelaRemedio, wraplength=win_width, bg='white', fg= 'black', textvariable=self.texto_Contra,
                                 font=('Calibre', 11), anchor=CENTER, justify=LEFT)
            self.label.pack()
            self.label.place(x=50, y=480)

            self.label = Label(self.janelaRemedio, wraplength=win_width, bg='white', fg='#786ce1',
                                 textvariable=self.paginacao,
                                 font=('Source Serif Pro Black', 11), anchor=CENTER, justify=CENTER)
            self.label.pack()
            self.label.place(x=300, y=570)

            #botoes
            botaovolt = Button(self.janelaRemedio, bd=0, bg='white', image=self.botaovoltar, command=self.voltar)
            botaovolt.place(width=80, height=45, x=10, y=1)

            # botaomed= Button(self.janelaRemedio, bd=0, bg='white', image=self.botaomedc, command=self.medico2)
            # botaomed.place(width=125, height=45, x=330, y=56)


            self.janelaRemedio.mainloop()

if __name__ == '__main__':
    JanelaRemedioPaciente().JanelaRemedio()

