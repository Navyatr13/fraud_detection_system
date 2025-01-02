from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import logging
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from src.database.db import save_transaction

# Add the project root to the module search path

# Configure logging
logging.basicConfig(
    filename="src/logs/app.log",  # Save logs to a file
    level=logging.INFO,           # Log level
    format="%(asctime)s - %(levelname)s - %(message)s"
)
app = Flask(__name__)

# Load the trained model
MODEL_PATH = "src/models/fraud_model.pkl"
model = joblib.load(MODEL_PATH)
transactions = []


@app.route("/")
def home():
    """
    Render the home page.
    """
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Handle JSON data
        if request.is_json:
            data = request.get_json()
            feature_names = ["V1", "V2", "V3", "V4", "V5"]
            features = [data[f"feature{i}"] for i in range(1, 6)]
        else:
            # Handle form data
            features = [float(request.form[f"feature{i}"]) for i in range(1, 6)]

        # Convert to DataFrame
        feature_names = ["V1", "V2", "V3", "V4", "V5"]
        input_data = pd.DataFrame([features], columns=feature_names)

        # Predict
        prediction = model.predict(input_data)[0]
        result = "Fraudulent" if prediction else "Not Fraudulent"
        save_transaction(features, result)

        # Store the transaction
        transaction = {f"feature{i}": features[i - 1] for i in range(1, 6)}
        transaction["result"] = result
        transactions.append(transaction)
        logging.info(f"Transaction: {transaction} | Prediction: {result}")

        # Return JSON response for real-time and render for manual form submission
        if request.is_json:
            return jsonify({"fraud": result})
        else:
            return render_template("index.html", prediction_text=f"Transaction is {result}")

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/transactions")
def get_transactions():
    """
    Get the list of all transactions.
    """
    return jsonify(transactions)


@app.route("/metrics")
def metrics():
    """
    Calculate and return metrics for visualizations.
    """
    total_transactions = len(transactions)
    fraudulent = sum(1 for tx in transactions if tx["result"] == "Fraudulent")
    not_fraudulent = total_transactions - fraudulent
    return jsonify({
        "total": total_transactions,
        "fraudulent": fraudulent,
        "not_fraudulent": not_fraudulent
    })


if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1", port=5000)
