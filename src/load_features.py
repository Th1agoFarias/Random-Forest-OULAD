import pandas as pd
from sqlalchemy import create_engine

def run_features(db_path='data/oulad.db', query_path='src/features_student.sql'):
    with open(query_path, 'r') as f:
        query = f.read()

    engine = create_engine(f'sqlite:///{db_path}')
    with engine.connect() as conn:
        df = pd.read_sql_query(query, conn)

    return df

