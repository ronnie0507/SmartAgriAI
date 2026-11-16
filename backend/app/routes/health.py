
from fastapi import APIRouter

router = APIRouter(tags=["System Health"])


@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "AgriSmart AI",
        "message": "Backend is running successfully"
    }
