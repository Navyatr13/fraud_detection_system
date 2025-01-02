import sys
import os

# Add the project root to the module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import logging
from fastapi import FastAPI
from src.api.model import predict_fraud

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.post("/predict")
def predict(data: dict):
    logger.info(f"Received data: {data}")
    result = predict_fraud(list(data.values()))
    logger.info(f"Prediction result: {result}")
    return {"fraud": result}
