from src.data.ingestion import load_data
from src.pipelines.train_model import train_model

def retrain_pipeline(file_path):
    data = load_data(file_path)
    train_model(data.drop("label", axis=1), data["label"])
