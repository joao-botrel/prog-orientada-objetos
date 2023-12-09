import tkinter as tk
from tkinter import messagebox


class Produto:

    def __init__(self, codigo, descricao, valor):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valor = valor

    @property
    def codigo(self):
        return self.__codigo

    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def valor (self):
        return self.__valor


class LimiteCadastraProduto(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Produto")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameDescricao = tk.Frame(self)
        self.frameValor = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameDescricao.pack()
        self.frameValor.pack()
        self.frameButton.pack()

        self.labelCodigo = tk.Label(self.frameCodigo, text="Código: ")
        self.labelDescricao = tk.Label(self.frameDescricao, text="Descrição: ")
        self.labelValor = tk.Label(self.frameValor, text="Valor: ")
        self.labelCodigo.pack(side="left")
        self.labelDescricao.pack(side="left")
        self.labelValor.pack(side="left")

        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputCodigo.pack(side="left")
        self.inputDescricao = tk.Entry(self.frameDescricao, width=20)
        self.inputDescricao.pack(side="left")
        self.inputValor = tk.Entry(self.frameValor, width=20)
        self.inputValor.pack(side="left")

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



class LimiteConsultaProduto(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title('Consultar produto')
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameButton.pack()

        self.labelCodigo = tk.Label(self.frameCodigo, text="Código: ")
        self.labelCodigo.pack(side="left")

        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputCodigo.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Consultar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.consultHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class CtrlProduto():
    def __init__(self):
        self.listaProdutos = [ Produto('01', 'Coca Cola 350 ml', 4)
        
        ]

    def getProduto(self, descricao):
        pdtRet = None
        for pdt in self.listaProdutos:
            if pdt.descricao == descricao:
                pdtRet = pdt
        return pdtRet

    def getListaCodProduto(self):
        listaCod = []
        for pdt in self.listaProdutos:
            listaCod.append(pdt.codigo)
        return listaCod

    def getListaDescricaoProduto(self):
        listaDesc = []
        for pdt in self.listaProdutos:
            listaDesc.append(pdt.descricao)
        return listaDesc

    def cadastraProduto(self):
        self.limiteIns = LimiteCadastraProduto(self)

    def consultaProduto(self):
        self.limiteConsulta = LimiteConsultaProduto(self)

    def enterHandler(self, event):
        codigo = self.limiteIns.inputCodigo.get()
        descricao = self.limiteIns.inputDescricao.get()
        valor = self.limiteIns.inputValor.get
        produto = Produto(codigo, descricao, valor)
        self.listaProdutos.append(produto)
        self.limiteIns.mostraJanela('Sucesso', 'Produto cadastrado com sucesso!')
        self.clearHandler(event)

    def consultHandler(self, event):
        codigo = self.limiteConsulta.inputCodigo.get()
        aux = 0
        for cod in self.listaProdutos:
            if codigo == cod.codigo:
                self.limiteConsulta.mostraJanela('Sucesso', 'Código: ' + cod.codigo + '\n -- Descricao: ' + cod.descricao + '\n -- Valor: ' + str(cod.valor) + '\n')
                aux +=1
                self.consultClearHandler(event)
                
        if aux == 0:
            self.limiteConsulta.mostraJanela("Erro!", "Produto não encontrado ou código inexistente.")
            self.consultClearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputCodigo.delete(0, len(self.limiteIns.inputCodigo.get()))
        self.limiteIns.inputDescricao.delete(0, len(self.limiteIns.inputDescricao.get()))
        self.limiteIns.inputValor.delete(0, len(self.limiteIns.inputValor.get()))

    def consultClearHandler(self, event):
        self.limiteConsulta.inputCodigo.delete(0, len(self.limiteConsulta.inputCodigo.get()))


    def fechaHandler(self, event):
        self.limiteIns.destroy()
