import os
from groq import Groq

def generate_ai_explanation(condition, symptoms):
    """
    Generates AI-based suggestions using Groq.
    Safe, optional, and non-diagnostic.
    """

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return None

    client = Groq(api_key=api_key)

    prompt = f"""
    A user has the following symptoms: {', '.join(symptoms)}.
    The possible condition is {condition}.

    Provide simple health suggestions and precautions.
    Do NOT give medical diagnosis.
    Keep it short and easy to understand.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    return response.choices[0].message.content

