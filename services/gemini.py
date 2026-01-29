# services/gemini.py
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def refine_text(text):
    response = model.generate_content(f"Improve this sentence: {text}")
    return response.text
