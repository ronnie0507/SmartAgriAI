from pymongo import MongoClient

try:
    client = MongoClient(
        "mongodb://127.0.0.1:27017",
        serverSelectionTimeoutMS=5000
    )

    client.admin.command("ping")

    print("MongoDB connected successfully!")

    db = client["agrismart"]
    print("Database:", db.name)

    client.close()

except Exception as error:
    print("MongoDB connection failed:", error)