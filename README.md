# Projeto de Análise de Evasão Estudantil

Este projeto implementa um pipeline completo de Machine Learning para analisar e prever a evasão estudantil, utilizando o dataset OULAD (Open University Learning Analytics Dataset).

## Estrutura do Projeto

```
.
├── data/             # Dados do projeto
├── model/            # Modelos treinados
├── notebooks/        # Notebooks de análise
│   ├── analise_dados.ipynb               # Análise exploratória dos dados
│   ├── analise_modelo.ipynb              # Análise do modelo treinado
│   ├── analise_resultados_pipeline.ipynb # Análise dos resultados do pipeline
│   └── students.ipynb                    # Análise detalhada dos estudantes
├── src/              # Código fonte
│   ├── utils.py              # Funções utilitárias
│   ├── load_features.py     # Carregamento de features
│   ├── preprocessing.py     # Pré-processamento dos dados
│   └── train_model.py       # Treinamento do modelo
├── logs/             # Logs do projeto
├── requirements.txt  # Dependências do projeto
└── setup.py          # Configuração do pacote
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

2. Instale o pacote em modo desenvolvimento:
   ```bash
   pip install -e .
   ```

3. Execute o treinamento:
   ```bash
   python src/train_model.py
   ```

4. Para explorar os dados e resultados, rode o Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

   Navegue até a pasta `notebooks/` e abra o notebook desejado.

---

> Projeto educacional com foco em ciência de dados aplicada à evasão estudantil.

