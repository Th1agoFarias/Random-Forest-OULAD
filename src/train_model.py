import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def train_model(data_path="data/student_data.csv"):
    df = pd.read_csv(data_path)

    X = df.drop(columns=["final_result"])
    y = df["final_result"]

    pipeline = joblib.load("models/preprocessing_pipeline.pkl")
    X_transformed = pipeline.transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    joblib.dump(model, "models/random_forest_model.pkl")
    print("✅ Modelo treinado e salvo!")

    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
