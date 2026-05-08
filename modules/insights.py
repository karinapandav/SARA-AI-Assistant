from modules.feedback import load_logs
from modules.ai_engine import ask_sara

def generate_insights():

    logs = load_logs()

    if not logs:
        return "Not enough data yet."

    recent_logs = logs[-10:]

    formatted_logs = ""

    for log in recent_logs:

        formatted_logs += f"""
User Query: {log['query']}
SARA Response: {log['response']}
"""

    prompt = f"""
Analyze the following user interactions.

Identify:
- behavioral patterns
- productivity habits
- lifestyle preferences
- possible improvements
- motivational insights

USER INTERACTIONS:
{formatted_logs}

Give concise and practical personalized insights.
"""

    insights = ask_sara(prompt)

    return insights