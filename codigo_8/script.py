import os

def processar_arquivo(arquivo_origem, arquivo_destino):
    try:
        with open(arquivo_origem, 'r') as f_origem:
            conteudo = f_origem.read()
    except FileNotFoundError:
        print(f'Arquivo {arquivo_origem} não encontrado.')
        return
    except PermissionError:
        print(f'Sem permissão para ler {arquivo_origem}.')
        return
    except Exception as e:
        print(f"Erro inesperado ao ler {arquivo_origem}: {e}")

    try:
        with open(arquivo_destino,'w') as f_destino