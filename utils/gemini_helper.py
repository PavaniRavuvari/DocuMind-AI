import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_answer(context, question):

    prompt = f"""
    Answer ONLY using the provided context.

    Context:
    {context}

    Question:
    {question}
    """

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:

        error_text = str(e)

        if "429" in error_text:

            return """
    ⚠️ Gemini API limit reached.

    Please wait 1 minute and try again.
    """

        return """
    ⚠️ Unable to generate response.
    """