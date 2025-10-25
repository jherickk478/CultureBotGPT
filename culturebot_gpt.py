# culturebot_gpt.py
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_culturebot(question):
    """
    Sends a question to OpenAI and returns CultureBot GPT's response.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are CultureBot GPT, a friendly Filipino storyteller and culture expert."},
                {"role": "user", "content": question}
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ Error: {str(e)}"
