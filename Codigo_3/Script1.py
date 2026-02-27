with open("Dados.txt", 'r') as arquivo:
    conteudo = arquivo.readline()
    print(conteudo)
    print(arquivo.name)
    print(arquivo.mode)
print(arquivo.closed)

