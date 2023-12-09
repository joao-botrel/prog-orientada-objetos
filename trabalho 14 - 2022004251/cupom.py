import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import produto as pdt

class Cupom:

    def __init__(self, nroCupom, itensCupom):
        self.__nroCupom = nroCupom
        self.__itensCupom = itensCupom

    @property
    def nroCupom(self):
        return self.__nroCupom
    
    @property
    def itensCupom(self):
        return self.__itensCupom



class LimiteCadastraProduto(tk.Toplevel):
    def __init__(self, controle, listaProdutos):

        tk.Toplevel.__init__(self)
        self.geometry('300x250')
        self.title("Turma")
        self.controle = controle

        self.frameNroCupom = tk.Frame(self)
        self.frameProdutos = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNroCupom.pack()
        self.frameProdutos.pack()
        self.frameButton.pack()        

        self.labelNroCupom = tk.Label(self.frameNroCupom,text="Informe o número do Cupom: ")
        self.labelNroCupom.pack(side="left")
        self.inputNroCupom = tk.Entry(self.frameNroCupom, width=20)
        self.inputNroCupom.pack(side="left")

          
        self.labelProdutos = tk.Label(self.frameProdutos,text="Escolha o produto: ")
        self.labelProdutos.pack(side="left") 
        self.listbox = tk.Listbox(self.frameProdutos)
        self.listbox.pack(side="left")
        for pdt in listaProdutos:
            self.listbox.insert(tk.END, pdt)

        self.buttonInsere = tk.Button(self.frameButton ,text="Insere Produto")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.insereProduto)

        self.buttonCria = tk.Button(self.frameButton ,text="Criar Cupom Fiscal")           
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaCupomFiscal)    

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)            


class LimiteConsultaCupom(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title('Consultar Cupom')
        self.controle = controle
        self.frameNroCupom = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNroCupom.pack()
        self.frameButton.pack()
        self.labelNroCupom = tk.Label(self.frameNroCupom, text="Número do cupom: ")
        self.labelNroCupom.pack(side="left")
        
        self.inputNroCupom = tk.Entry(self.frameNroCupom, width=20)
        self.inputNroCupom.pack(side="left")
        
        self.buttonSubmit = tk.Button(self.frameButton ,text="Consultar")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.consultHandler)

    
    def mostraJanela(self, titulo, msg):
      messagebox.showinfo(titulo, msg)

class CtrlCupom():       
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaCupom = []

    def cadastraCupom(self):        
        self.listaProdutosCupom = []
        listaProdutos = self.ctrlPrincipal.ctrlProduto.getListaDescricaoProduto()
        self.limiteIns = LimiteCadastraProduto(self, listaProdutos)

    def criaCupomFiscal(self, event):
        nroCupomFiscal = self.limiteIns.inputNroCupom.get()
        cupom = Cupom(nroCupomFiscal, self.listaProdutosCupom)
        self.listaCupom.append(cupom)
        self.limiteIns.mostraJanela('Sucesso', 'Cupom emitido com sucesso')
        self.limiteIns.destroy()


    def consultaCupom(self):
        self.limiteConsulta = LimiteConsultaCupom(self)

    def insereProduto(self, event):
        prodSel = self.limiteIns.listbox.get(tk.ACTIVE)
        prod = self.ctrlPrincipal.ctrlProduto.getProduto(prodSel)
        self.listaProdutosCupom.append(prod)
        self.limiteIns.mostraJanela('Sucesso', 'Produto cadastrado!')

    def consultHandler (self, event):
        nroCupom = self.limiteConsulta.inputNroCupom.get()
        string = ''
        aux = 0
        preco = 0
        for cupom in self.listaCupom:
            if nroCupom == cupom.nroCupom:
                aux += 1
                string += 'Número do Cupom: ' + cupom.nroCupom + '\n'
                string += 'Itens vendidos: \n'
                for item in self.listaProdutosCupom:
                    string += item.codigo + ' - ' + item.descricao + ' - ' + str(item.valor) + '\n'
                    preco += item.valor
                string += 'Preço total: ' + str(preco) + '\n'
                string += '------\n'
                self.limiteConsulta.mostraJanela('Sucesso!', string)
        if aux == 0:
            self.limiteConsulta.mostraJanela("Erro!", "Cupom não achado ou número de cupom inexistente")
            
            
