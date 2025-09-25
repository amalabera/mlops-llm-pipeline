from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Load Hugging Face sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

app = FastAPI(title="MLOps LLM Pipeline 🤖")

class TextInput(BaseModel):
    text: str

@app.post("/predict")
def predict(input: TextInput):
    result = classifier(input.text)[0]
    return {"label": result["label"], "score": result["score"]}
