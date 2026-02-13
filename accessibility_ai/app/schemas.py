from pydantic import BaseModel
from typing import List, Optional

class GuidelineCreate(BaseModel):
    succes_criterion: str
    description: str
    level: str

    class Config:
        from_attributes = True

class GuidelineResponse(GuidelineCreate):
    id:int