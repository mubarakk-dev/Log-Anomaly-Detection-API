from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(
    title="Log Anomaly Detection API",
    description="Detects anomalies in system response times.",
    version="1.0"
)

model = joblib.load("anomaly_model.pkl")


class LogMetric(BaseModel):
    response_time: float


@app.get("/")
def home():
    return {"message": "Log Anomaly Detection API is running"}


@app.post("/predict")
def predict(metric: LogMetric):
    data = pd.DataFrame([[metric.response_time]], columns=["response_time"])

    prediction = model.predict(data)[0]
    is_anomaly = prediction == -1

    return {
        "response_time": metric.response_time,
        "anomaly": bool(is_anomaly)
    }