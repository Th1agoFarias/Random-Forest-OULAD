<<<<<<< HEAD
# Projeto de Análise de Evasão Estudantil

Este projeto tem como objetivo analisar e prever a evasão estudantil usando técnicas de Machine Learning.
=======
# Pipeline de Machine Learning - Análise de Dados Educacionais

Este projeto implementa um pipeline completo de Machine Learning para análise de dados educacionais, utilizando o dataset OULAD (Open University Learning Analytics Dataset).
>>>>>>> 5724a20343220e4ddba27d8a49be7c54464420f0

## Estrutura do Projeto

```
<<<<<<< HEAD
.
├── data/                   # Dados do projeto
├── model/                  # Modelos treinados
├── notebooks/              # Notebooks de análise
│   ├── analise_dados.ipynb         # Análise exploratória dos dados
│   ├── analise_modelo.ipynb        # Análise do modelo treinado
│   ├── analise_resultados_pipeline.ipynb  # Análise dos resultados do pipeline
│   └── students.ipynb              # Análise detalhada dos estudantes
├── src/                    # Código fonte
│   ├── utils.py           # Funções utilitárias
│   ├── load_features.py   # Carregamento de features
│   ├── preprocessing.py   # Pré-processamento dos dados
│   └── train_model.py     # Treinamento do modelo
├── logs/                  # Logs do projeto
├── requirements.txt       # Dependências do projeto
└── setup.py              # Configuração do pacote
```

## Notebooks Disponíveis

1. **analise_dados.ipynb**
   - Análise exploratória básica dos dados
   - Estatísticas descritivas
   - Visualizações iniciais

2. **analise_modelo.ipynb**
   - Avaliação do modelo treinado
   - Métricas de performance
   - Matriz de confusão
   - Curva ROC

3. **analise_resultados_pipeline.ipynb**
   - Análise dos resultados do pipeline
   - Comparação entre evasão real e predita
   - Análise de erros
   - Visualizações por módulo e apresentação

4. **students.ipynb**
   - Análise detalhada dos estudantes
   - Análise demográfica
   - Análise de desempenho
   - Análise temporal

## Como Usar

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Instale o pacote em modo de desenvolvimento:
```bash
pip install -e .
```

3. Abra o Jupyter Notebook:
```bash
jupyter notebook
```

4. Navegue até a pasta `notebooks` e abra o notebook desejado.

## Dependências

- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- sqlalchemy
- joblib
=======
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
>>>>>>> 5724a20343220e4ddba27d8a49be7c54464420f0

