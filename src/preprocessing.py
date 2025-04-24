from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer

def build_preprocessing_pipeline(df):
    ignore_cols = ['student_id', 'date_registration', 'date_unregistration', 'withdrew']

    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    numeric_features = []
    for col in numeric_cols:
        if col not in ignore_cols:
            numeric_features.append(col)
    
    cat_cols = df.select_dtypes(include=['object', 'bool']).columns
    categorical_features = []
    for col in cat_cols:
        categorical_features.append(col)

    numeric_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="mean")),
        ("scaler", StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer(transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ])

    return preprocessor
