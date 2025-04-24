import os
import pandas as pd
import joblib
from sqlalchemy import create_engine

def load_features(db_path='data/oulad.db', query_path='src/features_student.sql'):
    
    
    with open(query_path, 'r') as f:
        query = f.read()

    engine = create_engine(f'sqlite:///{db_path}')
    with engine.connect() as conn:
        df = pd.read_sql_query(query, conn)

    return df

def load_model(model_path='model/model.pkl'):
   
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Modelo não encontrado em {model_path}")
    
    return joblib.load(model_path)

def load_preprocessor(preprocessor_path='model/preprocessor.pkl'):
    
    
    if not os.path.exists(preprocessor_path):
        raise FileNotFoundError(f"Preprocessador não encontrado em {preprocessor_path}")
    
    return joblib.load(preprocessor_path) 