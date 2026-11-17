
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class FarmCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)

    area_acres: float = Field(gt=0)

    address: str

    latitude: Optional[float] = Field(
        default=None, ge=-90, le=90
    )

    longitude: Optional[float] = Field(
        default=None, ge=-180, le=180
    )


class FarmResponse(BaseModel):
    id: str
    owner_uid: str
    name: str
    area_acres: float
    address: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    created_at: datetime
