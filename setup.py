from setuptools import setup, find_packages

setup(
    name="fraud_detection_system",
    version="1.0.0",
    author="Your Name",
    description="A real-time fraud detection system with MLOps practices",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "fastapi",
        "uvicorn",
        "pandas",
        "scikit-learn",
        "joblib",
        "xgboost",
        "kafka-python",
        "evidently",
        "prometheus-client",
        "matplotlib"
    ],
    entry_points={
        "console_scripts": [
            "run-api=api.main:app",
        ],
    },
)
