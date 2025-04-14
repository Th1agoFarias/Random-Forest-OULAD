import pandas as pd
from sqlalchemy import create_engine

def run_etl(db_path='data/oulad.db', sql_path='etl.sql', output_path='data/student_data.csv'):
    engine = create_engine(f"sqlite:///{db_path}")
    with open(sql_path, "r") as f:
        query = f.read()
    df = pd.read_sql_query(query, engine)
    df.to_csv(output_path, index=False)
    print("✅ Dataset salvo em:", output_path)

