# main.py (inside src/app)

import os
import sys
import pickle
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# ----------------------------
# Add project root to sys.path to avoid ModuleNotFoundError
# ----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)

from src.utils.text_preprocessing import clean_tweet

# ----------------------------
# Load model and vectorizer
# ----------------------------
model_path = os.path.join(BASE_DIR, 'models', 'sentiment_model.pkl')
vectorizer_path = os.path.join(BASE_DIR, 'models', 'tfidf_vectorizer.pkl')

with open(model_path, 'rb') as f:
    loaded_model = pickle.load(f)

with open(vectorizer_path, 'rb') as f:
    loaded_vectorizer = pickle.load(f)

# ----------------------------
# Initialize FastAPI
# ----------------------------
app = FastAPI(title="Twitter Sentiment Analysis API")
# ----------------------------
# Add CORS middleware
# ----------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React dev server URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------
# Pydantic model for request
# ----------------------------
class TweetRequest(BaseModel):
    text: str

# ----------------------------
# Prediction function
# ----------------------------
def predict_sentiment(text: str):
    cleaned = clean_tweet(text)
    vector = loaded_vectorizer.transform([cleaned])
    prediction = loaded_model.predict(vector)
    # Convert numeric label back to string if needed
    label_map = {0: "negative", 1: "neutral", 2: "positive"}
    return label_map[prediction[0]]

# ----------------------------
# API endpoint
# ----------------------------
@app.post("/predict")
def predict(tweet: TweetRequest):
    result = predict_sentiment(tweet.text)
    return {"text": tweet.text, "sentiment": result}

# Optional root endpoint
@app.get("/")
def root():
    return {"message": "Twitter Sentiment Analysis API is running"}

