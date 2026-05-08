import json

MEMORY_FILE = "memory.json"

def load_memory():

    with open(MEMORY_FILE, "r") as file:
        return json.load(file)

def save_memory(memory):

    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)

def add_preference(category, value):

    memory = load_memory()

    memory["preferences"][category] = value

    save_memory(memory)

def add_feedback(feedback):

    memory = load_memory()

    memory["feedback"].append(feedback)

    save_memory(memory)