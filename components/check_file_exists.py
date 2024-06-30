import os

def check_file_exists(file_name):
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resources'))
    full_path = os.path.join(base_path, file_name)
    
    return os.path.isfile(full_path)