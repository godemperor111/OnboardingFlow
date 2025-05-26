from openai import OpenAI
import os
from dotenv import load_dotenv
from openai import RateLimitError, AuthenticationError
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MOCK_RESPONSE = """
1. **Software Developer (Remote)** - Tech companies like Google, Microsoft, and startups are hiring remote developers. Knowledge of full-stack technologies is highly sought after.
2. **Data Analyst (Hybrid)** - Finance and healthcare sectors need data professionals. Tools like SQL, Python, and Power BI are in demand.
3. **Cybersecurity Analyst (Remote)** - With increasing online threats, firms across sectors are hiring security experts. Certifications like CompTIA Security+ help.
4. **IT Support Specialist (On-site or Remote)** - Good entry-level opportunities. Focus on troubleshooting, customer support, and networking skills.
5. **Cloud Engineer (Remote)** - AWS, Azure, and GCP skills are valuable. Many roles available in tech and enterprise companies.

💡 Consider upskilling via platforms like Coursera or LinkedIn Learning. Check job boards like Indeed, Glassdoor, and BuiltIn for opportunities.
"""


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
        response = client.chat.completions.create(
            model="gpt-4",  
            messages=[
                {
                    "role": "system",
                    "content": "You're a helpful and knowledgeable career advisor.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=500,
        )
        return response.choices[0].message.content.strip()
    except (RateLimitError, AuthenticationError):
        return f"⚠️ Unable to fetch live job insights right now, but here are some general suggestions:\n\n{MOCK_RESPONSE}"

    except Exception as e:
        return f"⚠️ Unexpected issue occurred. Here's a general job guide to help you out:\n\n{MOCK_RESPONSE}"