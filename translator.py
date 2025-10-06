# Make sure you have deep-translator installed:
# pip install deep-translator

from deep_translator import GoogleTranslator

# Supported languages (subset from Google Translate)
SUPPORTED_LANGUAGES = {
    # "af": "Afrikaans",
    # "ar": "Arabic",
    # "bn": "Bengali",
    # "zh": "Chinese",
    # "cs": "Czech",
    # "da": "Danish",
    # "nl": "Dutch",
    "en": "English",
    "fr": "French",
    # "de": "German",
    # "el": "Greek",
    "gu": "Gujarati",
    "hi": "Hindi",
    # "it": "Italian",
    # "ja": "Japanese",
    # "ko": "Korean",
    # "pt": "Portuguese",
    # "ru": "Russian",
    # "es": "Spanish",
    # "sv": "Swedish",
    # "ta": "Tamil",
    # "tr": "Turkish",
}

def translate_text(text, target_lang):
    target_lang = target_lang.lower()

    if target_lang not in SUPPORTED_LANGUAGES:
        print(f"❌ Sorry, the language code '{target_lang}' is not supported.")
        return False

    try:
        translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
        print(f"\n✅ Translated Text ({SUPPORTED_LANGUAGES[target_lang]}):\n{translated}")
        return True
    except Exception as e:
        print("❌ Translation failed:", e)
        return False

def main():
    print("🌐 AI Language Translator (using Deep Translator)")
    text = input("Enter text to translate: ").strip()

    print("\nSupported languages and their codes:")
    for code, lang in SUPPORTED_LANGUAGES.items():
        print(f"{code}: {lang}")
    print("\n")

    while True:
        target_lang = input("Enter target language code (e.g., 'fr'): ").strip()
        success = translate_text(text, target_lang)
        if success:
            break
        else:
            print("Please enter a valid language code from the list above.\n")

if __name__ == "__main__":
    main()
