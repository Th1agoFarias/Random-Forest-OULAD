import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

def build_preprocessing_pipeline(data_path="data/student_data.csv", output_path="models/preprocessing_pipeline.pkl"):
    df = pd.read_csv(data_path)

    X = df.drop(columns=["final_result"])
    cat = X.select_dtypes(include="object").columns.tolist()
    num = X.select_dtypes(include="number").columns.tolist()

    pipeline = ColumnTransformer([
        ("num", Pipeline([
            ("imputer", SimpleImputer(strategy="mean")),
            ("scaler", StandardScaler())
        ]), num),
        ("cat", Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore"))
        ]), cat),
    ])

    pipeline.fit(X)
    joblib.dump(pipeline, output_path)
    print("✅ Pipeline de pré-processamento salva.")
