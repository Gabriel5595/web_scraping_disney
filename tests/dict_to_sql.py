import sqlite3
import os

from components.create_table import create_table

def dict_to_sql(rides, park):
    # Conecta ao banco de dados (ou cria se não existir)
    path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..', 'resources', 'database', 'parques'))
    
    conn = sqlite3.connect(path)
    create_table(conn, park)
    
    # Prepara os dados para inserção
    data_to_insert = [(ride['data'], ride['hora'], ride['parque'], ride['area'], ride['nome'], ride['tempo_espera']) for ride in rides]
    
    # Inserir os dados na tabela
    insert_sql = f"""
    INSERT INTO {park} (data, hora, parque, area, nome, tempo_espera)
    VALUES (?, ?, ?, ?, ?, ?);
    """
    conn.executemany(insert_sql, data_to_insert)
    conn.commit()
    
    # Fecha a conexão
    conn.close()