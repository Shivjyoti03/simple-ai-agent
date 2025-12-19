# AI Agent with Persistent Memory (Beginner Friendly)

import json
import os
import datetime

MEMORY_FILE = "memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {"name": None, "messages": []}

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

def ai_agent():
    memory = load_memory()

    print("🤖 AI Agent with Persistent Memory Activated!")
    if memory["name"]:
        print(f"Welcome back, {memory['name']} 😊")
    else:
        print("Hello! I don't know your name yet.")

    print("Commands:")
    print("- hello")
    print("- my name is <name>")
    print("- time")
    print("- create file <filename>")
    print("- read file <filename>")
    print("- remember")
    print("- exit")

    while True:
        user_input = input("You: ").lower()
        memory["messages"].append(user_input)

        if "hello" in user_input:
            if memory["name"]:
                print(f"Agent: Hello again, {memory['name']}!")
            else:
                print("Agent: Hello! What is your name?")

        elif "my name is" in user_input:
            name = user_input.replace("my name is", "").strip()
            memory["name"] = name.capitalize()
            print(f"Agent: Got it! I'll remember you, {memory['name']}.")

        elif user_input == "time":
            now = datetime.datetime.now()
            print("Agent:", now.strftime("%Y-%m-%d %H:%M:%S"))

        elif user_input.startswith("create file"):
            filename = user_input.replace("create file", "").strip()
            if filename:
                with open(filename, "w") as f:
                    f.write("Created by AI Agent with persistent memory.\n")
                print(f"Agent: File '{filename}' created 📄")

        elif user_input.startswith("read file"):
            filename = user_input.replace("read file", "").strip()
            if os.path.exists(filename):
                with open(filename, "r") as f:
                    print("Agent: File content:")
                    print(f.read())
            else:
                print("Agent: File not found ❌")

        elif "remember" in user_input:
            print("Agent: Here's what I remember:")
            print(f"- Name: {memory['name']}")
            print(f"- Total messages: {len(memory['messages'])}")

        elif "exit" in user_input:
            save_memory(memory)
            print("Agent: Memory saved. Goodbye! 👋")
            break

        else:
            print("Agent: I'm learning...")

        save_memory(memory)

if __name__ == "__main__":
    ai_agent()




