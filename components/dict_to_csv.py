import pandas as pd
import os

from components.generate_file_name import generate_file_name
from components.check_file_exists import check_file_exists

def dict_to_csv(dict_list):
    file_name = generate_file_name(dict_list, "csv")
    
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..', 'resources', 'csv'))
    
    if check_file_exists(file_name, "csv"):
        full_path = os.path.join(base_path, file_name)
        existing_df = pd.read_csv(full_path)
        new_df = pd.DataFrame(dict_list)
        combined_df = pd.concat([existing_df, new_df], ignore_index=True)
        combined_df.to_csv(full_path, index=False)
    else:
        # Arquivo não existe, então criar um novo arquivo
        new_df = pd.DataFrame(dict_list)
        full_path = os.path.join(base_path, file_name)
        new_df.to_csv(full_path, index=False)