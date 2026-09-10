import os
import pickle

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from load_features import run_features
from preprocessing import build_preprocessing_pipeline
from utils import get_logger

logger = get_logger(__name__)


def train_model():
    df = run_features()
    df["dropout"] = df["final_result"].apply(lambda x: 1 if x == "Withdrawn" else 0)

    X = df.drop(columns=["final_result", "dropout"])
    y = df["dropout"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    preprocessor = build_preprocessing_pipeline(X_train)

    full_pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", RandomForestClassifier(n_estimators=100, random_state=42)),
        ]
    )

    full_pipeline.fit(X_train, y_train)

    y_pred = full_pipeline.predict(X_test)
    logger.info("Modelo treinado. Resultados de avaliação:")
    logger.info("\n" + classification_report(y_test, y_pred))

    os.makedirs("model", exist_ok=True)

    with open("model/full_pipeline.pkl", "wb") as f:
        pickle.dump(full_pipeline, f)

    df.to_parquet("model/features_df.parquet")

    test_df = X_test.copy()
    test_df["dropout"] = y_test.values
    test_df.to_parquet("model/test_data.parquet")

    logger.info("Pipeline e datasets salvos com sucesso.")
