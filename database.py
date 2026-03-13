import os
from pymongo import MongoClient
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# read MongoDB URI
MONGO_URI = os.getenv("MONGO_URI")

print("Mongo URI Loaded:", MONGO_URI)

# connect to MongoDB Atlas
client = MongoClient(MONGO_URI)

# create database
db = client["adaptive_ai_engine"]

# collections
questions_collection = db["questions"]
sessions_collection = db["user_sessions"]

print("MongoDB connected successfully")