from bs4 import BeautifulSoup

def define_attraction(ride_element):
    attraction_name = ride_element.get_text(strip=True)
    return attraction_name