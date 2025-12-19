# Simple AI Agent (Beginner Friendly)

def ai_agent():
    print("🤖 AI Agent Activated!")
    print("I can help with: hello, help, or exit")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input:
            print("Agent: Hello! Nice to meet you 😊")

        elif "help" in user_input:
            print("Agent: I am a simple rule-based AI agent.")
            print("Try saying hello or type exit to quit.")

        elif "exit" in user_input:
            print("Agent: Goodbye! 👋")
            break

        else:
            print("Agent: Sorry, I don't understand yet.")

if __name__ == "__main__":
    ai_agent()
