class Veiculo():
    def __init__(self):
        self.marca = "" # chave estranfeira para marca do veículo
        self.modelo = ""
        self.ano = 0
        self.cor = ""
        self.cpf = "" # chave estrangeira indicando o nome da pessoa dona do carro
        self.placa = "" #chave primaria

    def cadastrarVeiculo(self):
        print("Cadastro de veículo")
        self.marca = input("Digite a marca do veículo: ")
        self.modelo = input("Digite o modelo do veículo: ")
        self.cor = input("Digite a cor do veículo: ")
        self.cpf = input("Digite o CPF do proprietário: ")
        self.placa = input("Digite a placa do veículo: ")
    def atualizarDados(self):
        print('Atualizar cadastro')
        self.placa = input("Digite a placa do veículo que deseja atualizar: ")
        self.marca = input("Digite a nova marca do veículo: ")
        self.modelo = input("Digite o novo modelo do veículo: ")
        self.cor = input("Digite a nova cor do veículo: ")
        self.cpf = input("Digite o novo CPF do proprietário: ")
    def excluirVeiculo(self):
        print('Excluir cadastro')
        self.placa = input("Digite a placa do veículo que deseja excluir: ")
    def consultarVeiculo(self):
        print('Consultar cadastro')
        self.placa = input("Digite a placa do veículo que deseja consultar: ")
