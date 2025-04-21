from pathlib import Path
import nbformat as nbf

# Caminho para salvar o notebook
output_path = Path("analise_resultados_pipeline.ipynb")

# Criando um novo notebook
nb = nbf.v4.new_notebook()

# Células de código e markdown com melhorias
cells = [
    nbf.v4.new_markdown_cell("# Análise dos Resultados do Pipeline\n\nEste notebook mostra os resultados do pipeline de machine learning."),
    
    nbf.v4.new_code_cell("""# Importações básicas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração do estilo dos gráficos
plt.style.use('ggplot')
sns.set(style="whitegrid")"""),
    
    nbf.v4.new_code_cell("""# Carrega os dados processados
df = pd.read_csv('../data/student_data.csv')
print(f"Total de registros: {len(df)}")
df.head()"""),

    nbf.v4.new_code_cell("""# Validação de tipos e valores faltantes
df.info()
df.isnull().sum()"""),

    nbf.v4.new_code_cell("""# Verifica a proporção dos resultados finais
df['final_result'].value_counts(normalize=True).plot(kind='bar', title='Distribuição Proporcional dos Resultados')
plt.show()"""),
    
    nbf.v4.new_code_cell("""# Análise da distribuição do resultado final
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='final_result')
plt.title('Distribuição dos Resultados Finais')
plt.xticks(rotation=45)
plt.show()"""),

    nbf.v4.new_code_cell("""# Análise de correlação entre features numéricas
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
plt.figure(figsize=(12, 8))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm')
plt.title('Matriz de Correlação')
plt.show()"""),
    
    nbf.v4.new_code_cell("""# Análise de features categóricas
categorical_cols = ['gender', 'region', 'highest_education', 'imd_band', 'age_band']

for col in categorical_cols:
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x=col, hue='final_result')
    plt.title(f'Distribuição de {col} por Resultado Final')
    plt.xticks(rotation=45)
    plt.legend(title='Resultado Final')
    plt.show()"""),
    
    nbf.v4.new_code_cell("""# Análise de métricas de performance
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import pickle

# Carrega o modelo e preprocessor
with open('../model/random_forest_model.pkl', 'rb') as f:
    model = pickle.load(f)
    
with open('../model/preprocessor.pkl', 'rb') as f:
    preprocessor = pickle.load(f)

# Prepara os dados
X = df.drop(columns=['final_result'])
y = (df['final_result'] == 'Withdrawn').astype(int)

# Transforma os dados
X_transformed = preprocessor.transform(X)

# Faz predições
y_pred = model.predict(X_transformed)

# Mostra o relatório de classificação
print(classification_report(y, y_pred))

# Mostra a matriz de confusão (visual)
ConfusionMatrixDisplay.from_predictions(y, y_pred, display_labels=["Permanente", "Desistente"])
plt.title("Matriz de Confusão - Visual")
plt.show()"""),

    nbf.v4.new_code_cell("""# Análise de importância das features
feature_names = preprocessor.get_feature_names_out()
importances = model.feature_importances_

# Cria um DataFrame com as importâncias
feature_importance = pd.DataFrame({
    'feature': feature_names,
    'importance': importances
}).sort_values('importance', ascending=False)

# Plota as 20 features mais importantes
plt.figure(figsize=(12, 8))
sns.barplot(data=feature_importance.head(20), x='importance', y='feature')
plt.title('Top 20 Features Mais Importantes')
plt.show()"""),

    nbf.v4.new_code_cell("""# Análise dos erros de predição
df_errors = df.copy()
df_errors['y_pred'] = y_pred
df_errors['y_real'] = y.values
erros = df_errors[df_errors['y_pred'] != df_errors['y_real']]
erros.head()""")
]

nb['cells'] = cells

# Salvando o notebook
with open(output_path, "w", encoding="utf-8") as f:
    nbf.write(nb, f)

output_path.name