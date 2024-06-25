from datetime import datetime
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def define_time_and_day():
    date_time = datetime.now()
    sql_date = date_time.strftime('%Y-%m-%d')
    sql_time = date_time.strftime('%H:%M:%S')
    
    return sql_date, sql_time

def main():
    sql_date, sql_time = define_time_and_day()
    
    print(sql_date)
    print(sql_time)

main()