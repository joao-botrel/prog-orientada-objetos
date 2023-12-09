# João Vítor Botrel - 2022004251
from abc import ABC, abstractmethod
from datetime import date


class Transacao (ABC):
    def __init__(self, valor, data):
        self.__valor = valor
        self.__data = data

    @property
    def valor(self):
        return self.__valor

    @property
    def data(self):
        return self.__data


class Saque(Transacao):
    def __init__(self, valor, data, senha):
        super().__init__(valor, data)
        self.__senha = senha

    @property
    def senha(self):
        return self.__senha


class Deposito(Transacao):
    def __init__(self, valor, data, nomeDepositante):
        super().__init__(valor, data)
        self.__nomeDepositante = nomeDepositante

    @property
    def nomeDepositante(self):
        return self.__nomeDepositante


class Transferencia(Transacao):
    def __init__(self, valor, data, senha, tipoTransf):
        super().__init__(valor, data)
        self.__senha = senha
        self.__tipoTransf = tipoTransf

    @property
    def senha(self):
        return self.__senha

    @property
    def tipoTransf(self):
        return self.__tipoTransf


class Conta:
    def __init__(self, nroConta, nome, limite, senha):
        self.__nroConta = nroConta
        self.__nome = nome
        self.__limite = limite
        self.__senha = senha
        self.__transacoes = []
        self.__saldo = 0

    @property
    def nroConta(self):
        return self.__nroConta

    @property
    def nome(self):
        return self.__nome

    @property
    def limite(self):
        return self.__limite

    @property
    def senha(self):
        return self.__senha

    @property
    def transacoes(self):
        return self.__transacoes

    def adicionaDeposito(self, valor, data, nomeDepositante):
        self.__transacoes.append(Deposito(valor, data, nomeDepositante))
        return True

    def adicionaSaque(self, valor, data, senha):
        if senha != self.__senha:
            return False
        if self.calculaSaldo() >= valor:
            self.__transacoes.append(Saque(-valor, data, senha))
            return True
        else:
            return False

    def adicionaTransf(self, valor, data, senha, contaFavorecida):
        if senha != self.__senha:
            return False
        if self.calculaSaldo()+self.__limite >= valor:
            contaFavorecida.transacoes.append(
                Transferencia(valor, data, senha, 'D'))
            self.__transacoes.append(Transferencia(valor, data, senha, 'C'))
            return True
        else:
            return False

    def calculaSaldo(self):
        saldo = 0
        for transferencia in self.__transacoes:
            if type(transferencia) == Transferencia:
                if transferencia.tipoTransf == 'C':
                    saldo = saldo - transferencia.valor
                else:
                    saldo = saldo + transferencia.valor
            else:
                saldo += transferencia.valor
        return saldo+self.__limite


################################################################################
if __name__ == "__main__":
    c1 = Conta(1234, 'Jose da Silva', 1000, 'senha1')
    c1.adicionaDeposito(5000, date.today(), 'Antonio Maia')
    if c1.adicionaSaque(2000, date.today(), 'senha1') == False:
        print('Não foi possível realizar o saque no valor de 2000')
    if c1.adicionaSaque(1000, date.today(), 'senha-errada') == False:  # deve falhar
        print('Não foi possível realizar o saque no valor de 1000')
    c2 = Conta(4321, 'Joao Souza', 1000, 'senha2')
    c2.adicionaDeposito(3000, date.today(), 'Maria da Cruz')
    if c2.adicionaSaque(1500, date.today(), 'senha2') == False:
        print('Não foi possível realizar o saque no valor de 1500')
    if c2.adicionaTransf(5000, date.today(), 'senha2', c1) == False:  # deve falhar
        print('Não foi possível realizar a transf no valor de 5000')
    if c2.adicionaTransf(800, date.today(), 'senha2', c1) == False:
        print('Não foi possível realizar a transf no valor de 800')

print('--------')
print('Saldo de c1: {}'.format(c1.calculaSaldo()))  # deve imprimir 4800
print('Saldo de c2: {}'.format(c2.calculaSaldo()))  # deve imprimir 1700
