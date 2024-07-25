import mysql.connector
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def create_table(conn, park):
    create_table_sql = f"""
    CREATE TABLE IF NOT EXISTS `{park}` (
        info_id INT AUTO_INCREMENT PRIMARY KEY,
        data DATE NOT NULL,
        hora TIME NOT NULL,
        parque VARCHAR(255) NOT NULL,
        area VARCHAR(255) NOT NULL,
        nome VARCHAR(255) NOT NULL,
        tempo_espera INT NOT NULL
    );
    """
    cursor = conn.cursor()
    try:
        cursor.execute(create_table_sql)
        conn.commit()
        print(f"Tabela '{park}' criada com sucesso.")
    except mysql.connector.Error as err:
        print(f"Erro ao criar tabela: {err}")
    finally:
        cursor.close()