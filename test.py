from sqlalchemy import create_engine

engine = create_engine('sqlite:///data/oulad.db')
with engine.connect() as conn:
    result = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = result.fetchall()
    print("Tabelas no banco de dados:", tables)
