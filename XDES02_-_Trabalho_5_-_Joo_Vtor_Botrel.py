
import random
from abc import ABC, abstractclassmethod
from datetime import date


class Transacao:
    def __init__(self, valor, data):
        self.__valor = valor
        self.__data = data
        if valor > 0:
            self.__descricao = "crédito"
        elif valor < 0:
            self.__descricao = "débito"

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    def imprimir_transacao(self):
        print("descrição: {}".format(self.descricao))
        print("valor:     {}".format(self.valor))
        print("data:      {}".format(self.data))


class Conta(ABC):
    def __init__(self, nome):
        self.__nome = nome
        self.__numero_conta = int(random.random() * 100000000)
        self.__saldo = 0
        self.__transacoes = []

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    @property
    def numero_conta(self):
        return self.__numero_conta

    @numero_conta.setter
    def numero_conta(self, numero_conta):
        self.__numero_conta = numero_conta

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def transacoes(self):
        return self.__transacoes

    @abstractclassmethod
    def imprimir_extratos(self):
        pass

    def imprime_atributos(self):
        print("Nome:     {}".format(self.nome))
        print("N° conta: {}".format(self.numero_conta))
        print("Saldo:    {}".format(self.saldo))
        print("Extrato:")
        for transacao in self.transacoes:
            transacao.imprimir_transacao()
            print("------")

    def retirada(self, valor):
        if valor > self.saldo:
            print("Não tem saldo suficiente")
        elif valor <= 0:
            print("valor invalido")
        else:
            self.transacoes.append(Transacao(-valor, date.today()))
            self.saldo -= valor

    def deposito(self, valor):
        if valor > 0:
            self.transacoes.append(Transacao(valor, date.today()))
            self.saldo += valor
        else:
            print("O valor é inválido, tente novamente.")


class Conta_Poupanca(Conta):
    def __init__(self, nome):
        super().__init__(nome)
        self.__aniversario = date.today()

    @property
    def aniversario(self):
        return self.__aniversario

    @aniversario.setter
    def aniversario(self, data):
        self.__aniversario = data

    def imprimir_extratos(self):
        self.imprime_atributos()
        print("A conta foi criada em: {}".format(self.aniversario))


class Conta_limite(Conta):
    def __init__(self, nome, limite):
        super().__init__(nome)
        self.__limite = -limite

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        if valor > 0:
            self.__limite = -valor
        else:
            self.__limite = valor

    def retirada(self, valor):
        if self.saldo < self.limite:
            print("Não tem saldo suficiente!")
        elif valor <= 0:
            print("Valor inválido!")
        else:
            self.transacoes.append(Transacao(-valor, date.today()))
            self.saldo -= valor

    def imprimir_extratos(self):
        self.imprime_atributos()
        print("Limite: {}".format(self.limite))


class Conta_Corrente(Conta):
    def __init__(self, nome):
        super().__init__(nome)

    def imprimir_extratos(self):
        self.imprime_atributos()


if __name__ == "__main__":
    conta_corrente = Conta_Corrente("Rafaela")
    conta_limite = Conta_limite("João", 1500)
    conta_poupanca = Conta_Poupanca("Matheus")

    """ operações conta_limite: """
    conta_limite.deposito(1500)
    conta_limite.retirada(700)
    conta_limite.retirada(700)
    conta_limite.retirada(700)
    conta_limite.retirada(700)

    """ operações conta_corrente: """
    conta_corrente.deposito(1500)
    conta_corrente.retirada(700)
    conta_corrente.retirada(700)

    """ operações conta_poupanca: """
    conta_poupanca.deposito(1500)
    conta_poupanca.retirada(700)
    conta_poupanca.retirada(700)

    lista_contas = [conta_corrente, conta_limite, conta_poupanca]
    for conta in lista_contas:
        conta.imprimir_extratos()
        print()

    conta_limite.limite = 2000
    conta_limite.imprimir_extratos()
