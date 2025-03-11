from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load the saved StandardScaler and RandomForest model
scaler = joblib.load("scaler.joblib")
rf_model = joblib.load("random_forest_model.joblib")

# Define the input data model based on your dataset
class InputFeatures(BaseModel):
    appearance: float
    minutes_played: float
    award: float
    highest_value: float
    team_Manchester_City: float

@app.get("/")
def read_root():
    return {"message": "Welcome to Tuwaiq Academy"}

@app.post("/predict")
def predict(input_features: InputFeatures):
    try:
        # Convert input data to a NumPy array
        test_data = np.array([[input_features.appearance, input_features.minutes_played,
                               input_features.award, input_features.highest_value,
                               input_features.team_Manchester_City]])

        # Apply StandardScaler to the new data
        scaled_test_data = scaler.transform(test_data)
        
        # Make a prediction using the model
        prediction = rf_model.predict(scaled_test_data)[0]
        
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction failed: {str(e)}")

import os
import uvicorn

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Set the appropriate port
    uvicorn.run(app, host="0.0.0.0", port=port)
