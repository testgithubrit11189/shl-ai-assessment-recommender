import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def ask_llm(user_query, recommendations):

    prompt = f"""
You are an SHL Assessment Recommendation Assistant.

Your job is to recommend ONLY assessments provided below.

STRICT RULES:

1. Never invent assessment names.
2. Never recommend anything outside the provided list.
3. Explain why each assessment matches the user's hiring needs.
4. Keep the answer under 200 words.
5. Be professional.
6. Mention assessment names exactly as given.

User Query:
{user_query}

Available Assessments:
{recommendations}

Return a short recommendation summary.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an expert SHL assessment recommendation assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0,
        max_tokens=300
    )

    return response.choices[0].message.content