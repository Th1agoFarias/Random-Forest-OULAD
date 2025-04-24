from setuptools import setup, find_packages

setup(
    name="evasao_estudantil",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
        "matplotlib",
        "seaborn",
        "shap",
        "sqlalchemy"
    ],
) 