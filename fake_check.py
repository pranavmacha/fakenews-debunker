import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv


load_dotenv()


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("models/gemini-1.5-flash-latest")



def analyze_verdict(headline, summaries):
    joined = "\n\n".join(summaries)
    
    prompt = f"""
A user read the following headline: "{headline}"

They found these summaries of real news articles:

{joined}

Based on the above, is the headline likely real, fake, or unclear? Give a one-line verdict.
"""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Could not determine: {str(e)}"
