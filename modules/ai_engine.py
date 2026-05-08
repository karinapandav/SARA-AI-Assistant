from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def load_memory():
    with open("memory.json", "r") as file:
        return json.load(file)

def load_logs():
    with open("logs.json", "r") as file:
        return json.load(file)

def ask_sara(user_query):

    memory = load_memory()
    logs = load_logs()

    prompt = f"""
You are SARA (Smart Adaptive Response Assistant).

Your role:
- Be personalized
- Understand user habits
- Give practical recommendations
- Respond intelligently and warmly

USER MEMORY:
{memory}

RECENT LOGS:
{logs[-5:]}

USER QUERY:
{user_query}

Give a personalized response.
"""

    try:

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "You are SARA, a personalized AI assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"