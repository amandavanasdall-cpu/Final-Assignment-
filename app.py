from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv
from User import User
import os

# Load environment variables
load_dotenv()

# Create Flask application
app = Flask(__name__)

# Connect to MongoDB
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)

# Select database and collection
db = client["healthcare_spending"]
collection = db["users"]


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        # Get information from the form
        age = int(request.form.get("age"))
        gender = request.form.get("gender")
        income = float(request.form.get("income"))

        utilities = float(request.form.get("utilities") or 0)
        entertainment = float(request.form.get("entertainment") or 0)
        school_fees = float(request.form.get("school_fees") or 0)
        shopping = float(request.form.get("shopping") or 0)
        healthcare = float(request.form.get("healthcare") or 0)

        # Create a dictionary containing the participant's information
        user = User(
            age,
            gender,
            income,
            utilities,
            entertainment,
            school_fees,
            shopping,
            healthcare
        )

        user_data = user.to_dict()

        # Save the information to MongoDB
        collection.insert_one(user_data)
        return "Survey submitted successfully!"

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)