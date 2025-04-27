import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline

from preprocessing import build_preprocessing_pipeline
from load_features import run_features
from utils import get_logger
import os

logger = get_logger(__name__)


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
    logger.info("Modelo treinado. Resultados de avaliação:")
    logger.info("\n" + classification_report(y_test, y_pred))


    full_pipeline = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("classifier", model)
    ])

    with open("model/random_forest_model.pkl", "wb") as f:
        pickle.dump(model, f)
    with open("model/preprocessor.pkl", "wb") as f:
        pickle.dump(preprocessor, f)
    with open("model/full_pipeline.pkl", "wb") as f:
        pickle.dump(full_pipeline, f)

    df.to_parquet("model/features_df.parquet")

    test_df = pd.DataFrame(X_test.toarray() if hasattr(X_test, "toarray") else X_test)
    test_df["dropout"] = y_test.values
    test_df.columns = test_df.columns.map(str)
    test_df.to_parquet("model/test_data.parquet")


    logger.info("Modelos e datasets salvos com sucesso.")


