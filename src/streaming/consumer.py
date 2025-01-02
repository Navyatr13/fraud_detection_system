from kafka import KafkaConsumer
import requests

consumer = KafkaConsumer(
    "fraud_transactions",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest"
)

for message in consumer:
    response = requests.post("http://localhost:8000/predict", json=message.value)
    print(f"Response: {response.json()}")
