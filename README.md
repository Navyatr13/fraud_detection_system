# Fraud Detection System

A production-grade system for real-time fraud detection with MLOps practices.

## Features
- **Real-Time Streaming**: Process transaction streams using Kafka.
- **Low-Latency API**: Serve fraud predictions via FastAPI.
- **Model Training and Retraining**: Pipelines for training and automated retraining.
- **Monitoring**: Metrics collection and drift detection with Prometheus and Evidently.

---

## Setup Instructions

### Prerequisites
- Python 3.9
- Docker (optional for deployment)
- Kafka (for streaming)

### Environment Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fraud-detection-system.git
   cd fraud-detection-system
2. Create a virtual environment and install dependencies:
   ```bash
   conda create --name fraud-detection python=3.9 -y
   conda activate fraud-detection
   pip install -r requirements.txt
3.  Running the Application 

   1. Start the API:
      ```bash
         uvicorn src.api.main:app --reload
   2. Start the Kafka producer:
      ```bash
         python src/streaming/producer.py
   3. Start the Kafka consumer:
      ```bash
         python src/streaming/consumer.py

## Run unit and integration tests:
``` bash
    pytest tests/
