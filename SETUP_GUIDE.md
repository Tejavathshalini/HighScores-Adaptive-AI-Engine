# How to Run the Project (Step-by-Step)

Follow these steps to run the project from scratch.

---

# 1. Install Python

Make sure Python is installed.

Check using:

```
python --version
```

If Python is not installed, download it from:

https://www.python.org/downloads/

---

# 2. Install MongoDB Atlas Database

1. Go to https://www.mongodb.com/cloud/atlas
2. Create a free account
3. Create a new cluster
4. Create a database named:

```
adaptive_ai_engine
```

5. Create a collection named:

```
questions
```

6. Copy the MongoDB connection string.

Example:

```
mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority
```

---

# 3. Clone the GitHub Repository

Open your terminal and run:

```
git clone https://github.com/YOUR_USERNAME/HighScores-Adaptive-AI-Engine.git
```

Move into the project folder:

```
cd HighScores-Adaptive-AI-Engine
```

---

# 4. Install Required Libraries

Install dependencies using:

```
pip install -r requirements.txt
```

Required packages include:

* fastapi
* uvicorn
* pymongo
* python-dotenv

---

# 5. Configure Environment Variables

Create a file named:

```
.env
```

Add the following:

```
MONGO_URI=your_mongodb_connection_string
```

Example:

```
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority
```

---

# 6. Load the Question Dataset

Insert GRE questions into MongoDB by running:

```
python -m data.seed_questions
```

You should see:

```
MongoDB connected successfully
20 questions inserted successfully
```

---

# 7. Start the FastAPI Server

Run the backend server:

```
uvicorn app.main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

# 8. Open API Documentation

Open your browser and go to:

```
http://127.0.0.1:8000/docs
```

This will open the **Swagger API documentation** where you can test all endpoints.

---

# 9. Test API Endpoints

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

# Expected Output

The system will return GRE questions and dynamically adjust difficulty based on user ability.

