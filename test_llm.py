from app.chatbot import ask_llm

reply = ask_llm(
    "I want to hire a Java Developer",
    [
        "JavaScript (New)",
        ".NET Framework",
        "Core Java"
    ]
)

print(reply)