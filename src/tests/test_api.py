import sys
import os
# Ensure the module search path includes the project root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from fastapi.testclient import TestClient
from src.api.main import app


# Initialize TestClient
client = TestClient(app)


def test_predict():
    # Test data simulating input from index.html
    payload = {"feature1": 0.1, "feature2": 1.5, "feature3": 3.2, "feature4": 0.8, "feature5": 1.8}

    # Send POST request to the /predict endpoint
    response = client.post("/predict", json=payload)
    # Print the predicted result
    if response.status_code == 200:
        print(f"Prediction result: {response.json()}")
    else:
        print(f"Failed with status code: {response.status_code}, Error: {response.text}")

    # Assertions to validate the response
    assert response.status_code == 200
    assert "fraud" in response.json()

if __name__ == "__main__":
    test_predict()