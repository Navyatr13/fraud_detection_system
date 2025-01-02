from prometheus_client import Counter

fraud_counter = Counter("fraud_predictions", "Number of fraud predictions")

def increment_fraud_counter():
    fraud_counter.inc()
