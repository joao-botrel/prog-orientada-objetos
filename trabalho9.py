# João Vítor Botrel - 2022004251

from abc import ABC, abstractmethod


class Funcionario (ABC):
    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome
        self.__pontoMensalFunc = []

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nome(self):
        return self.__nome

    @property
    def pontoMensalFunc(self):
        return self.__pontoMensalFunc

    def adicionaPonto(self, mes, ano, falta, atrasos):
        return self.__pontoMensalFunc.append(PontoFunc(mes, ano, falta, atrasos))

    def lancaFaltas(self, mes, ano, faltas):
        for pontoMensal in self.__pontoMensalFunc:
            if mes == pontoMensal.mes and ano == pontoMensal.ano:
                pontoMensal.lancaFaltas = faltas

    def lancaAtrasos(self, mes, ano, atrasos):
        for pontoMensal in self.__pontoMensalFunc:
            if mes == pontoMensal.mes and ano == pontoMensal.ano:
                pontoMensal.lancaAtrasos = atrasos

    def imprimeFolha(self, mes, ano):
        print("Código: {}".format(self.codigo))
        print("Nome: {}".format(self.nome))
        print("Salário líquido: {}".format(self.calculaSalario(mes, ano)))
        print("Bonus: {}".format(self.calculaBonus(mes, ano)))

    @abstractmethod
    def calculaSalario(self, mes, ano):
        pass

    @abstractmethod
    def calculaBonus(self, mes, ano):
        pass


class PontoFunc:
    def __init__(self, mes, ano, nroFaltas, nroAtrasos):
        self.__mes = mes
        self.__ano = ano
        self.__nroFaltas = nroFaltas
        self.__nroAtrasos = nroAtrasos

    @property
    def mes(self):
        return self.__mes

    @property
    def ano(self):
        return self.__ano

    @property
    def nroFaltas(self):
        return self.__nroFaltas

    @property
    def nroAtrasos(self):
        return self.__nroAtrasos

    @nroFaltas.setter
    def lancaFaltas(self, nroFaltas):
        self.__nroFaltas = nroFaltas

    @nroAtrasos.setter
    def lancaAtrasos(self, nroAtrasos):
        self.__nroAtrasos = nroAtrasos


class Professor(Funcionario):
    def __init__(self, codigo, nome, titulacao, salarioHora, nroAulas):
        super().__init__(codigo, nome)
        self.__titulacao = titulacao
        self.__salarioHora = salarioHora
        self.__nroAulas = nroAulas

    @property
    def titulacao(self):
        return self.__titulacao

    @property
    def salarioHora(self):
        return self.__salarioHora

    @property
    def nroAulas(self):
        return self.__nroAulas

    def calculaSalario(self, mes, ano):
        salarioProf = 0
        for pontoMensal in self.pontoMensalFunc:
            if mes == pontoMensal.mes and ano == pontoMensal.ano:
                salarioProf = (self.__salarioHora*self.__nroAulas) - \
                    (self.__salarioHora*pontoMensal.nroFaltas)
        return salarioProf

    def calculaBonus(self, mes, ano):
        bonus = 10
        for pontoMensal in self.pontoMensalFunc:
            if mes == pontoMensal.mes and ano == pontoMensal.ano:
                bonus = bonus - pontoMensal.nroAtrasos
                if (bonus > 0):
                    return self.calculaSalario(mes, ano) * bonus/100
                else:
                    return 0


class TecAdmin (Funcionario):
    def __init__(self, codigo, nome, funcao, salarioMensal):
        super().__init__(codigo, nome)
        self.__funcao = funcao
        self.__salarioMensal = salarioMensal

    @property
    def funcao(self):
        return self.__funcao

    @property
    def salarioMensal(self):
        return self.__salarioMensal

    def calculaSalario(self, mes, ano):
        salarioTec = 0
        for pontoMensal in self.pontoMensalFunc:
            if mes == pontoMensal.mes and ano == pontoMensal.ano:
                salarioTec = self.__salarioMensal - \
                    ((self.__salarioMensal/30)*pontoMensal.nroFaltas)
        return salarioTec

    def calculaBonus(self, mes, ano):
        bonus = 8
        for pontoMensal in self.pontoMensalFunc:
            if mes == pontoMensal.mes and ano == pontoMensal.ano:
                bonus = bonus - pontoMensal.nroAtrasos
                if (bonus > 0):
                    return self.calculaSalario(mes, ano) * bonus/100
                else:
                    return 0


if __name__ == "__main__":
    funcionarios = []
    prof = Professor(1, "Joao", "Doutor", 45.35, 32)
    prof.adicionaPonto(4, 2021, 0, 0)
    prof.lancaFaltas(4, 2021, 2)
    prof.lancaAtrasos(4, 2021, 3)
    funcionarios.append(prof)
    tec = TecAdmin(2, "Pedro", "Analista Contábil", 3600)
    tec.adicionaPonto(4, 2021, 0, 0)
    tec.lancaFaltas(4, 2021, 3)
    tec.lancaAtrasos(4, 2021, 4)
    funcionarios.append(tec)
    for func in funcionarios:
        func.imprimeFolha(4, 2021)
        print()
