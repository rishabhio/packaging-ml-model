


# app/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load
import numpy as np
from fastapi.responses import HTMLResponse


# Define FastAPI app
app = FastAPI()

# Load the trained model
model = load("model.joblib")

# Define request body schema using Pydantic BaseModel
class Item(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Define endpoint to make predictions
@app.post("/predict")
async def predict(item: Item):
    # Convert input to array
    input_data = [item.sepal_length, item.sepal_width, item.petal_length, item.petal_width]
    input_array = np.array([input_data])

    # Make prediction
    prediction = model.predict(input_array)[0]

    # Map prediction to class label
    class_label = {0: "setosa", 1: "versicolor", 2: "virginica"}
    predicted_class = class_label[prediction]

    # Return prediction
    return {"predicted_class": predicted_class}


@app.get('/app', response_class=HTMLResponse)
async def html():
    return """
    <!DOCTYPE html>
    <html>
    <head>
    <title>HTML Response</title>
    </head>
    <body>
    <h1>This is HTML response</h1>
    <img src="https://placehold.co/600x400" /> 
    <h1> Version 10 </h1> 
    </body>
    </html>
    """
