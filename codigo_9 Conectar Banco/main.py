import database.conexao as conect
import database.CRUD as crud

def main():
    
    """Criei os seguintes códigos apenas para estudos. Porém como tabela e banco já estão criados deixarei como comentário para evitar erros. 
    O código é apenas para exemplificar a conexão, criação e desconexão do banco de dados."""
    
    while True:
            opcao = input("Deseja criar o banco de dados? (s/n): ").strip().lower()
            if opcao in ['s', 'n']:
                if opcao == 's':
                    conect.logging.info("Iniciando criação do banco de dados...")
                    try:
                        banco = conect.BancoDeDados()
                        banco.criar_banco()
                        conect.logging.info("Banco de dados criado com sucesso.")
                    except Exception as e:
                        conect.logging.error(f"Erro ao criar o banco de dados: {e}")
                    finally:
                        if banco:
                            try:
                                banco.desconectar_banco()
                                conect.logging.info("Desconectado do banco de dados.")
                            except Exception as e:
                                conect.logging.error(f"Erro ao desconectar: {e}")
                else:
                    conect.logging.info("Usuário não deseja criar um novo banco de dados")
                    break

            print("Opção inválida. Por favor, digite 's' para sim ou 'n' para não.")
  
    try:
        conect.BancoDeDados.conectar_banco()
        crud.criar_tabela()
        conect.logging.info("Tabelas criadas com sucesso.")
    except Exception as e:
        conect.logging.error(f"Erro ao criar tabelas: {e}")    
    


if __name__ == "__main__":
    main()