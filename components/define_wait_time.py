from bs4 import BeautifulSoup

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