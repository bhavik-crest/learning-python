from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import datetime

def categorize_query(user_input):
    user_input_lower = user_input.lower()
    if "hello" in user_input_lower or "hi" in user_input_lower:
        return "greeting"
    elif "time" in user_input_lower:
        return "time"
    elif "weather" in user_input_lower:
        return "weather"
    else:
        return "general"

def handle_custom_response(category):
    if category == "greeting":
        return "Hello! How are you today?"
    elif category == "time":
        now = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The current time is {now}"
    elif category == "weather":
        return "Sorry, I can't provide live weather updates yet 🌤️"
    else:
        return None  # Let DialoGPT handle general queries

# Load pre-trained small DialoGPT model from Hugging Face
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small")

# Start conversation
chat_history_ids = None
print("🤖 AI Chatbot Ready! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot: Goodbye! 👋")
        break

    # Categorize user input
    category = categorize_query(user_input)
    custom_response = handle_custom_response(category)

    if custom_response:
        print("Bot:", custom_response)
        continue

    # Encode user input for DialoGPT
    new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
    bot_input_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1) if chat_history_ids is not None else new_input_ids

    output_ids = model.generate(
        bot_input_ids,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.75
    )

    chat_history_ids = output_ids
    response = tokenizer.decode(output_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    print("Bot:", response)

