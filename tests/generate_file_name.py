from datetime import datetime
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.get_page_content import get_page_content
from components.extract_data import extract_data

def generate_file_name(dict_list, extension):
    """
    Gera o nome do arquivo baseado na data, prefixo e nome do parque.
    """
    # Formatar a data
    formatted_date = datetime.now().strftime("%d%m%Y")
    
    # Pegar o valor da chave 'park' do primeiro dicionário e substituir espaços por underscores
    park_name = dict_list[0]['parque'].replace(' ', '_')
    
    # Nome do arquivo
    file_name = f"{formatted_date}-{park_name}.{extension}"
    
    return file_name

def main():
    url = "https://wdwpassport.com/wait-times/magic-kingdom"
    page_content = get_page_content(url)
    rides = extract_data(page_content)

    print(generate_file_name(rides, "csv"))

main()