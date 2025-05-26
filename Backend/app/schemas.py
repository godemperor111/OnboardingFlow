from pydantic import BaseModel
from typing import Literal


class OnboardingRequest(BaseModel):
    zip_code: str
    work_location: Literal["remote", "hybrid", "in-person"]
    field_of_work: Literal["tech", "finance", "healthcare", "education", "business", "service", "creative", "non-profit", "other"]


class JobInsightResponse(BaseModel):
    insights: str