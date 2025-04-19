# Pipeline de Machine Learning - Análise de Dados Educacionais

Este projeto implementa um pipeline completo de Machine Learning para análise de dados educacionais, utilizando o dataset OULAD (Open University Learning Analytics Dataset).

## Estrutura do Projeto

```
aplicacaoMachineLearning/
├── data/           # Arquivos de dados CSV
├── src/            # Código fonte
│   ├── main.py              # Ponto de entrada do pipeline
│   ├── ingest_data.py       # Ingestão de dados
│   ├── etl.py              # Transformação de dados
│   ├── preprocessing.py    # Pré-processamento
│   └── train_model.py      # Treinamento do modelo
├── requirements.txt        # Dependências
└── ingestion.json         # Configuração de ingestão
```

## Pipeline

O pipeline é executado na seguinte ordem:

1. **Ingestão de Dados**: Carrega os arquivos CSV para o banco de dados SQLite
2. **ETL**: Transforma e limpa os dados
3. **Pré-processamento**: Prepara os dados para o modelo
4. **Treinamento**: Treina o modelo de machine learning

## Requisitos

- Dependências listadas em `requirements.txt`

