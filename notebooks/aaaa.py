# notebook_eda_model.ipynb (estrutura de células convertida em script para facilitar visualização)

# Cell 1: Imports
import pandas as pd
import pickle
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Cell 2: Carregar artefatos do projeto
path = "notebook_artifacts"

with open(f"{path}/model.pkl", "rb") as f:
    model = pickle.load(f)

with open(f"{path}/preprocessor.pkl", "rb") as f:
    preprocessor = pickle.load(f)

df = pd.read_parquet(f"{path}/features.parquet")

# Cell 3: Separar variáveis
X = df.drop(columns=["dropout", "final_result"])
y = df["dropout"]

# Cell 4: Análise Exploratória Simples
print("Visão Geral dos Dados:")
display(df.head())
display(df.describe())
display(df["dropout"].value_counts())

# Cell 5: Visualizações
sns.countplot(x="dropout", data=df)
plt.title("Distribuição da Variável Alvo (Dropout)")
plt.show()

sns.histplot(data=df, x="total_clicks", hue="dropout", kde=True)
plt.title("Total de Cliques no VLE vs Dropout")
plt.show()

# Cell 6: Previsão e Métricas
X_transformed = preprocessor.transform(X)
y_pred = model.predict(X_transformed)

print("\nClassification Report:")
print(classification_report(y, y_pred))

cm = confusion_matrix(y, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel("Predito")
plt.ylabel("Real")
plt.title("Matriz de Confusão")
plt.show()
