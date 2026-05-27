import streamlit as st
import os
from groq import Groq

def get_client():
    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except:
        api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("❌ GROQ_API_KEY not found. Please set it in Streamlit Secrets.")

    return Groq(api_key=api_key)


def get_llm_response(prompt):
    client = get_client()

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-8b-8192",
        temperature=0.3,
        max_tokens=300
    )

    return response.choices[0].message.content