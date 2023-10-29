import openai

# Set your OpenAI API key
openai.api_key = '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'

def generate_text(prompt, max_tokens=50):
    """
    Generate text based on a prompt using the OpenAI API.

    :param prompt: The input text prompt for text generation.
    :param max_tokens: The maximum number of tokens in the generated text (default: 50).
    :return: Generated text.
    """
    try:
        # Use the OpenAI API for text generation
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=max_tokens
        )

        # Extract the generated text from the API response
        generated_text = response.choices[0].text.strip()
        return generated_text
    except Exception as e:
        # Handle any errors or exceptions here
        print("Error in text generation:", str(e))
        return "Error in text generation."

# Example usage:
# prompt = "Once upon a time, in a land far, far away..."
# generated_text = generate_text(prompt)
# print(generated_text)
