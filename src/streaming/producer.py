from kafka import KafkaProducer
import json
import time

def produce_data(file_path, topic):
    producer = KafkaProducer(
        bootstrap_servers="localhost:9092",
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
    for record in load_data(file_path).to_dict(orient="records"):
        producer.send(topic, record)
        time.sleep(0.1)
