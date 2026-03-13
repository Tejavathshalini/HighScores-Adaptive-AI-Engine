# Setup Guide – HighScores Adaptive AI Engine

This guide explains how to clone, install, and run the project locally.

---

# 1. Clone the Repository

Open your terminal and run:

```
git clone https://github.com/YOUR_USERNAME/HighScores-Adaptive-AI-Engine.git
```

Move into the project directory:

```
cd HighScores-Adaptive-AI-Engine
```

---

# 2. Install Python Dependencies

Install all required libraries using:

```
pip install -r requirements.txt
```

Required packages include:

* FastAPI
* Uvicorn
* pymongo
* python-dotenv
* groq (optional for AI study plan)

---

# 3. Configure Environment Variables

Create a `.env` file in the project root directory.

Add the following:

```
MONGO_URI=your_mongodb_connection_string
GROQ_API_KEY=your_groq_api_key (optional)
```

Example:

```
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxx
```

---

# 4. Seed the Database

Load GRE questions into MongoDB:

```
python -m data.seed_questions
```

This command inserts the question dataset into the MongoDB collection.

---

# 5. Run the FastAPI Server

Start the backend server:

```
uvicorn app.main:app --reload
```

The server will run at:

```
http://127.0.0.1:8000
```

---

# 6. Open API Documentation

Visit the interactive Swagger documentation:

```
http://127.0.0.1:8000/docs
```

You can test all endpoints directly from this page.

---

# 7. Test API Endpoints

Example endpoints:

Get all questions

```
GET /questions
```

Get adaptive next question

```
GET /next-question?ability=0.5
```

Generate study plan

```
GET /study-plan?ability=0.4
```

Start user session

```
POST /start-session
```

Submit answer

```
POST /submit-answer
```

---

# 8. Project Structure

```
HighScores-Adaptive-AI-Engine
│
├── app
│   ├── main.py
│   ├── routes.py
│   ├── adaptive_engine.py
│   ├── ai_study_plan.py
│   ├── database.py
│   ├── models.py
│   └── session.py
│
├── data
│   └── seed_questions.py
│
├── README.md
├── SETUP_GUIDE.md
├── AI_USAGE_LOG.md
├── requirements.txt
└── .env
```

---

# 9. Notes

* MongoDB Atlas is used as the cloud database.
* The adaptive engine selects questions based on user ability level.
* Study plans are generated using AI or rule-based recommendations.

---

# Author

Tejavath Shalini
Artificial Intelligence & Machine Learning Student
