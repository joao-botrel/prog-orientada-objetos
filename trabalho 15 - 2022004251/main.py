import tkinter as tk
import jogo as jogo

#2022004251 - João Vítor Botrel



class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.jogoMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar)

        self.jogoMenu.add_command(label="Cadastrar", command=self.controle.cadastraJogo)
        self.jogoMenu.add_command(label="Consultar", command=self.controle.consultaJogo)
        self.jogoMenu.add_command(label="Avaliar", command=self.controle.avaliaJogo)
        self.menubar.add_cascade(label="Jogos", menu=self.jogoMenu)

        self.sairMenu.add_command(label="Salva", command=self.controle.salvaDados)
        self.menubar.add_cascade(label="Sair", menu=self.sairMenu)
               
        self.root.config(menu=self.menubar)

      
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlJogo = jogo.CtrlJogo(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Games")
        # Inicia o mainloop
        self.root.mainloop()
    
    def cadastraJogo(self):
        self.ctrlJogo.cadastraJogo()
    
    def consultaJogo(self):
        self.ctrlJogo.consultaJogo()
    
    def avaliaJogo (self):
        self.ctrlJogo.avaliaJogo()
    
    def salvaDados(self):
        self.ctrlJogo.salvaJogos()
        self.root.destroy()


if __name__ == '__main__':
    c = ControlePrincipal()