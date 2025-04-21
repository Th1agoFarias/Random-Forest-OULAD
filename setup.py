from setuptools import setup, find_packages

setup(
    name="aplicacao_ml",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas==2.1.4",
        "numpy==1.24.3",
        "scipy==1.11.4",
        "scikit-learn==1.3.2",
        "sqlalchemy==2.0.23"
    ],
) 