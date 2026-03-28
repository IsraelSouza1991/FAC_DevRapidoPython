class Marca():

    def __init__(self):
        self.id = 0 # Chave primária
        self.nome = ""
        self.sigla = ""

    def cadastrarMarca(self):
        print("Cadastro de marca")
        self.id = int(input("Digite o ID da marca: "))
        self.nome = input("Digite o nome da marca: ")
        self.sigla = input("Digite a sigla da marca: ")
    def atualizarMarca(self):
        print("Atualizar marca")
        self.id = int(input("Digite o ID da marca que deseja atualizar: "))
        self.nome = input("Digite o novo nome da marca: ")
        self.sigla = input("Digite a nova sigla da marca: ")
    def excluirMarca(self):
        print("Excluir marca")
        self.id = int(input("Digite o ID da marca que deseja excluir: "))
    def consultarMarca(self):
        print("Consultar marca")
        self.id = int(input("Digite o ID da marca que deseja consultar: "))
