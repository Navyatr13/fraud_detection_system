import joblib
import numpy as np

# Load the trained model
MODEL_PATH = "src/models/fraud_model.pkl"
try:
    model = joblib.load(MODEL_PATH)
    print(f"Model loaded successfully from {MODEL_PATH}")
except FileNotFoundError:
    print(f"Error: Model not found at {MODEL_PATH}. Please train the model first.")

def predict_fraud(data):
    """
    Predict if a transaction is fraudulent.
    Args:
        data (list): A list of feature values (single transaction).
    Returns:
        bool: True if fraudulent, False otherwise.
    """

    data_array = np.array([data])  # Convert input to a 2D array
    prediction = model.predict(data_array)
    return bool(prediction[0])

if __name__ == "__main__":
    data = [0.25, 3.2, 0.85, 1.2, 0.95]
    res = predict_fraud(data)
    print(res)