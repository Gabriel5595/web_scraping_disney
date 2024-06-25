from bs4 import BeautifulSoup
from tabulate import tabulate
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.define_land import define_land
from components.define_time_and_day import define_time_and_day
from components.define_park import define_park
from components.define_attraction import define_attraction
from components.define_wait_time import define_wait_time
from components.get_page_content import get_page_content

def extract_data(content):
    soup = BeautifulSoup(content, 'html.parser')
    
    #DIA E HORA
    sql_date, sql_time = define_time_and_day()
    
    # PARQUE
    park = define_park(soup)
    
    # ATRAÇÕES E TEMPO DE ESPERA
    rides = []

    ride_elements = soup.find_all('h3', class_='relative z-10 mr-4 text-sm font-medium leading-tight')
    
    for ride_element in ride_elements:
        attraction_name = define_attraction(ride_element)
        
        wait_time = define_wait_time(ride_element)

        land = define_land(park, attraction_name)
        
        rides.append({
            'data': sql_date,
            'hora': sql_time,
            'parque': park,
            'area': land,
            'nome': attraction_name,
            'tempo_espera': wait_time
        })

    return rides

def main():
    url = "https://wdwpassport.com/wait-times/magic-kingdom"
    page_content = get_page_content(url)
    rides = extract_data(page_content)

    headers = rides[0].keys()
    rows = [ride.values() for ride in rides]
    print(tabulate(rows, headers=headers, tablefmt='grid'))

main()
