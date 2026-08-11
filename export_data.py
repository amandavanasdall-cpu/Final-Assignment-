from pymongo import MongoClient
from dotenv import load_dotenv
import pandas as pd
import os

# Load environment variables
load_dotenv()

# Connect to MongoDB
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)

# Select database and collection
db = client["healthcare_spending"]
collection = db["users"]

# Get all users from MongoDB
users = collection.find()

# Create a list to store the data
user_data = []

# Loop through the MongoDB records
for user in users:
    user_data.append({
        "age": user.get("age"),
        "gender": user.get("gender"),
        "income": user.get("income"),
        "utilities": user.get("utilities"),
        "entertainment": user.get("entertainment"),
        "school_fees": user.get("school_fees"),
        "shopping": user.get("shopping"),
        "healthcare": user.get("healthcare")
    })

# Create a DataFrame
df = pd.DataFrame(user_data)

# Save the data to a CSV file
df.to_csv("data/healthcare_spending.csv", index=False)

print("Data successfully exported to data/healthcare_spending.csv")
print("\nNumber of users exported:", len(df))