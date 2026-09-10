# 🎓 Previsão de Evasão Estudantil com Random Forest — OULAD

Projeto de Machine Learning voltado à análise e previsão de evasão estudantil utilizando o **Open University Learning Analytics Dataset (OULAD)**.

O objetivo é transformar dados acadêmicos e comportamentais dos estudantes em features que possam ser usadas por um modelo de classificação para identificar alunos com maior risco de desistência.

---

## 🎯 Problema

A evasão estudantil é um problema relevante em ambientes de ensino online. Neste projeto, a classe positiva é definida como:

```text
final_result = "Withdrawn" → dropout = 1
outros resultados            → dropout = 0
```

A ideia é usar informações demográficas, acadêmicas e de interação com o ambiente virtual para apoiar a identificação de padrões associados à desistência.

---

## 🔄 Fluxo do projeto

```text
CSV do OULAD
    ↓
Ingestão em SQLite
    ↓
Feature Engineering com SQL
    ↓
Pré-processamento com Scikit-learn
    ↓
Train/Test Split
    ↓
Random Forest
    ↓
Avaliação
    ↓
Persistência do modelo e dos artefatos
```

---

## 🧱 Arquitetura

O projeto separa ingestão, geração de features, pré-processamento e treinamento em módulos diferentes.

```text
.
├── data/                     # Dados utilizados pelo projeto
├── model/                    # Artefatos gerados pelo pipeline
│   ├── random_forest_model.pkl
│   ├── preprocessor.pkl
│   ├── full_pipeline.pkl
│   ├── features_df.parquet
│   └── test_data.parquet
│
├── notebooks/
│   └── student.ipynb         # Exploração e análise dos estudantes
│
├── src/
│   ├── features_student.sql  # Feature engineering
│   ├── ingestion.py          # Ingestão dos CSVs em SQLite
│   ├── load_features.py      # Execução da query de features
│   ├── preprocessing.py      # Pipeline de pré-processamento
│   ├── train_model.py        # Treinamento e avaliação
│   └── main.py               # Orquestração das etapas
│
├── exploracao.sql            # Consultas de exploração dos dados
├── ingestion.json            # Configuração das tabelas de ingestão
├── requirements.txt
└── setup.py
```

---

## 🗄️ Ingestão de dados

O arquivo `ingestion.json` configura a ingestão das principais tabelas do OULAD, incluindo:

- `assessments`
- `courses`
- `student_assessment`
- `student_info`
- `student_registration`
- `student_vle`
- `vle`

Os arquivos CSV são carregados com **Pandas** e persistidos em um banco **SQLite** com **SQLAlchemy**.

---

## 🧠 Feature Engineering

A construção das features é feita em SQL no arquivo `src/features_student.sql`.

Entre as informações utilizadas estão:

- módulo e apresentação do curso;
- gênero e faixa etária;
- nível educacional;
- quantidade de tentativas anteriores;
- créditos estudados;
- tempo de permanência no curso;
- quantidade de avaliações;
- média das notas;
- avaliações realizadas nos primeiros 14 dias;
- interações no VLE;
- total de cliques;
- cliques realizados nos primeiros 14 dias.

Essa etapa combina múltiplas tabelas do OULAD para gerar uma visão consolidada por estudante.

---

## ⚙️ Pré-processamento

O pré-processamento é construído com `Pipeline` e `ColumnTransformer` do Scikit-learn.

### Variáveis numéricas

```text
valores ausentes → média
padronização      → StandardScaler
```

### Variáveis categóricas

```text
valores ausentes → categoria mais frequente
encoding         → OneHotEncoder
```

O uso de pipeline permite manter as etapas de transformação organizadas e reutilizáveis.

---

## 🌲 Modelo

O modelo utilizado é um `RandomForestClassifier` com:

```python
RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
```

Os dados são separados em treino e teste com:

```python
train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

---

## 📊 Avaliação

A implementação atual gera um `classification_report` no conjunto de teste, permitindo acompanhar métricas como:

- Precision
- Recall
- F1-score
- Accuracy

Não há, no README atual do projeto, um resultado numérico consolidado salvo como referência; por isso este documento não apresenta métricas que não estejam registradas no repositório.

---

## 💾 Artefatos gerados

Após o treinamento, o projeto persiste artefatos que podem ser reutilizados posteriormente:

- modelo Random Forest;
- pré-processador;
- pipeline completo;
- dataset de features em Parquet;
- conjunto de teste transformado em Parquet.

Isso separa a etapa de treinamento do uso posterior do modelo.

---

## 🔎 Análise exploratória

O arquivo `exploracao.sql` contém consultas para analisar aspectos como:

- quantidade de estudantes;
- distribuição dos resultados finais;
- evasão por gênero e faixa etária;
- tentativas anteriores;
- desempenho em avaliações;
- tempo de permanência;
- interações com o ambiente virtual;
- número de cliques por estudante.

O notebook `notebooks/student.ipynb` complementa a exploração dos dados.

---

## 🛠️ Tecnologias

- Python
- Pandas
- SQL
- SQLite
- SQLAlchemy
- Scikit-learn
- Jupyter Notebook
- Random Forest
- Pickle / Parquet

---

## ▶️ Instalação

Clone o projeto:

```bash
git clone https://github.com/Th1agoFarias/Random-Forest-OULAD.git
cd Random-Forest-OULAD
```

Crie e ative um ambiente virtual e instale as dependências:

```bash
pip install -r requirements.txt
```

Os arquivos CSV esperados pelo pipeline devem estar dentro de `data/`, conforme os caminhos definidos em `ingestion.json`.

---

## 🚀 Próximas evoluções

Como evolução do projeto, alguns pontos podem fortalecer ainda mais a validação do modelo:

- utilizar separação estratificada das classes;
- adicionar Cross Validation estratificado;
- comparar o Random Forest com um baseline, como Regressão Logística;
- adicionar ROC-AUC e PR-AUC;
- analisar threshold de classificação;
- registrar as métricas finais no próprio repositório;
- avaliar importância das features e interpretabilidade do modelo.

---

## 📌 O que este projeto demonstra

Este projeto foi desenvolvido com foco não apenas no treinamento de um algoritmo, mas na construção de um fluxo organizado de dados e Machine Learning:

**ingestão → SQL → feature engineering → preprocessing → modelagem → avaliação → persistência**.

Ele demonstra conhecimentos em manipulação de dados, SQL, arquitetura de projeto Python, pipelines do Scikit-learn e classificação com Random Forest.
