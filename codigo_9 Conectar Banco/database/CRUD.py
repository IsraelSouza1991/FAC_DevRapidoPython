import sqlite3 as conector

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