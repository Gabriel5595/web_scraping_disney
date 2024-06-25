from bs4 import BeautifulSoup
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.get_page_content import get_page_content

def define_wait_time(ride_element):
    ride_wait_time_element = ride_element.find_next('div', class_='relative z-10 flex items-center')
        
    ride_ok = ride_wait_time_element.find('div', class_="inline-flex h-8 w-8 items-center justify-center rounded-full bg-teal-200 font-medium text-teal-800")
    ride_unavailable_now = ride_wait_time_element.find('div', class_="inline-flex h-8 w-8 items-center justify-center rounded-full bg-red-200 text-red-800")
    ride_unavailable_indefinitely = ride_wait_time_element.find('div', class_="inline-flex h-8 w-8 items-center justify-center rounded-full bg-gray-200 text-gray-600")
    
    if ride_ok is not None:
        wait_time = ride_ok.get_text(strip=True)
        return wait_time
    elif ride_unavailable_now is not None:
        wait_time = "Atração indisponível agora"
        return wait_time
    elif ride_unavailable_indefinitely is not None:
        wait_time = "Atração indiponível indefinidamente"
        return wait_time
    else:
        wait_time = "Desconhecido"
        return wait_time

def main():
    url = "https://wdwpassport.com/wait-times/magic-kingdom"
    page_content = get_page_content(url)
    soup = BeautifulSoup(page_content, 'html.parser')
    
    ride_elements = soup.find_all('h3', class_='relative z-10 mr-4 text-sm font-medium leading-tight')
    
    for ride_element in ride_elements:
        print(define_wait_time(ride_element))

main()