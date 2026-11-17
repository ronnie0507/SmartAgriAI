
from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    firebase_uid: str
    full_name: str = Field(min_length=2, max_length=100)
    email: Optional[EmailStr] = None
    phone: Optional[str] = None


class UserResponse(BaseModel):
    id: str
    firebase_uid: str
    full_name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    role: str = "farmer"
    created_at: datetime
