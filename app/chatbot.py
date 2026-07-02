import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Read API key
api_key = os.environ.get("GROQ_API_KEY")

# Debug
print("========== CHATBOT ==========")
print("GROQ_API_KEY FOUND:", api_key is not None)
print("=============================")

if not api_key:
    raise RuntimeError(
        "GROQ_API_KEY is missing! Please set it in Railway Variables."
    )

# Initialize Groq client
client = Groq(api_key=api_key)


def ask_llm(user_query, recommendations):

    prompt = f"""
You are an SHL Assessment Recommendation Assistant.

Your task is to recommend ONLY assessments from the provided list.

STRICT RULES:

1. Never invent assessment names.
2. Recommend ONLY from the available assessments.
3. Explain briefly why each recommendation matches.
4. Keep the answer under 200 words.
5. Mention assessment names exactly as provided.

User Query:
{user_query}

Available Assessments:
{recommendations}

Return a concise recommendation.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an expert SHL Assessment Recommendation Assistant."
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