import json
from datetime import datetime

LOG_FILE = "logs.json"

def load_logs():

    with open(LOG_FILE, "r") as file:
        return json.load(file)

def save_logs(logs):

    with open(LOG_FILE, "w") as file:
        json.dump(logs, file, indent=4)

def add_log(user_query, sara_response):

    logs = load_logs()
    logs = logs[-20:]
    logs.append({
        "time": str(datetime.now()),
        "query": user_query,
        "response": sara_response
    })

    save_logs(logs)