# pip install SpeechRecognition
#
# pip install pyaudio

# Imports
from centralizarfunction import centralizar
from tkinter import *
from tkinter import messagebox as ms
import speech_recognition as sr


# Class
class ReconhecimentoDeVoz:

# Construtores
    def __init__(self):
        self.faleRemed = PhotoImage(file='FaleRemedio.png')
        self.falar = "Vazio"
        self.janela = Tk()
        self.janela.title('reconhecimento')
        self.janela.iconbitmap(default='icone.ico')
        self.janela.geometry('350x612')
        self.janela.resizable(height=0, width=0)
        self.janela.config(bg='white')
        self.texto_variable = StringVar(self.janela,"")
        self.Label = Label()



    #funções
    def pesquisarFala(self):


        self.Label.destroy()
        #label pesquisar
        centralizar(350,170, self.janela)
        LabelPesquisa = Label(self.janela, bg='white', fg= '#786ce1', textvariable=self.texto_variable, font=('Source Serif Pro Black', 25), justify=CENTER)
        LabelPesquisa.pack()
        LabelPesquisa.place(x=50, y=50)
        self.Label = LabelPesquisa

        self.janela.update()

        return True




    # # Função para ouvir e reconhecer a fala
    # def ouvirMicrofone(self):
    #
    #
    #     # label fale
    #
    #     #centralizar(230, 170, self.janela)
    #     centralizar(350, 170, self.janela)
    #     Labelfale = Label(self.janela,bg='white', fg= '#786ce1', text="FALE O NOME DO\nREMÉDIO", font=('Source Serif Pro Black', 25), justify=CENTER)
    #     #Labelfale = Label(self.janela, image=self.faleRemed, bg='white')
    #     Labelfale.pack()
    #     Labelfale.place(x=40, y=30)
    #     self.Label = Labelfale
    #     #Labelfale.place(x=-15, y=45)
    #     #Labelfale.place(width=330, height=80, x=10, y=-15)
    #
    #     # loopjanela
    #     # self.janela.mainloop()
    #
    #
    #     # Habilita o microfone do usuário
    #     microfone = sr.Recognizer()
    #
    #     # usando o microfone
    #     with sr.Microphone() as source:
    #
    #         # Chama um algoritmo de reducao de ruidos no som
    #         microfone.adjust_for_ambient_noise(source)
    #
    #         # Frase para o usuario dizer algo
    #         self.janela.update()
    #         print("Diga alguma coisa: ")
    #
    #
    #
    #         # Armazena o que foi dito numa variavel
    #         audio = microfone.listen(source)
    #
    #
    #         try:
    #             # Passa a variável para o algoritmo reconhecedor de padroes
    #             frase = microfone.recognize_google(audio, language='pt-BR')
    #
    #             # Retorna a frase pronunciada
    #
    #             print("Você disse: " + frase)
    #
    #             #self.falar = frase
    #             self.texto_variable.set("PESQUISANDO...")
    #
    #             return frase
    #
    #             # Se nao reconheceu o padrao de fala, exibe a mensagem
    #
    #         except sr.UnknownValueError:
    #
    #             return False



    #Função para ouvir e reconhecer a fala
    def ouvirMicrofone(self):


        # label fale

        #centralizar(230, 170, self.janela)
        centralizar(350, 170, self.janela)
        Labelfale = Label(self.janela,bg='white', fg= '#786ce1', text="FALE O NOME DO\nREMÉDIO", font=('Source Serif Pro Black', 25), justify=CENTER)
        #Labelfale = Label(self.janela, image=self.faleRemed, bg='white')
        Labelfale.pack()
        Labelfale.place(x=40, y=30)
        self.Label = Labelfale
        #Labelfale.place(x=-15, y=45)
        #Labelfale.place(width=330, height=80, x=10, y=-15)

        # loopjanela
        # self.janela.mainloop()

        self.janela.update()
        print("Diga alguma coisa: ")




        # Armazena o que foi dito numa variavel
        audio = "Dipirona"

        self.texto_variable.set("PESQUISANDO...")


        try:
            # Passa a variável para o algoritmo reconhecedor de padroes
            frase = audio

            # Retorna a frase pronunciada

            print("Você disse: " + frase)

            #self.falar = frase
            self.texto_variable.set("PESQUISANDO...")

            return frase

            # Se nao reconheceu o padrao de fala, exibe a mensagem

        except sr.UnknownValueError:

            return False