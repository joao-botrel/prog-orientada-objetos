from abc import ABC, abstractmethod


class Vendedor(ABC):
    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome
        self.__vendas = []

    @property
    def codigo(self):
        return self.__codigo

    @property
    def vendas(self):
        return self.__vendas

    @property
    def nome(self):
        return self.__nome

    def adicionaVenda(self, codigo, mes, ano, valor):
        self.vendas.append(Venda(codigo, mes, ano, valor))

    @abstractmethod
    def dados(self):
        pass

    @abstractmethod
    def calculaRenda(self, mes, ano):
        pass


class Venda:
    def __init__(self, codigo, mes, ano, valor):
        self.__codigo = codigo
        self.__mes = mes
        self.__ano = ano
        self.__valor = valor

    @property
    def codigo(self):
        return self.__codigo

    @property
    def mes(self):
        return self.__mes

    @property
    def ano(self):
        return self.__ano

    @property
    def valor(self):
        return self.__valor


class Contratado(Vendedor):
    def __init__(self, codigo, nome, salario, nroCarteira):
        super().__init__(codigo, nome)
        self.__salario = salario
        self.__nroCarteira = nroCarteira

    @property
    def nroCarteira(self):
        return self.__nroCarteira

    @property
    def salario(self):
        return self.__salario

    @property
    def dados(self):
        return "Nome: {} - Nro Carteira: {}".format((self.nome), (self.nroCarteira))

    def calculaRenda(self, mes, ano):
        salario = self.salario
        for venda in self.vendas:
            if venda.mes == mes and venda.ano == ano:
                salario += venda.valor * 1 / 100
        return salario


class Comissionado(Vendedor):
    def __init__(self, codigo, nome, nroCPF, comissao):
        super().__init__(codigo, nome)
        self.__nroCPF = nroCPF
        self.__comissao = comissao

    @property
    def nroCPF(self):
        return self.__nroCPF

    @property
    def comissao(self):
        return self.__comissao

    @property
    def dados(self):
        return "Nome: {} - Nro CPF: {}".format((self.nome), (self.nroCPF))

    def calculaRenda(self, mes, ano):
        salario = 0
        comissao = self.comissao
        for venda in self.vendas:
            if venda.mes == mes and venda.ano == ano:
                salario += venda.valor * comissao / 100
        return salario


if __name__ == "__main__":
    funcContratado = Contratado(1001, "João da Silva", 2000, 1234)
    funcContratado.adicionaVenda(100, 3, 2022, 200000)
    funcContratado.adicionaVenda(101, 3, 2022, 300000)
    funcContratado.adicionaVenda(102, 4, 2022, 600000)
    funcComissionado = Comissionado(1002, "José Santos", 4321, 5)
    funcComissionado.adicionaVenda(200, 3, 2022, 200000)
    funcComissionado.adicionaVenda(201, 3, 2022, 400000)
    funcComissionado.adicionaVenda(202, 4, 2022, 500000)
    listaFunc = [funcContratado, funcComissionado]
    for func in listaFunc:
        print(func.dados)
        print("Renda no mês 3 de 2022: ")
        print(func.calculaRenda(3, 2022))
