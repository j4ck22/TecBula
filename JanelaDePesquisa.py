from tkinter import *
from centralizarfunction import centralizar
from TESTE import *
from tkinter import messagebox as ms
from ReconhecimentoDeVoz import ReconhecimentoDeVoz
from JanelaRemedioPaciente import JanelaRemedioPaciente
from FuncoesBanco import Banco



# #Janela Bula
# class JanelaDePesquisa:
#
#     def __init__(self):
#         self.janelaPesq = Tk()
#         self.janelaPesq.title('Bulas')
#         self.janelaPesq.iconbitmap(default='icone.ico')
#         self.janelaPesq.geometry('350x612')
#         self.janelaPesq.resizable(height=0, width=0)
#         self.janelaPesq.config(bg='white')
#         self.banco = Banco()
#
#         #Imagens
#
#         self.medicIMAGE = PhotoImage(file='medicaimg.png')
#         self.abapesquisa = PhotoImage(file='ABApesquisa.png')
#         self.refbotao = PhotoImage(file='refbt.png')
#         self.genbotao = PhotoImage(file='genbt.png')
#         self.simbotao = PhotoImage(file='Simbt.png')
#         self.outbotao = PhotoImage(file='outrosbt.png')
#         self.falarbt = PhotoImage(file='botaoFalar.png')
#         self.pesqbt = PhotoImage(file='botpesquisa.png')
#
#
#     #funcoes
#
#     def falar(self):
#
#      microfone = ReconhecimentoDeVoz()
#      retorno = microfone.ouvirMicrofone()
#
#      if (not retorno):
#         self.microfone.janela.destroy()
#         m = ms.showwarning('Ops!', 'Não entendi! Tente novamente.')
#
#
#      microfone.pesquisarFala()
#      microfone.janela.update()
#
#      busca = self.banco.procurarMedicamento(retorno)
#
#      if (not busca):
#
#          microfone.janela.destroy()
#          m = ms.showwarning('Ops!', 'Remédio não encontrado!')
#
#      microfone.janela.destroy()
#      self.janelaPesq.destroy()
#      print(len(busca))
#      JanelaRemedioPaciente(busca).JanelaRemedio()
#
#
#
#
#     def JanelaPesquisa(self):
#
#         #Centralizador
#
#         centralizar(350, 612, self.janelaPesq)
#
#         #LABELS
#
#         l1 = Label(self.janelaPesq, image=self.medicIMAGE, bg='white')
#         l1.pack()
#         l1.place(x=-15, y=45)
#
#         l2 = Label(self.janelaPesq, image=self.abapesquisa, bg='white')
#         l2.pack()
#         l2.place(width=330, height=80,x=10, y=-15)
#
#
#
#
#         #ENTRADA DE TEXTO
#
#         entrada1 = Entry(self.janelaPesq, bd=0, bg='#786ce1', font=('Calibri', 15), justify=LEFT, )
#         entrada1.place(width=250,height=30, x=55,y=10)
#
#         #BOTÕES
#         botaoreferencia = Button(self.janelaPesq, bd=0, bg='white', image=self.refbotao)
#         botaoreferencia.place(width=456,height=72,x=6, y=109)
#
#         botaogenerico = Button(self.janelaPesq, bd=0, bg='white', image=self.genbotao)
#         botaogenerico.place(width=456,height=73,x=5, y=181)
#
#         botaosimilar = Button(self.janelaPesq, bd=0, bg='white', image=self.simbotao)
#         botaosimilar.place(width=456,height=72,x=8, y=255)
#
#         botaooutros = Button(self.janelaPesq, bd=0, bg='white', image=self.outbotao)
#         botaooutros.place(width=458,height=72,x=10, y=332)
#
#         botaoFalar = Button(self.janelaPesq, bd=0, bg='white', image=self.falarbt, command=self.falar)
#         botaoFalar.place(width=100,height=95,x=128, y=450)
#
#         botaopesquisar = Button(self.janelaPesq, bd=0, bg='#786ce1', image=self.pesqbt)
#         botaopesquisar.place(width=35,height=25,x=12,y=12)
#
#         # loopjanela
#
#         self.janelaPesq.mainloop()
#
# if __name__ == '__main__':
#     JanelaDePesquisa().JanelaPesquisa()
# # janela = JanelaDePesquisa()
# # janela.JanelaPesquisa()




#Janela Bula

def JanelaDePesquisa():
    janelaPesq = Tk()
    janelaPesq.title('Bulas')
    janelaPesq.iconbitmap(default='icone.ico')
    janelaPesq.geometry('350x612')
    janelaPesq.resizable(height=0, width=0)
    janelaPesq.config(bg='white')

    #Imagens

    medicIMAGE = PhotoImage(file='medicaimg.png')
    abapesquisa = PhotoImage(file='ABApesquisa.png')
    refbotao = PhotoImage(file='refbt.png')
    genbotao = PhotoImage(file='genbt.png')
    simbotao = PhotoImage(file='Simbt.png')
    outbotao = PhotoImage(file='outrosbt.png')
    falarbt = PhotoImage(file='botaoFalar.png')
    pesqbt = PhotoImage(file='botpesquisa.png')


    #funcoes

    def falar():

        microfone = ReconhecimentoDeVoz()
        retorno = microfone.ouvirMicrofone()

        if (not retorno):
            microfone.janela.destroy()
            m = ms.showwarning('Ops!', 'Não entendi! Tente novamente.')

        microfone.pesquisarFala()
        microfone.janela.update()

        banco = Banco()
        busca = banco.procurarMedicamento(retorno)

        if (not busca):
            microfone.janela.destroy()
            m = ms.showwarning('Ops!', 'Remédio não encontrado!')

        microfone.janela.destroy()
        janelaPesq.destroy()
        print(len(busca))
        JanelaRemedioPaciente(busca).JanelaRemedio()

        return True


    #Centralizador

    centralizar(350, 612, janelaPesq)

    #LABELS

    l1 = Label(janelaPesq, image=medicIMAGE, bg='white')
    l1.pack()
    l1.place(x=-15, y=45)

    l2 = Label(janelaPesq, image=abapesquisa, bg='white')
    l2.pack()
    l2.place(width=330, height=80,x=10, y=-15)




    #ENTRADA DE TEXTO

    entrada1 = Entry(janelaPesq, bd=0, bg='#786ce1', font=('Calibri', 15), justify=LEFT, )
    entrada1.place(width=250,height=30, x=55,y=10)

    #BOTÕES
    botaoreferencia = Button(janelaPesq, bd=0, bg='white', image=refbotao)
    botaoreferencia.place(width=456,height=72,x=6, y=109)

    botaogenerico = Button(janelaPesq, bd=0, bg='white', image=genbotao)
    botaogenerico.place(width=456,height=73,x=5, y=181)

    botaosimilar = Button(janelaPesq, bd=0, bg='white', image=simbotao)
    botaosimilar.place(width=456,height=72,x=8, y=255)

    # botaooutros = Button(janelaPesq, bd=0, bg='white', image=outbotao)
    # botaooutros.place(width=458,height=72,x=10, y=332)

    botaoFalar = Button(janelaPesq, bd=0, bg='white', image=falarbt, command=falar)
    botaoFalar.place(width=100,height=95,x=128, y=450)

    botaopesquisar = Button(janelaPesq, bd=0, bg='#786ce1', image=pesqbt)
    botaopesquisar.place(width=35,height=25,x=12,y=12)

    # loopjanela

    janelaPesq.mainloop()

if __name__ == '__main__':
    JanelaDePesquisa()