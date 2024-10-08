from abc import ABC, abstractmethod

banco_dados = {'Alunos': {},
               'Visitantes': {},
               'Restaurantes': {},
               'Funcionario_Depae': {}}


class Usuario(ABC):
    def __init__(self, nome, email, senha, n_telefone, cpf):
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__n_telefone = n_telefone
        self.__cpf = cpf

    @abstractmethod
    def cadastrar(self):
        pass

    @abstractmethod
    def logar(self):
        pass

    # get
    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_senha(self):
        return self.__senha

    def get_n_telefone(self):
        return self.__n_telefone

    def get_cpf(self):
        return self.__cpf

    # set
    def set_nome(self, nome):
        self.__nome = nome

    def set_email(self, email):
        self.__email = email

    def set_senha(self, senha):
        self.__senha = senha

    def set_n_telefone(self, n_telefone):
        self.__n_telefone = n_telefone

    def set_cpf(self, cpf):
        self.__cpf = cpf


# Aluno-----------------------------------------------------------------------------------------
class Aluno(Usuario):
    def __init__(self, nome, email, senha, n_telefone, cpf, curso, turma, matricula):
        super().__init__(nome, email, senha, n_telefone, cpf)

        self.__curso = curso
        self.__turma = turma
        self.__matricula = matricula

    # get
    def get_curso(self):
        return self.__curso

    def get_turma(self):
        return self.__turma

    def get_matricula(self):
        return self.__matricula

    # set
    def set_curso(self, curso):
        self.__curso = curso

    def set_turma(self, turma):
        self.__turma = turma

    def set_matricula(self, matricula):
        self.__matricula = matricula

    # cadastro
    def cadastrar(self):
        if self.__matricula in banco_dados["Alunos"]:
            print('Aluno já cadastrado.')

        else:
            banco_dados['Alunos'][self.__matricula] = {'nome': self.get_nome(),
                                                       'email': self.get_email(),
                                                       'senha': self.get_senha(),
                                                       'n_telefone': self.get_n_telefone(),
                                                       'curso': self.get_curso(),
                                                       'turma': self.get_turma(),
                                                       'cpf': self.get_cpf(),
                                                       'matricula': self.get_matricula()}
            print('Aluno cadastrado com sucesso.')

    # login
    def logar(self):
        if self.get_matricula() in banco_dados['Alunos'] and self.get_senha() == \
                banco_dados['Alunos'][self.__matricula]['senha']:
            print(f'Aluno {self.get_nome()} logado com sucesso!\n')

        else:
            print('Usuário ou senha incorreto.\n')


# Restaurante-----------------------------------------------------------------------------------------------------

class Restaurante(Usuario):
    def __init__(self, nome, email, senha, n_telefone, cpf, cnpj, nomeEmpresa):
        super().__init__(nome, email, senha, n_telefone, cpf)

        self.__cnpj = cnpj
        self.__nomeEmpresa = nomeEmpresa

    # get
    def get_cnpj(self):
        return self.__cnpj

    def get_nomeEmpresa(self):
        return self.__nomeEmpresa

    # set
    def set_cnpj(self, cnpj):
        self.__cnpj = cnpj

    def set_cpfDono(self, nomeEmpresa):
        self.__nomeEmpresa = nomeEmpresa

    # Cadastro
    def cadastrar(self):
        if self.__cnpj in banco_dados["Restaurantes"]:
            print("Restaurante já cadastrado.")
        else:
            banco_dados['Restaurantes'][self.__cnpj] = {'nome': self.get_nome(),
                                                        'email': self.get_email(),
                                                        'senha': self.get_senha(),
                                                        'n_telefone': self.get_n_telefone(),
                                                        'cnpj': self.get_cnpj(),
                                                        'cpf_dono': self.get_nomeEmpresa()}
            print('Restaurante cadastrado com sucesso!')

    # Login
    def logar(self):
        if self.get_cnpj() in banco_dados['Restaurantes'] and self.get_senha() == \
                banco_dados['Restaurantes'][self.__cnpj]['senha']:
            print(F'{self.__nomeEmpresa} Logado com sucesso!\n')

        else:
            print('Usuário ou senha incorreto.\n')


# Visitantes-----------------------------------------------------------------------------------------------------

class Visitantes(Usuario):
    def __init__(self, nome, email, senha, n_telefone, cpf):
        super().__init__(nome, email, senha, n_telefone, cpf)

        self.__cpf = cpf

    # Cadastro
    def cadastrar(self):
        if self.__cpf in banco_dados['Visitantes']:
            print("visitante já cadastrado")

        else:
            banco_dados['Visitantes'][self.__cpf] = {'nome': self.get_nome(),
                                                     'email': self.get_email(),
                                                     'senha': self.get_senha(),
                                                     'n_telefone': self.get_n_telefone(),
                                                     'cpf': self.get_cpf()}
            print("Visitante cadsatrado com sucesso!")

    # Login
    def logar(self):
        if self.get_cpf() in banco_dados['Visitantes'] and self.get_senha() == banco_dados['Visitantes'][self.__cpf][
            'senha']:
            print(f'Visitante {self.get_nome()} logado com sucesso\n')

        else:
            print('Usuário ou senha incorreto.\n')


# Funcionário Depae-----------------------------------------------------------------------------------------------------

class Func_Depae(Usuario):
    def __init__(self, nome, email, senha, n_telefone, cpf, siape):
        super().__init__(nome, email, senha, n_telefone, cpf)

        self.__siape = siape

    # get
    def get_siape(self):
        return self.__siape

    # set
    def set_siape(self, siape):
        self.__siape = siape

    # Cadastro
    def cadastrar(self):
        if self.__siape in banco_dados["Funcionario_Depae"]:
            print("Funcionário já cadastrado!")

        else:
            banco_dados['Funcionario_Depae'][self.__siape] = {'nome': self.get_nome(),
                                                              'email': self.get_email(),
                                                              'senha': self.get_senha(),
                                                              'n_telefone': self.get_n_telefone(),
                                                              'siape': self.get_siape(),
                                                              'cpf': self.get_cpf()}
            print("Funcionário cadastrado com sucesso!")

    # Login
    def logar(self):

        if self.get_siape() in banco_dados['Funcionario_Depae'] and self.get_senha() == \
                banco_dados['Funcionario_Depae'][self.__siape]['senha']:
            print(f'Funcionário do Depae {self.get_nome()} logado com sucesso!\n')

        else:
            print('Usuário ou senha incorreto.\n')

# -----------------------------------------------------------------------------------------------------