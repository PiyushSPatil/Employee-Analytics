from groq import Groq
from config.config import GROQ_API_KEY

# Initialize client
client = Groq(api_key=GROQ_API_KEY)

def get_llm_response(prompt):
    """
    Send prompt to Groq LLM and return response
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # powerful model
            messages=[
                {"role": "system", "content": "You are an expert HR data analyst."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"