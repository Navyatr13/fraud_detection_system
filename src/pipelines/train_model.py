import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

DATA_PATH = "src/data/creditcard.csv"

def train_and_save_model():
    # Load dataset
    N_ROWS = 10000
    data = pd.read_csv(DATA_PATH,  nrows=N_ROWS)
    # Feature selection and preprocessing
    selected_features = ["V1", "V2", "V3", "V4", "V5"]
    X = data[selected_features]
    y = data["Class"]

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a simple model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save the model
    joblib.dump(model, "src/models/fraud_model.pkl")
    print("Model saved to models/fraud_model.pkl")

if __name__ == "__main__":
    train_and_save_model()
