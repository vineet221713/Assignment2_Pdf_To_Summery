import openai

# Set your OpenAI API key
openai.api_key = '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'

def translate_text(text, source_language, target_language):
    """
    Translate text from the source language to the target language using the OpenAI API.

    :param text: The text to be translated.
    :param source_language: The language of the input text.
    :param target_language: The target language for translation.
    :return: Translated text.
    """
    try:
        # Use the OpenAI API for text translation
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Translate the following text from {source_language} to {target_language}: '{text}'",
            max_tokens=60
        )

        # Extract the translated text from the API response
        translation = response.choices[0].text.strip()
        return translation
    except Exception as e:
        # Handle any errors or exceptions here
        print("Error in translation:", str(e))
        return "Error in translation."

# Example usage:
# text = "Hello, how are you?"
# source_language = "en"
# target_language = "fr"
# translated_text = translate_text(text, source_language, target_language)
# print(translated_text)
