import mysql.connector

from components.create_table import create_table
from components.db_connection import db_connection

def dict_to_sql(rides, park):
    # Conecta ao banco de dados
    conn = db_connection()
    create_table(conn, park)
    
    # Prepara os dados para inserção
    data_to_insert = [(ride['data'], ride['hora'], ride['parque'], ride['area'], ride['nome'], ride['tempo_espera']) for ride in rides]
    
    # Inserir os dados na tabela
    insert_sql = f"""
    INSERT INTO `{park}` (data, hora, parque, area, nome, tempo_espera)
    VALUES (%s, %s, %s, %s, %s, %s);
    """
    cursor = conn.cursor()
    try:
        cursor.executemany(insert_sql, data_to_insert)
        conn.commit()
        print(f"Dados inseridos com sucesso na tabela '{park}'.")
    except mysql.connector.Error as err:
        print(f"Erro ao inserir dados: {err}")
    finally:
        cursor.close()
        conn.close()