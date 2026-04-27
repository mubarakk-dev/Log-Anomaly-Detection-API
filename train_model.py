import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

np.random.seed(42)

normal = np.random.normal(200, 30, 500)
anomalies = np.random.normal(600, 80, 30)

response_times = np.concatenate([normal, anomalies])

df = pd.DataFrame({
    "response_time": response_times
})

model = IsolationForest(contamination=0.06, random_state=42)

model.fit(df[["response_time"]])

joblib.dump(model, "anomaly_model.pkl")

print("Model trained and saved.")