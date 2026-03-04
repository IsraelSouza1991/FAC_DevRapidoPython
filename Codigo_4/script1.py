arquivo = open('dados.txt','r')
for linha in arquivo:
    print(repr(linha))

arquivo.close()