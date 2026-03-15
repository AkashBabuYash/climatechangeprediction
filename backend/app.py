import pandas as pd
import numpy as np
import gradio as gr

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# -----------------------------
# FASTAPI APP
# -----------------------------

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# LOAD DATA
# -----------------------------

df = pd.read_csv("train.csv")

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day

X = df.drop(columns=["meantemp", "date"])
y = df["meantemp"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# TRAIN MODEL
# -----------------------------

model = RandomForestRegressor(
    n_estimators=500,
    max_depth=7,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

# -----------------------------
# INPUT SCHEMA
# -----------------------------

class InputData(BaseModel):
    year: int
    month: int
    day: int
    humidity: float
    wind_speed: float
    meanpressure: float
    rainfall: float

# -----------------------------
# FASTAPI ROUTES
# -----------------------------

@app.get("/")
def home():
    return {
        "message": "Temperature Prediction API Running",
        "R2 Score": r2,
        "MAE": mae,
        "RMSE": rmse
    }

@app.post("/predict")
def predict(data: InputData):

    input_data = pd.DataFrame([data.model_dump()])
    input_data = input_data[X_train.columns]

    prediction = model.predict(input_data)

    return {"predicted_temperature": float(prediction[0])}

# -----------------------------
# GRADIO FUNCTION
# -----------------------------

def gradio_predict(year, month, day, humidity, wind_speed, meanpressure, rainfall):

    input_data = pd.DataFrame([{
        "year": year,
        "month": month,
        "day": day,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "meanpressure": meanpressure,
        "rainfall": rainfall
    }])

    input_data = input_data[X_train.columns]

    prediction = model.predict(input_data)

    return float(prediction[0])

# -----------------------------
# GRADIO UI
# -----------------------------

gradio_ui = gr.Interface(
    fn=gradio_predict,
    inputs=[
        gr.Number(label="Year"),
        gr.Number(label="Month"),
        gr.Number(label="Day"),
        gr.Number(label="Humidity"),
        gr.Number(label="Wind Speed"),
        gr.Number(label="Mean Pressure"),
        gr.Number(label="Rainfall")
    ],
    outputs=gr.Number(label="Predicted Temperature"),
    title="Temperature Prediction Model"
)

# -----------------------------
# MAIN RUN
# -----------------------------

if __name__ == "__main__":
    gradio_ui.launch(share=True)