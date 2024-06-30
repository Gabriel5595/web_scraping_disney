def create_table(conn, park):
    
    create_table_sql = f"""
    CREATE TABLE IF NOT EXISTS {park} (
        info_id INTEGER PRIMARY KEY AUTOINCREMENT,
        data DATE NOT NULL,
        hora TIME NOT NULL,
        parque TEXT NOT NULL,
        area TEXT NOT NULL,
        nome TEXT NOT NULL,
        tempo_espera INTEGER NOT NULL
    );
    """
    conn.execute(create_table_sql)
    conn.commit()