from fastapi import FastAPI
from transformers import pipeline

app = FastAPI(title="ML Pipeline Demo")

classifier = pipeline("sentiment-analysis")

@app.get("/predict")
def predict(text: str):
    result = classifier(text)
    return {"input": text, "prediction": result}