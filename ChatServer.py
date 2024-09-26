# 定義聊天機器人的回應邏輯
def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "your name" in user_input:
        return "I am a simple ChatBot."
    elif "how are you" in user_input:
        return "I'm just a bunch of code, but I'm doing great! How about you?"
    elif "bye" in user_input or "quit" in user_input:
        return "Goodbye! Have a nice day!"
    else:
        return "I'm sorry, I don't understand that."

# 啟動聊天機器人
def start_chat():
    print("Hi, I'm ChatBot. Type 'bye' or 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "quit"]:
            print("ChatBot: Goodbye! Have a nice day!")
            break
        response = get_response(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    start_chat()