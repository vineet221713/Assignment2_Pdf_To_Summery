import openai

# Set your OpenAI API key
openai.api_key = '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'

def summarize_documents(documents):
    """
    Summarize multiple documents using the OpenAI API.

    :param documents: List of documents to be summarized.
    :return: A coherent summary of the input documents.
    """
    try:
        # Combine the input documents into a single string
        input_text = '\n'.join(documents)

        # Use the OpenAI API for summarization
        response = openai.Completion.create(
            engine="davinci",
            prompt=f"Please summarize the following documents:\n{input_text}\nSummary:",
            max_tokens=150  # Adjust the max_tokens as needed
        )

        # Extract the generated summary from the API response
        summary = response.choices[0].text.strip()
        return summary
    except Exception as e:
        # Handle any errors or exceptions here
        print("Error in summarization:", str(e))
        return "Error in summarization."

# Example usage:
# documents = ["Document 1 text.", "Document 2 text.", "Document 3 text."]
# summary = summarize_documents(documents)
# print(summary)
