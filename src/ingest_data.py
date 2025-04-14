import json
import pandas as pd
from sqlalchemy import create_engine

def ingest_data():
    # Configuração do banco de dados
    engine = create_engine('sqlite:///data/oulad.db')
    
    # Carrega configuração do arquivo JSON
    with open('ingestion.json', 'r') as f:
        arquivos = json.load(f)
    
    for config in arquivos:
        print(f"Carregando {config['table']}...")
        for i, chunk in enumerate(pd.read_csv(config['path'], chunksize=1000)):
            if i == 0:
                chunk.to_sql(config['table'].lower(), engine, if_exists='replace', index=False)
            else:
                chunk.to_sql(config['table'].lower(), engine, if_exists='append', index=False)
        print(f"✅ {config['table']} carregado")
