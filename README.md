# Twitter Sentiment Analysis

## Overview
This project is a full-stack Twitter Sentiment Analysis application. It allows users to input tweet text and get the predicted sentiment (positive, neutral, or negative). The backend is built with **FastAPI**, and the frontend uses **React**.

The backend uses a pre-trained machine learning model (TF-IDF + classifier) to predict sentiment. The frontend interacts with the backend API to display results in real-time.

## Project Structure
Twitter_analysis/
├── frontend/ # React frontend
├── models/ # Pre-trained ML models
├── src/
│ ├── app/ # FastAPI application
│ ├── train/ # Training scripts (if any)
│ └── utils/ # Helper scripts
├── data/ # Sample data
├── notebooks/ # Jupyter notebooks
├── requirements.txt # Backend Python dependencies
├── .gitignore
└── README.md

markdown
Copy code

## Backend
- **Framework:** FastAPI  
- **Endpoints:**
  - `POST /predict` → Predict sentiment for a given text  
  - `GET /` → Root endpoint to check API status
- **Files:**
  - `src/app/main.py` → FastAPI main file
  - `src/utils/text_preprocessing.py` → Preprocessing helper

### Running Backend
1. Activate your Python virtual environment:
```bash
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Start the backend server:

bash
Copy code
uvicorn src.app.main:app --reload --port 8000
Access Swagger UI to test endpoints: http://127.0.0.1:8000/docs

Frontend
Framework: React (Vite)

File to Edit: frontend/src/App.jsx

Connects to the FastAPI backend for predictions.

Displays sentiment result on button click.

Running Frontend
Navigate to the frontend folder:

bash
Copy code
cd frontend
Install Node dependencies:

bash
Copy code
npm install
Start the frontend server:

bash
Copy code
npm run dev
Open the displayed URL (usually http://localhost:5173/) in your browser.

Optional Enhancements
Add CSS styling for better UI

Improve ML model for higher accuracy

Add additional API endpoints

Deployment to cloud platforms (Heroku, Vercel, etc.)

GitHub
The project is version-controlled using git

Push your changes using:

bash
Copy code
git add .
git commit -m "Your message"
git push origin main
