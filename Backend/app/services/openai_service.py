import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

async def get_job_insights(
    zip_code: str, work_location: str, field_of_work: str
) -> str:
    prompt = (
        f"A job seeker from zip code {zip_code} is looking for a {work_location} position "
        f"in the field of {field_of_work}. Based on the current US job market trends, "
        f"provide 3-5 tailored job suggestions with brief descriptions, companies or sectors hiring, "
        f"and any advice or resources they should consider."
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4.0",
            messages=[
                {
                    "role": "system",
                    "content": "You're a helpful and knowledgeable career advisor.",
                },
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"Error fetching job insights: {e}"
