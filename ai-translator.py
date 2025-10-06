# pip install transformers sentencepiece torch

from transformers import MarianMTModel, MarianTokenizer

# Mapping language codes to specific English->target models
MODEL_MAPPING = {
    "fr": "Helsinki-NLP/opus-mt-en-fr",
    "es": "Helsinki-NLP/opus-mt-en-es",
    "de": "Helsinki-NLP/opus-mt-en-de",
    "it": "Helsinki-NLP/opus-mt-en-it",
    "pt": "Helsinki-NLP/opus-mt-en-pt",
    "ru": "Helsinki-NLP/opus-mt-en-ru",
    "hi": "Helsinki-NLP/opus-mt-en-hi",
    "gu": "Helsinki-NLP/opus-mt-en-gu",
    "ja": "Helsinki-NLP/opus-mt-en-ja",
    "zh": "Helsinki-NLP/opus-mt-en-zh",
}

# Friendly names
SUPPORTED_LANGUAGES = {
    "fr": "French",
    "es": "Spanish",
    "de": "German",
    "it": "Italian",
    "pt": "Portuguese",
    "ru": "Russian",
    "hi": "Hindi",
    "gu": "Gujarati",
    "ja": "Japanese",
    "zh": "Chinese",
}

MODEL_CACHE = {}

def load_model(target_lang):
    if target_lang in MODEL_CACHE:
        return MODEL_CACHE[target_lang]

    model_name = MODEL_MAPPING[target_lang]
    try:
        print(f"⚡ Loading model for {SUPPORTED_LANGUAGES[target_lang]} (first time, may take 30-60s)...")
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model = MarianMTModel.from_pretrained(model_name)
        MODEL_CACHE[target_lang] = (tokenizer, model)
        print("✅ Model loaded successfully.")
        return tokenizer, model
    except Exception as e:
        print(f"❌ Failed to load model: {e}")
        return None, None

def translate_text(text, target_lang):
    target_lang = target_lang.lower()
    if target_lang not in SUPPORTED_LANGUAGES:
        print(f"❌ Language '{target_lang}' not supported.")
        return False

    tokenizer, model = load_model(target_lang)
    if tokenizer is None or model is None:
        print("❌ Cannot translate due to model load failure.")
        return False

    try:
        batch = tokenizer([text], return_tensors="pt", padding=True)
        translated = model.generate(**batch)
        translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
        print(f"\n✅ Translated Text ({SUPPORTED_LANGUAGES[target_lang]}): {translated_text}")
        return True
    except Exception as e:
        print(f"❌ Translation failed: {e}")
        return False

def main():
    print("🌐 AI Translator (Hugging Face Transformers)")
    text = input("Enter text to translate: ").strip()

    print("\nSupported languages:")
    for code, lang in SUPPORTED_LANGUAGES.items():
        print(f"{code}: {lang}")
    print()

    while True:
        target_lang = input("Enter target language code (e.g., 'fr'): ").strip()
        success = translate_text(text, target_lang)
        if success:
            break
        else:
            print("Please enter a valid language code or check your input.\n")

if __name__ == "__main__":
    main()
