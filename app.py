from flask import Flask, request, jsonify, render_template
from PyPDF2 import PdfReader


import openai
# import pdfplumber



app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = ""


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate-text", methods=["POST"])
def generate_text():
    data = request.json
    keyword = data.get("keyword")

    # Use a more detailed prompt and context
    prompt = f"Write a detailed paragraph about {keyword} and its significance in human life."
    context = f"This is a text about {keyword} and its impact on human existence."

    # Combine context and prompt
    input_text = f"{context}\n{prompt}"

    # Adjust these parameters for better results
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=input_text,
        max_tokens=150,  # Adjust based on your desired text length
        temperature=0.7,  # Adjust as needed
        n=1,
    )

    generated_text = response.choices[0].text.strip()

    return jsonify({"generated_text": generated_text})


@app.route("/summarization", methods=["POST"])
def summarization():
    try:
        uploaded_files = request.files.getlist("files")
        summary_request = request.form.get("summaryRequest")
        file_contents = []

        if not uploaded_files or len(uploaded_files) == 0:
            return jsonify({"error": "Please upload at least one valid file."}), 400

        for file in uploaded_files:
            content = ""
            if file.mimetype == "text/plain":
                content = file.read().decode("utf-8")
            elif file.mimetype == "application/pdf":
                pdf_reader = PdfReader(file)
                content = ""
                for page in pdf_reader.pages:
                    content += page.extract_text()

            file_contents.append(content)

        messages = [
            {"role": "system", "content": "You are a summarization assistant."},
            {"role": "user", "content": f"Please make a summary of the content from the below files for: {summary_request}"},
            * [{"role": "user", "content": content} for content in file_contents],
        ]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

        summary = response["choices"][0]["message"]["content"]
        return jsonify({"summary": summary})

    except Exception as e:
        app.logger.error(f"Error in /summarization route: {str(e)}")
        return (
            jsonify({"error": "An error occurred while processing the request."}),
            500,
        )


    
if __name__ == "__main__":
    app.run()
