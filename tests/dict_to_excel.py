import pandas as pd
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.generate_file_name import generate_file_name
from components.check_file_exists import check_file_exists
from components.should_check import should_check
from components.get_page_content import get_page_content
from components.extract_data import extract_data

def dict_to_excel(dict_list):
    file_name = generate_file_name(dict_list, "xlsx")
    
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..', 'resources', 'excel'))
    
    # Verificar se o arquivo já existe
    if check_file_exists(file_name, "excel"):
        # Arquivo existe, então ler o arquivo existente e concatenar os novos dados
        existing_df = pd.read_excel(file_name)
        new_df = pd.DataFrame(dict_list)
        combined_df = pd.concat([existing_df, new_df], ignore_index=True)
        full_path = os.path.join(base_path, file_name)
        combined_df.to_excel(full_path, index=False)
    else:
        # Arquivo não existe, então criar um novo arquivo
        new_df = pd.DataFrame(dict_list)
        full_path = os.path.join(base_path, file_name)
        new_df.to_excel(full_path, index=False)

def main():
    if should_check():

        parks = ["magic-kingdom", "epcot", "hollywood-studios", "animal-kingdom"]

        for park in parks:
            url = "https://wdwpassport.com/wait-times/" + park
            
            content = get_page_content(url)
            rides = extract_data(content)
            
            dict_to_excel(rides)

main()