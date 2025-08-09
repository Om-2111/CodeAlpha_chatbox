import datetime

# Function to get bot response based on keywords
def get_bot_response(user_input):
    user_input = user_input.lower()

    if any(greet in user_input for greet in ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]):
        return "Hi! How can I help you today?"

    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"

    elif any(word in user_input for word in ["bye", "goodbye", "see you"]):
        return "Goodbye! Have a wonderful day!"

    else:
        return "Hmm... I’m not sure I understand, but I’m learning every day!"

# Function to log conversations to a file
def log_conversation(user_input, bot_response):
    with open("chat_log.txt", "a") as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] You: {user_input}\n")
        log_file.write(f"[{timestamp}] Bot: {bot_response}\n")

# Main chatbot function
def chatbot():
    print("Welcome to the Chatbot! (Type 'bye' to exit)")
    while True:
        user_input = input("You: ")
        bot_response = get_bot_response(user_input)
        print("Bot:", bot_response)
        
        # Log the conversation
        log_conversation(user_input, bot_response)
        
        if "bye" in user_input.lower():
            break

# Run the chatbot
chatbot()
