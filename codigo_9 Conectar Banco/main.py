import logging
import database.conexao as conect
import database.CRUD as crud

# Configurar logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    """
    Criei os seguintes códigos apenas para estudos. Porém como tabela e banco já estão criados deixarei como comentário para evitar erros. 
    O código é apenas para exemplificar a conexão, criação e desconexão do banco de dados.
    
    banco = None
    try:
        banco = conect.BancoDeDados()
        logging.info("Iniciando operações com o banco de dados...")
        
        banco.criar_banco()
        logging.info("Banco de dados criado com sucesso.")
        
        banco.conectar_banco()
        logging.info("Conexão estabelecida com sucesso.")
        
        # Adicione aqui suas operações com o banco
        
    except Exception as e:
        logging.error(f"Erro ao operar o banco de dados: {e}")
    finally:
        if banco:
            try:
                banco.desconectar_banco()
                logging.info("Desconectado do banco de dados.")
            except Exception as e:
                logging.error(f"Erro ao desconectar: {e}")
    try:
        crud.criar_tabela(banco)
        logging.info("Tabelas criadas com sucesso.")
    except Exception as e:
        logging.error(f"Erro ao criar tabelas: {e}")    
    """
    

if __name__ == "__main__":
    main()