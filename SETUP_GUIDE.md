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

## Adaptive Algorithm Logic

The system implements a simple adaptive testing mechanism that selects questions based on the user's estimated ability level.

Each question in the database contains a **difficulty score** between **0 and 1**. The user also has an **ability score**, which represents their current performance level.

### Algorithm Steps

1. **Initial Ability**

   * Every user starts with a default ability score of **0.5**.

2. **Question Selection**

   * The system retrieves a question whose difficulty is closest to the user's current ability score.

3. **Answer Evaluation**

   * When the user submits an answer, the system checks whether it is correct.

4. **Ability Update**

   * If the answer is **correct**, the ability score increases slightly.
   * If the answer is **incorrect**, the ability score decreases slightly.

5. **Next Question Adaptation**

   * The updated ability score is used to select the next question.
   * Easier questions are shown when ability is low.
   * Harder questions are shown when ability is high.

### Difficulty Mapping Example

| Ability Range | Question Difficulty |
| ------------- | ------------------- |
| 0.0 – 0.3     | Easy                |
| 0.3 – 0.6     | Medium              |
| 0.6 – 1.0     | Hard                |

This adaptive approach helps simulate modern standardized testing systems where the difficulty of questions adjusts dynamically according to the user's performance.

## AI Usage Log

AI tools such as **ChatGPT** were used during the development of this project to accelerate the implementation process and assist with debugging.

### How AI Was Used

The following tasks were supported using AI tools:

* Generating the initial **FastAPI project structure**
* Creating **API route templates**
* Designing the **MongoDB schema for questions and user sessions**
* Implementing the **adaptive question selection logic**
* Debugging issues related to **FastAPI routing and server configuration**
* Assisting in writing **documentation and project explanations**

AI significantly helped speed up development by suggesting code patterns and identifying common errors.

### Challenges AI Could Not Solve

While AI tools provided useful guidance, some issues required manual debugging and testing, including:

* Fixing **MongoDB connection authentication errors**
* Resolving **environment variable configuration problems**
* Correcting **FastAPI import and routing errors**
* Ensuring proper **API testing through Swagger documentation**

These issues required manual investigation, testing, and validation to ensure the system worked correctly.

Overall, AI tools were used as a **development assistant**, while final implementation decisions and debugging were handled manually.


