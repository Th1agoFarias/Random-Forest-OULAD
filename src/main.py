from ingest_data import ingest_data
from etl import run_etl
from train_model import train_model
from preprossing import build_preprocessing_pipeline
from train_model import train_model

def main():
    print('Pipeline de Machine Learning')
    ingest_data()
    run_etl()
    build_preprocessing_pipeline()
    train_model()
    print('Pipeline concluída com sucesso!')

if __name__ == "__main__":
    main()