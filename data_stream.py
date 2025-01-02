import time
import random
import requests
import logging
import os
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# API endpoint
API_URL = os.getenv("API_URL", "http://127.0.0.1:5000/predict")

# Configure retry session
def configure_session():
    session = requests.Session()
    retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    session.mount("http://", HTTPAdapter(max_retries=retries))
    session.mount("https://", HTTPAdapter(max_retries=retries))
    return session

session = configure_session()

# Simulate streaming data
def generate_transaction():
    return {
        "feature1": round(random.uniform(0, 100), 2),
        "feature2": round(random.uniform(0, 5000), 2),
        "feature3": round(random.uniform(1, 10), 2),
        "feature4": round(random.uniform(-5, 5), 2),
        "feature5": round(random.uniform(0, 1), 2),
    }

def send_transaction(transaction):
    try:
        response = session.post(API_URL, json=transaction)
        response.raise_for_status()
        logger.info(f"Sent: {transaction} | Response: {response.json()}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {e}")
    except ValueError:
        logger.error("Invalid JSON response from server")

if __name__ == "__main__":
    logger.info("Starting real-time transaction simulation...")
    for _ in range(10):  # Send 100 transactions
        transaction = generate_transaction()
        send_transaction(transaction)
        time.sleep(1)  # Send data every second
    logger.info("Simulation complete.")
