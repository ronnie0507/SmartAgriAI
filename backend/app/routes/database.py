
from fastapi import APIRouter, HTTPException

from app.database.connection import check_database_connection

router = APIRouter(tags=["Database"])


@router.get("/database/health")
def database_health():
    try:
        check_database_connection()

        return {
            "database": "MongoDB",
            "status": "connected",
        }

    except Exception:
        raise HTTPException(
            status_code=503,
            detail="MongoDB is unavailable",
        )
