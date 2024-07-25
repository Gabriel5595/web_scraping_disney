import time
from datetime import datetime, time as dt_time

from components.extract_data import extract_data
from components.get_page_content import get_page_content
from components.should_check import should_check
from components.dict_to_csv import dict_to_csv
from components.dict_to_excel import dict_to_excel
from components.dict_to_sql import dict_to_sql
from components.send_email_backup import send_email_backup


def main():
    while True:
        
        if should_check():

            parks = ["magic-kingdom", "epcot", "hollywood-studios", "animal-kingdom"]

            for park in parks:
                url = "https://wdwpassport.com/wait-times/" + park
                
                content = get_page_content(url)
                rides = extract_data(content)

                if rides:
                    dict_to_csv(rides)
                    dict_to_excel(rides)
                    dict_to_sql(rides, park)
                
        print("\nInformation updated successfully\n")
        
        current_time = datetime.now().time()
        if current_time > dt_time(23, 30) and current_time < dt_time(23, 34):
            send_email_backup()
             
        time.sleep(300)

main()