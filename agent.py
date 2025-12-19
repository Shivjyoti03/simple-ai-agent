# Simple AI Agent with Memory (Beginner)

def ai_agent():
    memory = {
        "name": None,
        "messages": []
    }

    print("🤖 AI Agent with Memory Activated!")
    print("I can remember your name and our conversation.")
    print("Commands: hello, my name is <name>, remember, exit")

    while True:
        user_input = input("You: ").lower()
        memory["messages"].append(user_input)

        if "hello" in user_input:
            if memory["name"]:
                print(f"Agent: Hello again, {memory['name']} 😊")
            else:
                print("Agent: Hello! What is your name?")

        elif "my name is" in user_input:
            name = user_input.replace("my name is", "").strip()
            memory["name"] = name.capitalize()
            print(f"Agent: Nice to meet you, {memory['name']}! I will remember you.")

        elif "remember" in user_input:
            print("Agent: Here is what I remember:")
            print(f"- Your name: {memory['name']}")
            print(f"- Messages count: {len(memory['messages'])}")

        elif "exit" in user_input:
            print("Agent: Goodbye! I won't forget you 👋")
            break

        else:
            print("Agent: I'm still learning, but I'm listening 👀")

if __name__ == "__main__":
    ai_agent()

