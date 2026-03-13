from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="HighScores Adaptive AI Engine")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "AI Adaptive Learning Engine Running"}