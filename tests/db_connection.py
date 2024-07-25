import mysql.connector

import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def db_connection():
    config = {
        'user': 'wishproj_admin',
        'password': 'BelieveInAWish0@',
        'host': '31.22.4.94',
        'database': 'wishproj_parques'
    }
    
    try:
        conn = mysql.connector.connect(**config)
        print("Connection Successful!")
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def main():
    db_connection()

main()