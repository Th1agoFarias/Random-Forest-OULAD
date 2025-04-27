from ingestion import run_ingestion
from load_features import run_features
from train_model import train_model

def main():
    print("Iniciando ingestão dos dados...")
    run_ingestion()

    print("Gerando features...")
    df = run_features()

    print("Treinando modelo...")
    train_model()

    print("Pipeline finalizado com sucesso.")

if __name__ == "__main__":
    main()
