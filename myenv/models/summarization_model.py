import openai

# Set your OpenAI API key
openai.api_key = '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'

def analyze_sentiment(text, language="en"):
    """
    Perform sentiment analysis using the OpenAI API.

    :param text: The text to be analyzed.
    :param language: The language of the input text (default: 'en' for English).
    :return: Sentiment analysis result.
    """
    try:
        # Define language-specific labels for sentiment analysis
        language_labels = {
            "en": ["Positive", "Negative", "Neutral"],
            # Add more languages and corresponding labels as needed
        }

        # Use the OpenAI API for sentiment analysis
        response = openai.Completion.create(
            engine="davinci",
            prompt=f"Translate the following text to sentiment: '{text}' (in {language})",
            max_tokens=1,
            temperature=0,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None,
            labels=language_labels[language]
        )

        # Extract the sentiment label from the API response
        sentiment_label = response.choices[0].text.strip()
        return sentiment_label
    except Exception as e:
        # Handle any errors or exceptions here
        print("Error in sentiment analysis:", str(e))
        return "Error in sentiment analysis."

# Example usage:
# text = "This is a great product!"
# sentiment = analyze_sentiment(text)
# print(sentiment)
