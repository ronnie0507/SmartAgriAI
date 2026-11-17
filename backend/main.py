from fastapi import FastAPI

from app.core.lifespan import lifespan
from app.routes import health, database

app = FastAPI(
    title="AgriSmart AI",
    description="AI-Assisted Agricultural Decision Support System",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(health.router)
app.include_router(database.router)


@app.get("/", tags=["Home"])
def home():
    return {
        "message": "Welcome to AgriSmart AI",
        "status": "Backend is running",
    }