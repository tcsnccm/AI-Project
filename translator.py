from transformers import MarianMTModel, MarianTokenizer

# Load the pretrained MarianMT model for Arabic-English translation
model_name = "Helsinki-NLP/opus-mt-ar-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def translate_ar_to_en(text):
    # Tokenize input text
    inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
    # Generate translation
    translated = model.generate(**inputs)
    # Decode translation
    translation = tokenizer.decode(translated[0], skip_special_tokens=True)
    return translation

# Example usage
arabic_text = "مرحبا بك في عالم الذكاء الاصطناعي"
english_translation = translate_ar_to_en(arabic_text)
print("Translated Text:", english_translation)
