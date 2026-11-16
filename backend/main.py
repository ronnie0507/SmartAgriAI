
from fastapi import FastAPI
from app.routes import health

app = FastAPI(
    title="AgriSmart AI",
    description="AI-Assisted Agricultural Decision Support System",
    version="1.0.0"
)

# Register API routes
app.include_router(health.router)


@app.get("/", tags=["Home"])
def home():
    return {
        "message": "Welcome to AgriSmart AI",
        "status": "Backend is running"
    }
