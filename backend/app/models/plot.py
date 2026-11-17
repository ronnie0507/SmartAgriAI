
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class PlotCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)

    area_acres: float = Field(gt=0)

    soil_type: Optional[str] = None

    irrigation_type: Optional[str] = None


class PlotResponse(BaseModel):
    id: str
    farm_id: str
    owner_uid: str
    name: str
    area_acres: float
    soil_type: Optional[str] = None
    irrigation_type: Optional[str] = None
    created_at: datetime
