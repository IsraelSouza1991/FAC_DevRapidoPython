import sqlite3 as conector
import os
from pathlib import Path

class BancoDeDados():
    def __init__(self):
        self.nome_banco = None
        self.conexao = None
        self.cursor = None
        self.pasta_database = Path(__file__).parent  # Pasta onde esse arquivo está

    def criar_banco(self):
        try:
            while True:
                nome_banco = input("Digite o nome do banco de dados (com extensão .db): ")
                
                if not nome_banco.endswith('.db'):
                    print("O nome do banco de dados deve terminar com '.db'. Por favor, tente novamente.")
                    continue
                
                # Caminho completo do banco na pasta database
                caminho_banco = self.pasta_database / nome_banco
                
                if os.path.exists(caminho_banco):
                    print("Banco já existente.")
                    self.nome_banco = str(caminho_banco)
                    break
                else:
                    self.nome_banco = str(caminho_banco)
                    break
            
            self.conexao = conector.connect(self.nome_banco)
            print(f"Banco de dados criado em: {self.nome_banco}")
        except conector.DatabaseError as e:
            print(f"Erro ao criar o banco de dados: {e}")
        finally:
            if self.conexao:
                self.conexao.close()
                print("Conexão com o banco de dados fechada.")

    def conectar_banco(self):
        try:
            if not self.nome_banco:
                raise ValueError("Nome do banco não foi definido. Execute criar_banco() primeiro.")
            
            self.conexao = conector.connect(self.nome_banco)
            self.cursor = self.conexao.cursor()
            print(f"Conexão estabelecida com: {self.nome_banco}")
        except conector.DatabaseError as e:
            print(f"Erro de banco de dados: {e}")
            if self.conexao:
                self.conexao.close()
                
    def desconectar_banco(self):
        if self.conexao:
            self.conexao.close()
            print("Conexão com o banco de dados fechada.")
