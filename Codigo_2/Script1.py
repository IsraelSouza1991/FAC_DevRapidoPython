import os

print(os.getcwd())
print("olá")

arquivo1 = open('Codigo_2/Documentos/Dados1.txt', "r") #caminho absoluto
arquivo2 = open('Codigo2/dados2.txt', "r") #caminho relativo

print(os.path.abspath(arquivo1.name)) 
print(os.path.relpath(arquivo2.name))

print(arquivo1)
print(arquivo2)