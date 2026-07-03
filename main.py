import os

print("========== START ==========")
print("ENV KEY:", os.environ.get("GROQ_API_KEY"))
print("===========================")

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from app.retriever import SHLRetriever
from app.chatbot import ask_llm
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="SHL Assessment Recommender",
    version="1.0"
)
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

retriever = SHLRetriever()


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat")
def chat(request: ChatRequest):

    # -----------------------------
    # Full conversation history
    # -----------------------------
    conversation = "\n".join(
        f"{m.role}: {m.content}" for m in request.messages
    )

    latest_query = request.messages[-1].content
    query = latest_query.lower().strip()

    # -----------------------------
    # Off-topic detection
    # -----------------------------
    off_topics = [
        "prime minister",
        "president",
        "weather",
        "cricket",
        "ipl",
        "football",
        "movie",
        "music",
        "bitcoin",
        "crypto",
        "stock market",
        "recipe",
        "covid",
        "youtube",
        "netflix"
    ]

    if any(word in query for word in off_topics):
        return {
            "reply": "Sorry, I can only answer questions related to SHL assessments and hiring assessments.",
            "recommendations": [],
            "end_of_conversation": False
        }

    # -----------------------------
    # Clarification detection
    # -----------------------------
    vague_queries = [
        "assessment",
        "test",
        "hire",
        "hiring",
        "recommend",
        "need assessment",
        "assessment needed",
        "need test",
        "help",
        "assessment please"
    ]

    role_keywords = [
        "developer",
        "engineer",
        "manager",
        "analyst",
        "consultant",
        "architect",
        "administrator",
        "designer",
        "tester",
        "qa",
        "scientist",
        "lead",
        "intern"
    ]

    has_role = any(role in query for role in role_keywords)

    if query in vague_queries or (len(query.split()) <= 2 and not has_role):
        return {
            "reply": (
                "Could you please tell me:\n\n"
                "1. Which role are you hiring for?\n"
                "2. Experience level?\n"
                "3. Any technical or behavioural skills you want to assess?"
            ),
            "recommendations": [],
            "end_of_conversation": False
        }

    # -----------------------------
    # Retrieve recommendations
    # -----------------------------
    recommendations = retriever.search(
        conversation,
        top_k=5
    )

    # -----------------------------
    # Generate response using LLM
    # -----------------------------
    reply = ask_llm(
        conversation,
        recommendations
    )

    # -----------------------------
    # Final Response
    # -----------------------------
    return {
        "reply": reply,
        "recommendations": recommendations,
        "end_of_conversation": False
    }