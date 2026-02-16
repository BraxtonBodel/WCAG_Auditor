from pydantic import BaseModel, ConfigDict
from typing import List, Optional

class GuidelineCreate(BaseModel):
    success_criterion: str
    description: str
    level: str

    model_config = ConfigDict(
        from_attributes = True,
        json_schema_extra = {
            "example": {
                "success_criterion": "1.1.1",
                "description": "Non-text Content: All non-text content that is presented to the user has a text alternative that serves the equivalent purpose.",
                "level": "A"
            }
        }
    )

class GuidelineResponse(GuidelineCreate):
    id:int