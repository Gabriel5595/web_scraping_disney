from bs4 import BeautifulSoup
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.get_page_content import get_page_content

def define_park(soup):
    page_title_element = soup.find('h1', class_="w-full text-center text-lg font-medium leading-tight tracking-tight text-teal-700 md:text-left md:text-2xl")
    page_title = page_title_element.get_text(strip=True)
    
    if "Magic Kingdom" in page_title:
        return "Magic Kingdom"
    elif "Disney's Hollywood Studios" in page_title:
        return "Disney's Hollywood Studios"
    elif "Epcot" in page_title:
        return "Epcot"
    elif "Disney's Animal Kingdom" in page_title:
        return "Disney's Animal Kingdom"
    else:
        return "Could not be defined"

def main():
    url = "https://wdwpassport.com/wait-times/magic-kingdom"
    page_content = get_page_content(url)
    soup = BeautifulSoup(page_content, 'html.parser')
    
    print(define_park(soup))

main()