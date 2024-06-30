from datetime import datetime

def generate_file_name(dict_list, extension):
    formatted_date = datetime.now().strftime("%d%m%Y")
    
    park_name = dict_list[0]['parque'].replace(' ', '_')
    
    file_name = f"{formatted_date}-{park_name}.{extension}"
    
    return file_name