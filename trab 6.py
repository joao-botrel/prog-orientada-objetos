class aluno:
    def __init__(self, nro_matr, nome, curso, historico=None):
        self.__nro_matr = nro_matr
        self.__nome = nome
        self.__curso = curso
        self.__historico = historico

        curso.add_alunos(self)

    def get_nro_matr(self):
        return self.__nro_matr

    def get_nome(self):
        return self.__nome

    def get_curso(self):
        return self.__curso

    def get_historico(self):
        return self.__historico

    def cria_historico(self):
        self.__historico = historico(self)

    def inserir_disciplina_hist(self, disciplina):
        self.__historico.add_disciplina(disciplina)


class curso:

    def __init__(self, nome, grade=None):
        self.__nome = nome
        self.__alunos = []
        self.__grade = grade

    def get_nome(self):
        return self.__nome

    def get_alunos(self):
        return self.__alunos

    def get_grade(self):
        return self.__grade

    def add_alunos(self, aluno):
        self.__alunos.append(aluno)

    def cria_grade(self, ano):
        self.__grade = grade(ano, self)


class grade:

    def __init__(self, ano, curso):
        self.__ano = ano
        self.__curso = curso
        self.__disciplinas = []

    def get_ano(self):
        return self.__ano

    def get_curso(self):
        return self.__curso

    def get_disciplinas(self):
        return self.__disciplinas

    def add_disciplinas(self, disciplina):
        self.__disciplinas.append(disciplina)


class disciplina:

    def __init__(self, codigo, nome, carga_hr, grade, historico=None):
        self.__codigo = codigo
        self.__nome = nome
        self.__carga_hr = carga_hr
        self.__grade = grade
        self.__historico = historico

    def get_codigo(self):
        return self.__codigo

    def get_nome(self):
        return self.__nome

    def get_carga_hr(self):
        return self.__carga_hr

    def get_grade(self):
        return self.__grade

    def get_historico(self):
        return self.__historico


class historico:

    def __init__(self, aluno):
        self.__aluno = aluno
        self.__disciplinas = []

    def get_aluno(self):
        return self.__aluno

    def get_disciplinas(self):
        return self.__disciplinas

    def add_disciplina(self, disciplina):
        self.__disciplinas.append(disciplina)


if __name__ == "__main__":
    carga_h_total_obr = 0
    carga_h_total_ele = 0
    curso1 = curso('CCO')
    curso2 = curso('ADM')
    curso1.cria_grade(2021)
    curso2.cria_grade(2021)
    aluno1 = aluno(2021001714, 'Eduarda', curso1)
    aluno1.cria_historico()

    disc1 = disciplina(1, 'XDES01', 16, curso1.get_grade())
    disc2 = disciplina(2, 'XDES02', 32, curso1.get_grade())
    disc3 = disciplina(3, 'XDES03', 96, curso1.get_grade())

    disc4 = disciplina(10, 'IEPG01', 64, curso2.get_grade())
    disc5 = disciplina(11, 'IEPG02', 64, curso2.get_grade())
    disc6 = disciplina(12, 'IEPG03', 40, curso2.get_grade())

    curso1.get_grade().add_disciplinas(disc1)
    curso1.get_grade().add_disciplinas(disc2)
    curso1.get_grade().add_disciplinas(disc3)
    curso2.get_grade().add_disciplinas(disc4)
    curso2.get_grade().add_disciplinas(disc5)
    curso2.get_grade().add_disciplinas(disc6)

    aluno1.inserir_disciplina_hist(disc1)
    aluno1.inserir_disciplina_hist(disc2)
    aluno1.inserir_disciplina_hist(disc4)

    if aluno1.get_curso() == curso1:
        for j in curso1.get_grade().get_disciplinas():
            for i in aluno1.get_historico().get_disciplinas():
                if j == i:
                    print('OBRIGATÓRIA\n{} Código {} -> Carga Horária: {} horas\n'.format(
                        i.get_nome(), i.get_codigo(), i.get_carga_hr()))
                    carga_h_total_obr += i.get_carga_hr()
                    break

        for j in curso2.get_grade().get_disciplinas():
            for i in aluno1.get_historico().get_disciplinas():
                if j == i:
                    print('ELETIVA\n{} Código {} -> Carga Horária: {} horas\n'.format(
                        i.get_nome(), i.get_codigo(), i.get_carga_hr()))
                    carga_h_total_ele += i.get_carga_hr()
                    break
    else:
        for j in curso2.get_grade().get_disciplinas():
            for i in aluno1.get_historico().get_disciplinas():
                if j == i:
                    print('OBRIGATÓRIA\n{} Código {} -> Carga Horária: {} horas\n'.format(
                        i.get_nome(), i.get_codigo(), i.get_carga_hr()))
                    carga_h_total_obr += i.get_carga_hr()
                    break

        for j in curso1.get_grade().get_disciplinas():
            for i in aluno1.get_historico().get_disciplinas():
                if j == i:
                    print('ELETIVA\n{} Código {} -> Carga Horária: {} horas\n'.format(
                        i.get_nome(), i.get_codigo(), i.get_carga_hr()))
                    carga_h_total_ele += i.get_carga_hr()
                    break

    print(f'Carga Horária total das disciplinas obrigatórias cursadas: {carga_h_total_obr} horas')

    print(f'Carga Horária total das disciplinas eletivas cursadas: {carga_h_total_ele} horas')
