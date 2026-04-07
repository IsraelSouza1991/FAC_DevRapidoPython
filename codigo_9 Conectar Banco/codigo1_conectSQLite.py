import sqlite3 as conector

try:
    conexao = conector.connect("./db_DevRapidoPython.db")
    cursor = conexao.cursor()
    print("Conexão bem-sucedida!")
    cmd_create_pessoa = '''CREATE TABLE IF NOT EXISTS Pessoa (
                    cpf INTEGER NOT NULL,
                    nome TEXT NOT NULL,
                    nascimento DATE NOT NULL,
                    oculos BOOLEAN NOT NULL,
                    PRIMARY KEY (cpf)
                    );'''
    cmd_create_marca = '''CREATE TABLE IF NOT EXISTS Marca (
                    id INTEGER NOT NULL,
                    nome TEXT NOT NULL,
                    sigla CHARACTER(2) NOT NULL,
                    PRIMARY KEY (id)
                    );'''
    cmd_create_veiculo = '''CREATE TABLE IF NOT EXISTS Veiculo (
                    placa CHARACTER(7) NOT NULL,
                    ano INTEGER NOT NULL,
                    cor TEXT NOT NULL,
                    proprietario INTEGER NOT NULL,
                    marca INTEGER NOT NULL,
                    PRIMARY KEY (placa),
                    FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
                    FOREIGN KEY(marca) REFERENCES Marca(id)
                    );'''
    cursor.execute(cmd_create_pessoa)
    cursor.execute(cmd_create_marca)
    cursor.execute(cmd_create_veiculo)
    conexao.commit()
except conector.DatabaseError as err:
    print(f"Erro ao conectar ao banco de dados: {err}")
finally:
    if conexao:
        cursor.close()
        conexao.close()