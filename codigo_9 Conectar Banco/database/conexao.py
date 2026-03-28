import sqlite3 as conector

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
