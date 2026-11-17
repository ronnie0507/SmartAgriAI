
import os

from pymongo import MongoClient
from pymongo.database import Database


MONGODB_URI = os.getenv(
    "MONGODB_URI",
    "mongodb://127.0.0.1:27017"
)

DATABASE_NAME = "agrismart"

client = MongoClient(
    MONGODB_URI,
    serverSelectionTimeoutMS=5000
)

db: Database = client[DATABASE_NAME]


def check_database_connection() -> bool:
    """Check whether MongoDB is reachable."""
    client.admin.command("ping")
    return True


def close_database_connection() -> None:
    """Close the MongoDB client."""
    client.close()
