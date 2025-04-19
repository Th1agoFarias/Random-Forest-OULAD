import pandas  as pd
from sqlalchemy import  create_engine

def run_etl(db_path='data/oulad.db'):
    engine = create_engine(f"sqlite:///{db_path}")

    query = ""

    with engine.begin() as conn:
        conn.execute(query)