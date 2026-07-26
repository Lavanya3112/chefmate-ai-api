import os
from google import genai
from dotenv import load_dotenv
from prompts import PERSONA

load_dotenv()

_client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def get_ai_response(user_prompt: str) -> str:
    """Same logic as your Streamlit get_ai_response() — unchanged, new SDK."""
    prompt = f"""
{PERSONA}

{user_prompt}
"""
    response = _client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt,
    )
    return response.text
