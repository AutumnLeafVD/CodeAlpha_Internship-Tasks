# TASK-1
# Language Translation Tool

# Importing Necessary Libraries

from googletrans import Translator

# Setting-Up The Translator
translator=Translator()

#Defining Function To Translate The Text
def translate_text(text, src_lang, dest_lang):
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    return translation.text

# Implementing The Main Logic
def main():
    # Sample text and languages
    text = "Hello, how are you?"
    source_language = 'en'  # English
    destination_language = 'es'  # Spanish

    # Translate the text
    translated_text = translate_text(text, source_language, destination_language)

    # Display the result
    print(f"Original text: {text}")
    print(f"Translated text: {translated_text}")

if __name__ == "__main__":
    main()

# Defining User-Input
def main():
    # User inputs
    text = input("Enter the text to translate: ")
    source_language = input("Enter the source language code: ")
    destination_language = input("Enter the destination language code: ")

    # Translate the text
    translated_text = translate_text(text, source_language, destination_language)

    # Display the result
    print(f"Original text: {text}")
    print(f"Translated text: {translated_text}")

if __name__ == "__main__":
    main()

