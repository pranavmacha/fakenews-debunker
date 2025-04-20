import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")


def summarize_article(text):
    prompt = f"Summarize the following article in 3 bullet points:\n\n{text[:3000]}"
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Summary failed: {str(e)}"
