import pandas as pd 
import json 
from sqlalchemy import create_engine
from utils import get_logger

logger = get_logger(__name__)

def run_igestion(json_path="ingestion.json", db_path="data/oulad.db"):
    engine = create_engine(f"sqlite:///{db_path}")
    with open(json_path, "r") as f:
        tables = json.load(f)
        for table in tables:
            df = pd.read_csv(table["path"])
            df.to_sql(table['path'], con=engine, if_exists="replace", index=False)
            df.to_sql(table['table'], engine, if_exists="replace", index=False)
            logger.info(f"Table {table['table']} ingestão completa.")

