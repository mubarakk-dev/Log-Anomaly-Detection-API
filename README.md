Log Anomaly Detection API

A simple Python-based API that detects anomalies in system metrics using machine learning.

This project simulates a cloud monitoring use case, where system logs or metrics are analysed to identify unusual behaviour in real time.

Overview:

In modern cloud environments, large volumes of logs are generated continuously. Detecting anomalies in these logs is important for identifying system failures, performance issues, or unusual activity.

This project demonstrates a basic approach to anomaly detection using machine learning, exposed through a lightweight API.


Features:

* Detect anomalies in numerical log data
* Simple REST API for real-time predictions
* Lightweight and easy to run locally
* Simulates a cloud observability / AIOps use case


Tech Stack:

* Python
* FastAPI
* scikit-learn
  

How it works:

1. Synthetic log data is generated (e.g. response times, request rates)
2. A machine learning model is trained to learn normal behaviour
3. New inputs are evaluated and classified as:

   * Normal
   * Anomaly


API Usage

### Endpoint

POST /predict

### Example Request

```json
{
  "response_time": 120
}
```

### Example Response

```json
{
  "anomaly": true
}
```


Installation & Running:

1. Clone the repository

```
git clone https://github.com/yourusername/log-anomaly-detection-api.git
cd log-anomaly-detection-api
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Run the API

```
uvicorn app:app --reload
```

4. Open in browser:

```
http://127.0.0.1:8000/docs
```


Future Improvements:

* Deploy on AWS
* Add real-time log streaming
* Integrate monitoring dashboards (Grafana)
* Improve model accuracy with real datasets


Learning Goals:

This project was built to explore how machine learning can be applied to system monitoring and cloud observability.

## 🚀 Live API

This project exposes a FastAPI endpoint for anomaly detection.

You can test it via the interactive docs (temporary):
https://improved-fiesta-779p4g5p55q6px4p-8000.app.github.dev/docs


Author:

Khaled Mubarak
