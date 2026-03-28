import database.conexao as conect
def main():
    banco = conect.BancoDeDados()
    banco.criar_banco()
    banco.conectar_banco()
    banco.desconectar_banco()

if __name__ == "__main__":
    main()