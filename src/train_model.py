import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from  sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pickle
from preprocessing import build_preprocessing_pipeline
from laod_features import run_features

def train_model():
    df = run_features()
    df['dropout'] = df['final_result'].apply(lambda x: 1 if x == "Withdrawn" else 0)
    
    X = df.drop(columns=['final_result', 'dropout'])
    y = df['dropout']

    preprocessor = build_preprocessing_pipeline(X)
    X_transformed = preprocessor.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("\n Avaliação do Modelo (Desistência):")
    print(classification_report(y_test, y_pred))

    with open("model/random_forest_model.pkl", "wb") as f:
        pickle.dump(model, f)
    with open("model/preprocessor.pkl", "wb") as f:
        pickle.dump(preprocessor, f)

    print(" Modelo e pipeline salvos em 'model/'")

if __name__ == "__main__":
    print("\n Iniciando pipeline completa...")
    train_model()