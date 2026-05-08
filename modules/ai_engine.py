from groq import Groq
from dotenv import load_dotenv
import os
import json
from modules.feedback import add_log
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

Your personality:
- Intelligent
- Supportive
- Organized
- Calm
- Personalized
- Practical

Your goals:
- Help the user manage life better
- Give contextual recommendations
- Adapt using user memory
- Feel like a real personal assistant

USER MEMORY:
{memory}

RECENT USER LOGS:
{logs[-2:]}

USER QUERY:
{user_query}

Respond in a helpful, warm, intelligent, and personalized way.
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
        reply = response.choices[0].message.content

        add_log(user_query, reply)
        return reply

    except Exception as e:
        return f"Error: {str(e)}"