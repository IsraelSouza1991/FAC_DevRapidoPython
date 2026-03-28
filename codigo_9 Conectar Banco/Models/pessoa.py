class Pessoa():
    #Atributos
    def __init__(self):
        self.nome = ' '
        self.cpf = '123.456.789-00' #considerar chave primária
        self.data_nascimento = '00/00/0000'
        self.oculos = False
    #Métodos
    def cadastrarPessoa(self):
        print("Cadastro de pessoa")
        self.nome = input("Digite o nome: ")
        self.cpf = input("Digite o CPF: ")
        self.data_nascimento = input("Digite a data de nascimento: ")
        oculos_input = input("Usa óculos? (s/n): ")
        self.oculos = oculos_input.lower().strip() == 's'
    def atualizarDados(self):
        print('Atualizar cadastro')
        self.cpf = input("Digite o CPF da pessoa que deseja atualizar: ")
        self.nome = input("Digite o novo nome: ")
        self.data_nascimento = input("Digite a nova data de nascimento: ")
        oculos_input = input("Usa óculos? (s/n): ")
        self.oculos = oculos_input.lower().strip() == 's'
    def excluirPessoa(self):
        print('Excluir cadastro')
        self.cpf = input("Digite o CPF da pessoa que deseja excluir: ")
    def consultarPessoa(self):
        print('Consultar cadastro')
        self.cpf = input("Digite o CPF da pessoa que deseja consultar: ")
