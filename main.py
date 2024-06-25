from tabulate import tabulate

from components.extract_data import extract_data
from components.get_page_content import get_page_content


def main():
    parks = ["magic-kingdom", "epcot", "hollywood-studios", "animal-kingdom"]
    
    for park in parks:
        url = "https://wdwpassport.com/wait-times/" + park
        
        content = get_page_content(url)
        rides = extract_data(content)
        
        headers = rides[0].keys()
        rows = [ride.values() for ride in rides]
        print(tabulate(rows, headers=headers, tablefmt='grid'))
    
    
main()