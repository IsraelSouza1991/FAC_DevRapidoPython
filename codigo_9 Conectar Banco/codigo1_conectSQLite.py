import sqlite3 as conector

conexao = conector.connect("codigo_9 Conectar Banco/db_DevRapidoPython.db")

cursor = conexao.cursor()

dado = cursor.execute("SELECT * FROM teste")

print(dado.fetchall())

cursor.fetchall()
conexao.commit()

cursor.close()
conexao.close()