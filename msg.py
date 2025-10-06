from transformers import pipeline
import re

def clean_text(text):
    """Clean generated text: remove newlines, excessive spaces, non-printable chars."""
    if not text:
        return None
    # Remove non-printable / weird characters
    text = re.sub(r"[^\x20-\x7E]+", "", text)
    # Take only first line
    text = text.splitlines()[0].strip()
    # Skip empty or single punctuation outputs
    if not text or all(ch in ".,;:!?-—–" for ch in text):
        return None
    return text

def generate_messages(num_messages=5):
    generator = pipeline("text-generation", model="distilgpt2")

    prompt = "Write a very short, positive, one-line self motivational message:"

    messages = set()
    attempts = 0
    max_attempts = num_messages * 5  # retry limit

    while len(messages) < num_messages and attempts < max_attempts:
        result = generator(
            prompt,
            max_new_tokens=15,  # very short
            do_sample=True,
            temperature=0.8,
            pad_token_id=50256  # eos_token_id
        )

        raw_text = result[0]["generated_text"].replace(prompt, "").strip()
        clean = clean_text(raw_text)
        if clean:
            messages.add(clean)

        attempts += 1

    # Fill with deterministic fallbacks if generation fails
    fallback_list = [
        "Keep going! Every step counts.",
        "Small steps lead to big results.",
        "Believe in yourself today.",
        "One step at a time is enough.",
        "You are stronger than you think."
    ]
    while len(messages) < num_messages:
        for fallback in fallback_list:
            messages.add(fallback)
            if len(messages) >= num_messages:
                break

    # Print messages
    print("\n🌞 Motivational Messages:\n")
    for i, msg in enumerate(messages, 1):
        print(f"{i}. {msg}")

if __name__ == "__main__":
    generate_messages()
