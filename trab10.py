# João Vítor Botrel - 2022004251


from abc import abstractmethod, ABC


class Pessoa (ABC):
    def __init__(self, nome, cpf, endereco, idade):
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def endereco(self):
        return self.__endereco

    @property
    def idade(self):
        return self.__idade

    @abstractmethod
    def printDescricao(self):
        pass


class Professor (Pessoa):
    def __init__(self, nome, cpf, endereco, idade, titulacao):
        super().__init__(nome, cpf, endereco, idade)
        self.__titulacao = titulacao

    @property
    def titulacao(self):
        return self.__titulacao

    def printDescricao(self):
        print("Nome: {}".format(self.nome))
        print("CPF: {}".format(self.cpf))
        print("Endereco: {}".format(self.endereco))
        print("Idade: {}".format(self.idade))
        print("Titulacao: {}".format(self.titulacao))


class Aluno (Pessoa):
    def __init__(self, nome, cpf, endereco, idade, curso):
        super().__init__(nome, cpf, endereco, idade)
        self.__curso = curso

    @property
    def curso(self):
        return self.__curso

    def printDescricao(self):
        print("Nome: {}".format(self.nome))
        print("CPF: {}".format(self.cpf))
        print("Endereco: {}".format(self.endereco))
        print("Idade: {}".format(self.idade))
        print("Curso: {}".format(self.curso))


class titulacaoError (Exception):
    pass


class idadeError (Exception):
    pass


class cursoError (Exception):
    pass


class cpfError (Exception):
    pass


if __name__ == "__main__":
    lista = []
    prof1 = Professor("José", "12345678910",
                      "Av. Industrial, 10", 31, "Doutor")
    prof2 = Professor("Maria", "12345678901", "Av. Mario, 11", 23, "Superior")
    aluno1 = Aluno("Carla", "12345678910", "Av. Esdras, 12", 21, "SIN")
    aluno2 = Aluno("Pedro", "12345678109", "Av. Domingos, 13", 17, "CCO")
    aluno3 = Aluno("João", "12345678108", "Av. Ribeiros, 14", 19, "ADM")
    aluno4 = Aluno("Vitor", "12345678107", "Av. Alcantara, 15", 20, "CCO")
    lista.append(prof1)
    lista.append(prof2)
    lista.append(aluno1)
    lista.append(aluno2)
    lista.append(aluno3)
    lista.append(aluno4)
    cadastro = {}

    for pessoa in lista:
        try:
            if type(pessoa) == Professor and pessoa.titulacao != "Doutor":
                raise titulacaoError
            if type(pessoa) == Professor and pessoa.idade <= 30:
                raise idadeError
            if type(pessoa) == Aluno and pessoa.curso != "CCO" and pessoa.curso != "SIN":
                raise cursoError
            if type(pessoa) == Aluno and pessoa.idade <= 18:
                raise idadeError
            if pessoa.cpf in cadastro:
                raise cpfError
        except titulacaoError:
            print()
            print("ERRO! A titulação não é suficiente para ser professor.")
            print()
        except idadeError:
            print()
            print("ERRO! A idade não é suficiente")
            print()
        except cursoError:
            print()
            print("ERRO! O curso deve ser CCO ou SIN.")
            print()
        except cpfError:
            print()
            print("ERRO! Cpf já cadastrado")
            print()
        else:
            cadastro[pessoa.cpf] = pessoa
            print()
            print("Usuário cadastrado com sucesso!")
            pessoa.printDescricao()
