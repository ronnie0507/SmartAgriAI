
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database.connection import (
    check_database_connection,
    close_database_connection,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    check_database_connection()
    print("AgriSmart AI: MongoDB connected successfully")

    yield

    close_database_connection()
    print("AgriSmart AI: MongoDB connection closed")
