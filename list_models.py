import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

print("Models available to your key that support generateContent:\n")
for m in client.models.list():
    if "generateContent" in getattr(m, "supported_actions", []):
        print(m.name)
