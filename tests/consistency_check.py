import sqlite3
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def consistency_check():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..', 'resources', 'database', 'parques.db'))
    with sqlite3.connect(path) as connection:
        cursor = connection.cursor()
        
        print("*** TABLE CARGOS ***")
        cursor.execute("SELECT * FROM magic_kingdom")
        results = cursor.fetchall()
        for line in results:
            print(line)
            
        print("*** TABLE CARGOS ***")
        cursor.execute("SELECT * FROM epcot")
        results = cursor.fetchall()
        for line in results:
            print(line)
            
        print("*** TABLE CARGOS ***")
        cursor.execute("SELECT * FROM hollywood_studios")
        results = cursor.fetchall()
        for line in results:
            print(line)
            
        print("*** TABLE CARGOS ***")
        cursor.execute("SELECT * FROM animal_kingdom")
        results = cursor.fetchall()
        for line in results:
            print(line)

def main():
    consistency_check()

main()