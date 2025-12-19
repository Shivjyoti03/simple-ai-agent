# AI Task Automation Agent (Beginner Friendly)

import datetime
import os

def ai_agent():
    memory = {
        "name": None,
        "messages": []
    }

    print("🤖 Task Automation AI Agent Activated!")
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
                print(f"Agent: Hello, {memory['name']} 😊")
            else:
                print("Agent: Hello! What is your name?")

        elif "my name is" in user_input:
            name = user_input.replace("my name is", "").strip()
            memory["name"] = name.capitalize()
            print(f"Agent: Nice to meet you, {memory['name']}!")

        elif user_input == "time":
            now = datetime.datetime.now()
            print("Agent: Current date & time:", now.strftime("%Y-%m-%d %H:%M:%S"))

        elif user_input.startswith("create file"):
            filename = user_input.replace("create file", "").strip()
            if filename:
                with open(filename, "w") as f:
                    f.write("This file was created by the AI automation agent.\n")
                print(f"Agent: File '{filename}' created successfully 📄")
            else:
                print("Agent: Please provide a filename.")

        elif user_input.startswith("read file"):
            filename = user_input.replace("read file", "").strip()
            if os.path.exists(filename):
                with open(filename, "r") as f:
                    print("Agent: File contents:")
                    print(f.read())
            else:
                print("Agent: File not found ❌")

        elif "remember" in user_input:
            print("Agent: Here is what I remember:")
            print(f"- Name: {memory['name']}")
            print(f"- Messages: {len(memory['messages'])}")

        elif "exit" in user_input:
            print("Agent: Shutting down. Goodbye! 👋")
            break

        else:
            print("Agent: Command not recognized yet.")

if __name__ == "__main__":
    ai_agent()


