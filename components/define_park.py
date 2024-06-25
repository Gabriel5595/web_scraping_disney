from bs4 import BeautifulSoup

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