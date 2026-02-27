import os

arquivo1 = open(r'Codigo_2\Dados1.txt') # caminho relativo
arquivo2 = open(r'C:\Users\Israe\OneDrive\Documentos\Projetos\FAC_DevRapidoPython\Codigo_2\Dados1.txt') # caminho absoluto

arquivo3 = open(r'Codigo_2\Documentos\dados2.txt')
arquivo4 = open(r'C:\Users\Israe\OneDrive\Documentos\Projetos\FAC_DevRapidoPython\Codigo_2\Documentos\dados2.txt')

print(os.path.realpath(arquivo1.name))
print(os.path.abspath(arquivo3.name))

print(arquivo1)
print(arquivo2)
print(arquivo3)
print(arquivo4)
arquivo1.close()
arquivo2.close()
arquivo3.close()
arquivo4.close()
