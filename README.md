# HighScores Adaptive AI Engine

## Project Overview

HighScores Adaptive AI Engine is an intelligent practice system designed for GRE preparation.
The platform dynamically adjusts question difficulty based on the user's ability level and provides personalized study recommendations.

The system uses **FastAPI**, **MongoDB Atlas**, and an adaptive algorithm to simulate a real adaptive testing engine similar to modern online learning platforms.

---

## Key Features

* Adaptive question difficulty algorithm
* Dynamic ability estimation
* MongoDB cloud database integration
* AI-powered study recommendations
* REST API built with FastAPI
* Interactive API documentation (Swagger UI)
* GRE-style question dataset
* User session tracking

---

## Tech Stack

| Technology           | Purpose               |
| -------------------- | --------------------- |
| Python               | Backend development   |
| FastAPI              | REST API framework    |
| MongoDB Atlas        | Cloud database        |
| Uvicorn              | ASGI server           |
| Groq / Rule-based AI | Study plan generation |

---

## System Architecture

User → FastAPI API → Adaptive Engine → MongoDB Database
↓
AI Study Plan Generator

---

## API Endpoints

### Get All Questions

```
GET /questions
```

Returns the list of GRE questions stored in MongoDB.

---

### Get Next Adaptive Question

```
GET /next-question?ability=0.5
```

Returns the next question based on the user's ability score.

---

### Generate Study Plan

```
GET /study-plan?ability=0.4
```

Generates a personalized study plan based on performance level.

Example Response

```
{
 "level": "Intermediate",
 "recommendations": [
   "Practice algebra problems",
   "Solve word problems",
   "Improve calculation speed"
 ]
}
```

---

### Start User Session

```
POST /start-session
```

Creates a new practice session.

---

### Submit Answer

```
POST /submit-answer
```

Evaluates the answer and updates the user's ability score.

---

## Installation

Clone repository

```
git clone https://github.com/YOUR_USERNAME/HighScores-Adaptive-AI-Engine.git
cd HighScores-Adaptive-AI-Engine
```

Install dependencies

```
pip install -r requirements.txt
```

Run server

```
uvicorn app.main:app --reload
```

---

## API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## Project Demo Links

Local API Server

```
http://127.0.0.1:8000
```

Swagger API Documentation

```
http://127.0.0.1:8000/docs
```

---

## Dataset

The project contains **25 GRE-style questions** with the following schema:

* Question
* Options
* Correct Answer
* Difficulty
* Topic
* Tags

---

## Author

Tejavath Shalini
Artificial Intelligence & Machine Learning Student
