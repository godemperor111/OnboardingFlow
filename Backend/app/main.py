from fastapi import FastAPI
from app.schemas import OnboardingRequest, JobInsightResponse
from app.services.openai_service import get_job_insights

app = FastAPI()


@app.post("/onboarding/insights", response_model=JobInsightResponse)
async def onboarding_insights(payload: OnboardingRequest):
    insights = await get_job_insights(
        zip_code=payload.zip_code,
        work_location=payload.work_location,
        field_of_work=payload.field_of_work,
    )
    return JobInsightResponse(insights=insights)
