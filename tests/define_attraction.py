from bs4 import BeautifulSoup
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.get_page_content import get_page_content

def define_attraction(ride_element):
    attraction_name = ride_element.get_text(strip=True)
    return attraction_name

def main():
    url = "https://wdwpassport.com/wait-times/magic-kingdom"
    page_content = get_page_content(url)
    soup = BeautifulSoup(page_content, 'html.parser')
    
    ride_elements = soup.find_all('h3', class_='relative z-10 mr-4 text-sm font-medium leading-tight')
    
    for ride_element in ride_elements:
        print(define_attraction(ride_element))

main()