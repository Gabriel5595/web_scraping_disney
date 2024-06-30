import time

from components.extract_data import extract_data
from components.get_page_content import get_page_content
from components.should_check import should_check
from components.dict_to_csv import dict_to_csv
from components.dict_to_excel import dict_to_excel
from components.dict_to_sql import dict_to_sql


def main():
    while True:
        
        if should_check():

            parks = ["magic-kingdom", "epcot", "hollywood-studios", "animal-kingdom"]

            for park in parks:
                url = "https://wdwpassport.com/wait-times/" + park
                
                content = get_page_content(url)
                rides = extract_data(content)
                
                dict_to_csv(rides)
                dict_to_excel(rides)
                dict_to_sql(rides, park)
                
        print("\nInformation updated successfully\n")
                        
        time.sleep(300)
    
    
    
main()