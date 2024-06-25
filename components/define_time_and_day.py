from datetime import datetime

def define_time_and_day():
    date_time = datetime.now()
    sql_date = date_time.strftime('%Y-%m-%d')
    sql_time = date_time.strftime('%H:%M:%S')
    
    return sql_date, sql_time