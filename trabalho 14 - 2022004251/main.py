import tkinter as tk
from tkinter import messagebox
import cupom as cup
import produto as pdt

#2022004251 - João Vítor Botrel

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)
        self.produtoMenu = tk.Menu(self.menubar)
        self.cupomMenu = tk.Menu(self.menubar)


        self.produtoMenu.add_command(label="Cadastra", command=self.controle.cadastraProduto)
        self.produtoMenu.add_command(label="Consulta", command=self.controle.consultaProduto)
        self.menubar.add_cascade(label="Produto", menu=self.produtoMenu)

        
        self.cupomMenu.add_command(label="Cadastrar",command=self.controle.cadastraCupom)
        self.cupomMenu.add_command(label="Consulta",command=self.controle.consultaCupom)
        self.menubar.add_cascade(label="Cupom", menu=self.cupomMenu)



        self.root.config(menu=self.menubar)


class ControlePrincipal():
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlProduto = pdt.CtrlProduto()
        self.ctrlCupom = cup.CtrlCupom(self)
        

        self.limite = LimitePrincipal(self.root, self)

        self.root.title("Emissão de cupom fiscal")
        # Inicia o mainloop
        self.root.mainloop()

    def cadastraProduto(self):
        self.ctrlProduto.cadastraProduto()

    def consultaProduto(self):
        self.ctrlProduto.consultaProduto()
    
    def cadastraCupom(self):
        self.ctrlCupom.cadastraCupom()

    def consultaCupom(self):
        self.ctrlCupom.consultaCupom()



if __name__ == '__main__':
    c = ControlePrincipal()