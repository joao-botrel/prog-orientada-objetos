import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os.path
import pickle


class Jogo:
    def __init__(self, codigo, titulo, console, genero, preco):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__console = console
        self.__genero = genero
        self.__preco = preco
        self.__avaliacoes = []

    @property
    def codigo(self):
        return self.__codigo

    @property
    def titulo(self):
        return self.__titulo

    @property
    def console(self):
        return self.__console

    @console.setter
    def console(self, valor):
        self.consoles = ["XBox", "Playstation", "Switch", "PC"]
        if not valor in self.consoles:
            raise ValueError("Console inválido: {}".format(valor))
        else:
            self.__console = valor

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, valor):
        self.generos = ["Ação", "Aventura",
                        "Estratégia", "RPG", "Esporte", "Simulação"]
        if not valor in self.generos:
            raise ValueError("Genero inválido: {}".format(valor))
        else:
            self.__genero = valor

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if valor < 0 or valor >= 500:
            raise ValueError("Valor inválido: {}".format(valor))
        else:
            self.__preco = valor

    @property
    def avaliacoes(self):
        return self.__avaliacoes

    def avaliaJogo(self, nota):
        self.__avaliacoes.append(nota)

    def calculoEstrela(self):
        estrelas = 0
        media = 0
        den = 0
        soma = 0
        for nota in self.avaliacoes:
            den = den + 1
            soma = soma + nota

        media = soma / den
        if 0 < media or media <= 1:
            estrelas = 1
        if 1 < media or media <= 2:
            estrelas = 2
        if 2 < media or media <= 3:
            estrelas = 3
        if 3 < media or media <= 4:
            estrelas = 4
        if 4 < media or media <= 5:
            estrelas = 5

        return estrelas

    def getJogo(self):
        return "\nTitulo: " + str(self.titulo)\
            + "\nCodigo: " + str(self.codigo)\
            + "\nConsole: " + str(self.console)\
            + "\nGenero: " + str(self.genero)\
            + "\nPreço: " + str(self.preco)


class LimiteInsereJogo(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Cadastrar")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameTitulo = tk.Frame(self)
        self.frameConsole = tk.Frame(self)
        self.frameGenero = tk.Frame(self)
        self.framePreco = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.frameCodigo.pack()
        self.frameTitulo.pack()
        self.frameConsole.pack()
        self.frameGenero.pack()
        self.framePreco.pack()
        self.frameButton.pack()

        self.labelCodigo = tk.Label(self.frameCodigo, text="Codigo: ")
        self.labelTitulo = tk.Label(self.frameTitulo, text="Titulo: ")
        self.labelConsole = tk.Label(self.frameConsole, text="Console: ")
        self.labelGenero = tk.Label(self.frameGenero, text="Genero: ")
        self.labelPreco = tk.Label(self.framePreco, text="Preco: ")
        self.labelCodigo.pack(side="left")
        self.labelTitulo.pack(side="left")
        self.labelConsole.pack(side="left")
        self.labelGenero.pack(side="left")
        self.labelPreco.pack(side="left")

        self.inputCodigo = tk.Entry(self.frameCodigo, width=10)
        self.inputTitulo = tk.Entry(self.frameTitulo, width=20)
        self.inputConsole = tk.Entry(self.frameConsole, width=15)
        self.inputGenero = tk.Entry(self.frameGenero, width=20)
        self.inputPreco = tk.Entry(self.framePreco, width=10)
        self.inputCodigo.pack(side="left")
        self.inputTitulo.pack(side="left")
        self.inputConsole.pack(side="left")
        self.inputGenero.pack(side="left")
        self.inputPreco.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class LimiteAvaliaJogo(tk.Toplevel):
    def __init__(self, controle, listaNotas):
        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Avaliar")
        self.controle = controle

        self.frameTitulo = tk.Frame(self)
        self.frameNota = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameTitulo.pack()
        self.frameNota.pack()
        self.frameButton.pack()

        self.labelTitulo = tk.Label(self.frameTitulo, text="Titulo do jogo: ")
        self.labelTitulo.pack(side="left")
        self.inputTitulo = tk.Entry(self.frameTitulo, width=20)
        self.inputTitulo.pack(side="left")

        self.labelNota = tk.Label(
            self.frameNota, text="Escolha a nota(em estrelas): ")
        self.labelNota.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(
            self.frameNota, width=15, textvariable=self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaNotas

        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterAvaliacaoHandler)

        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearAvaliacaoHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaAvaliacaoHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class LimiteConsultaJogo(tk.Toplevel):
    def __init__(self, controle, listaNotas):

        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Consultar")
        self.controle = controle

        self.frameNota = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNota.pack()
        self.frameButton.pack()

        self.labelNota = tk.Label(self.frameNota, text="Escolha a nota: ")
        self.labelNota.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(
            self.frameNota, width=15, textvariable=self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaNotas

        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", self.controle.enterConsultHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", self.controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class CtrlJogo():
    def __init__(self, controlador):
        self.controlador = controlador
        self.listaNotas = ['1', '2', '3', '4', '5']
        if not os.path.isfile("jogos.pickle"):
            self.listaJogos = []
        else:
            with open("jogos.pickle", "rb") as f:
                self.listaJogos = pickle.load(f)

    def salvaJogos(self):
        if len(self.listaJogos) != 0:
            with open("jogos.pickle", "wb") as f:
                pickle.dump(self.listaJogos, f)

    def cadastraJogo(self):
        self.limiteIns = LimiteInsereJogo(self)

    def avaliaJogo(self):
        self.limiteAvl = LimiteAvaliaJogo(self, self.listaNotas)

    def consultaJogo(self):
        self.limiteCons = LimiteConsultaJogo(self, self.listaNotas)


    def enterHandler(self, event):
        codigo = self.limiteIns.inputCodigo.get()
        titulo = self.limiteIns.inputTitulo.get()
        console = self.limiteIns.inputConsole.get()
        genero = self.limiteIns.inputGenero.get()
        preco = int(self.limiteIns.inputPreco.get())

        try:
            jogo = Jogo(codigo, titulo, console, genero, preco)
            self.listaJogos.append(jogo)
            self.limiteIns.mostraJanela(
                'Sucesso', 'Jogo cadastrado com sucesso')
            self.clearHandler(event)
        except ValueError as error:
            self.limiteIns.mostraJanela('Erro', error)

    def enterAvaliacaoHandler(self, event):
        titulo = self.limiteAvl.inputTitulo.get()
        nota = int(self.limiteAvl.escolhaCombo.get())
        for jogo in self.listaJogos:
            if jogo.titulo == titulo:
                jogo.avaliaJogo(nota)
                self.limiteAvl.mostraJanela(
                    'Sucesso', 'Avaliação recebida com sucesso')
        self.limiteAvl.destroy()

    def enterConsultHandler(self, event):
        str = ''
        nota = int(self.limiteCons.escolhaCombo.get())
        for jogo in self.listaJogos:
            if nota == jogo.calculoEstrela():
                str += jogo.getJogo() + '\n'
        self.limiteCons.mostraJanela('Consulta', str)

    def clearHandler(self, event):
        self.limiteIns.inputCodigo.delete(
            0, len(self.limiteIns.inputCodigo.get()))
        self.limiteIns.inputTitulo.delete(
            0, len(self.limiteIns.inputTitulo.get()))
        self.limiteIns.inputConsole.delete(
            0, len(self.limiteIns.inputConsole.get()))
        self.limiteIns.inputGenero.delete(
            0, len(self.limiteIns.inputGenero.get()))
        self.limiteIns.inputPreco.delete(
            0, len(self.limiteIns.inputPreco.get()))

    def clearAvaliacaoHandler(self, event):
        self.limiteIns.inputTitulo.delete(
            0, len(self.limiteIns.inputTitulo.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()

    def fechaAvaliacaoHandler(self, event):
        self.limiteAvl.destroy()
