import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def check_file_exists(file_name):

    # Define o caminho base relativo ao diretório do script atual
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resources'))
    # Combina o caminho base com o nome do arquivo fornecido
    full_path = os.path.join(base_path, file_name)
    # Verifica se o arquivo existe no caminho combinado
    return os.path.isfile(full_path)

def main():
    print(check_file_exists("30062024-Magic_Kingdom.csv"))

main()