import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def refine_sentence(raw_text):
    if raw_text == "UNKNOWN":
        return None
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=f"Convert this sign language output into a natural English sentence: {raw_text}"
        )
        return response.text.strip()
    except:
        return raw_text
