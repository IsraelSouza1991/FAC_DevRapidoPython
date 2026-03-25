import sqlite3 as conector
import os

class Pessoa():
    #Atributos
    def __init__(self):
        self.nome = ' '
        self.cpf = '123.456.789-00' #considerar chave primária
        self.data_nascimento = '00/00/0000'
        self.oculos = False
    #Métodos
    def cadastrarPessoa(self):
        print("Cadastro de pessoa")
        self.nome = input("Digite o nome: ")
        self.cpf = input("Digite o CPF: ")
        self.data_nascimento = input("Digite a data de nascimento: ")
        oculos_input = input("Usa óculos? (s/n): ")
        self.oculos = oculos_input.lower().strip() == 's'
    def atualizarDados(self):
        print('Atualizar cadastro')
        self.cpf = input("Digite o CPF da pessoa que deseja atualizar: ")
        self.nome = input("Digite o novo nome: ")
        self.data_nascimento = input("Digite a nova data de nascimento: ")
        oculos_input = input("Usa óculos? (s/n): ")
        self.oculos = oculos_input.lower().strip() == 's'
    def excluirPessoa(self):
        print('Excluir cadastro')
        self.cpf = input("Digite o CPF da pessoa que deseja excluir: ")
    def consultarPessoa(self):
        print('Consultar cadastro')
        self.cpf = input("Digite o CPF da pessoa que deseja consultar: ")

class Veiculo():
    def __init__(self):
        self.marca = "" # chave estranfeira para marca do veículo
        self.modelo = ""
        self.ano = 0
        self.cor = ""
        self.cpf = "" # chave estrangeira indicando o nome da pessoa dona do carro
        self.placa = "" #chave primaria

    def cadastrarVeiculo(self):
        print("Cadastro de veículo")
        self.marca = input("Digite a marca do veículo: ")
        self.modelo = input("Digite o modelo do veículo: ")
        self.cor = input("Digite a cor do veículo: ")
        self.cpf = input("Digite o CPF do proprietário: ")
        self.placa = input("Digite a placa do veículo: ")
    def atualizarDados(self):
        print('Atualizar cadastro')
        self.placa = input("Digite a placa do veículo que deseja atualizar: ")
        self.marca = input("Digite a nova marca do veículo: ")
        self.modelo = input("Digite o novo modelo do veículo: ")
        self.cor = input("Digite a nova cor do veículo: ")
        self.cpf = input("Digite o novo CPF do proprietário: ")
    def excluirVeiculo(self):
        print('Excluir cadastro')
        self.placa = input("Digite a placa do veículo que deseja excluir: ")
    def consultarVeiculo(self):
        print('Consultar cadastro')
        self.placa = input("Digite a placa do veículo que deseja consultar: ")

class Marca():

    def __init__(self):
        self.id = 0 # Chave primária
        self.nome = ""
        self.sigla = ""

    def cadastrarMarca(self):
        print("Cadastro de marca")
        self.id = int(input("Digite o ID da marca: "))
        self.nome = input("Digite o nome da marca: ")
        self.sigla = input("Digite a sigla da marca: ")
    def atualizarMarca(self):
        print("Atualizar marca")
        self.id = int(input("Digite o ID da marca que deseja atualizar: "))
        self.nome = input("Digite o novo nome da marca: ")
        self.sigla = input("Digite a nova sigla da marca: ")
    def excluirMarca(self):
        print("Excluir marca")
        self.id = int(input("Digite o ID da marca que deseja excluir: "))
    def consultarMarca(self):
        print("Consultar marca")
        self.id = int(input("Digite o ID da marca que deseja consultar: "))

# Conexão com o banco de dados SQLite
class BancoDeDados():
    def __init__(self):
        self.nome_banco = None
        self.conexao = None
        self.cursor = None

    def criar_banco(self):
        try:
            while True:
                nome_banco = input("Digite o nome do banco de dados (com extensão .db): ")
                if not nome_banco.endswith('.db'):
                    print("O nome do banco de dados deve terminar com '.db'. Por favor, tente novamente.")
                    continue
                if os.path.exists(nome_banco):
                    print("Banco já existente.")
                    break
                else:
                    self.nome_banco = nome_banco
                    break
            self.conexao = conector.connect(self.nome_banco)
            print("Banco de dados criado com sucesso!")
        except conector.DatabaseError as e:
            print(f"Erro ao criar o banco de dados: {e}")
        finally:
            if self.conexao:
                self.conexao.close()
                print("Conexão com o banco de dados fechada.")

    def conectar_banco(self):
        try:
            self.conexao = conector.connect(self.nome_banco)
            print("Conexão com o banco de dados estabelecida com sucesso!")
        except conector.DatabaseError as e:
            print(f"Erro de banco de dados: {e}")
        finally:
            if self.conexao:
                self.conexao.close()
                print("Conexão com o banco de dados fechada.")
                
    def desconectar_banco(self):
        if self.conexao:
            self.conexao.close()
            print("Conexão com o banco de dados fechada.")

    def criar_tabela(self):
        try:
            self.conectar_banco()
            self.cursor = self.conexao.cursor()
            self.cursor.execute('''CREATE TABLE Pessoa (
                                    cpf TEXT NOT NULL,
                                    nome TEXT NOT NULL,
                                    nascimento DATE NOT NULL,
                                    oculos BOOLEAN NOT NULL,
                                    PRIMARY KEY (cpf)
                                    );''')
            self.cursor.execute('''CREATE TABLE Marca (
                                    id INTEGER NOT NULL,
                                    nome TEXT NOT NULL,
                                    sigla TEXT NOT NULL,
                                    PRIMARY KEY (id)
                                    );''')
            self.cursor.execute('''CREATE TABLE Veiculo (
                                    placa CHARACTER(7) NOT NULL,
                                    ano INTEGER NOT NULL,
                                    cor TEXT NOT NULL,
                                    proprietario TEXT NOT NULL,
                                    marca INTEGER NOT NULL,
                                    PRIMARY KEY (placa),
                                    FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
                                    FOREIGN KEY(marca) REFERENCES Marca(id)
                                    );''')
            self.conexao.commit()
            print("Tabelas criadas com sucesso!")
        except conector.DatabaseError as e:
            print(f"Erro ao criar as tabelas: {e}")
        finally:
            self.desconectar_banco()

