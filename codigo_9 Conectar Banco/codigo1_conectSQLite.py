import sqlite3 as conector

conexao = conector.connect(".\\db_DevRapidoPython")

cursor = conexao.cursor()

dado = cursor.execute("SELECT * FROM teste")

print(dado.fetchall())

cursor.fetchall()
conexao.commit()