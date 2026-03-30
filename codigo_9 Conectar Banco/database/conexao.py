import sqlite3 as conector
import os
from pathlib import Path
import logging
import tkinter as tk
from tkinter import messagebox, filedialog

# Configurar logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

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
        """Abre um diálogo para selecionar um arquivo de banco de dados e se conecta."""
        try:
            # Criar janela raiz invisível para o filedialog
            root = tk.Tk()
            root.withdraw()  # Esconder a janela
            
            # Abrir diálogo de seleção de arquivo
            arquivo_banco = filedialog.askopenfilename(
                title="Selecionar banco de dados",
                initialdir=str(self.pasta_database),
                filetypes=[("Banco de Dados", "*.db"), ("Todos os arquivos", "*.*")]
            )
            
            root.destroy()
            
            if not arquivo_banco:
                messagebox.showwarning("Aviso", "Nenhum arquivo foi selecionado.")
                return False
            
            # Conectar ao banco selecionado
            self.nome_banco = arquivo_banco
            self.conexao = conector.connect(self.nome_banco)
            self.cursor = self.conexao.cursor()
            
            messagebox.showinfo("Sucesso", f"Conectado ao banco: {os.path.basename(arquivo_banco)}")
            logging.info(f"Conectado ao banco de dados: {self.nome_banco}")
            return True
            
        except conector.DatabaseError as e:
            messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {e}")
            logging.error(f"Erro ao conectar: {e}")
            return False
        except Exception as e:
            messagebox.showerror("Erro", f"Erro inesperado: {e}")
            logging.error(f"Erro inesperado: {e}")
            return False
                
    def desconectar_banco(self):
        """Desconecta do banco de dados."""
        try:
            if self.cursor:
                self.cursor.close()
            if self.conexao:
                self.conexao.close()
                logging.info("Desconectado do banco de dados.")
                return True
        except conector.DatabaseError as e:
            logging.error(f"Erro ao desconectar: {e}")
            return False

if __name__ == "__main__":
    banco = BancoDeDados()
    banco.criar_banco()
    banco.conectar_banco()
    banco.desconectar_banco()