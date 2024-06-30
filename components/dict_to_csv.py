import pandas as pd
import os

from components.generate_file_name import generate_file_name
from components.check_file_exists import check_file_exists

def dict_to_csv(dict_list):
    # Gerar o nome do arquivo
    file_name = generate_file_name(dict_list, "csv")
    
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..', 'resources'))
    
    # Verificar se o arquivo já existe
    if check_file_exists(file_name):
        # Arquivo existe, então ler o arquivo existente e concatenar os novos dados
        existing_df = pd.read_csv(file_name)
        new_df = pd.DataFrame(dict_list)
        combined_df = pd.concat([existing_df, new_df], ignore_index=True)
        full_path = os.path.join(base_path, file_name)
        combined_df.to_csv(full_path, index=False)
    else:
        # Arquivo não existe, então criar um novo arquivo
        new_df = pd.DataFrame(dict_list)
        full_path = os.path.join(base_path, file_name)
        new_df.to_csv(full_path, index=False)