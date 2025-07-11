from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict
import random

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PredictionResponse(BaseModel):
    label: str
    confidence: float

@app.get("/")
def root():
    return {"message": "Welcome to the DeepFake Detection API! Use /predict to analyze images."}

@app.post("/predict", response_model=PredictionResponse)
async def predict(file: UploadFile = File(...)):
    # Placeholder logic: randomly choose real/fake
    label = random.choice(["real", "fake"])
    confidence = round(random.uniform(0.7, 0.99), 2)
    return {"label": label, "confidence": confidence} 