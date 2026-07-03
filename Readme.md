# 🤖 SHL AI Assessment Recommendation System

An AI-powered conversational recommendation system that helps recruiters identify the most suitable SHL assessments based on hiring requirements.

The application combines Retrieval-Augmented Generation (RAG) with a Large Language Model (LLM) to retrieve relevant assessments from the SHL product catalog and generate grounded recommendations.

---

## 🚀 Features

- Conversational hiring assistant
- Retrieval-Augmented Generation (RAG)
- Intelligent assessment recommendations
- Clarification questions for vague queries
- Off-topic query detection
- Grounded responses using Groq Llama 3.3 70B
- REST API built with FastAPI
- Interactive API documentation using Swagger UI

---

## 🏗️ System Architecture

```
User Query
      │
      ▼
FastAPI REST API
      │
      ▼
TF-IDF Retrieval
      │
      ▼
Cosine Similarity Ranking
      │
      ▼
Top Relevant SHL Assessments
      │
      ▼
Groq Llama 3.3 70B Versatile
      │
      ▼
Final Recommendation
```

---

## 📁 Project Structure

```
SHL-AI-Assessment-Recommender/
│
├── app/
│   ├── chatbot.py
│   ├── retriever.py
│   └── scraper.py
│
├── data/
│   └── shl_product_catalog_fixed.json
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── main.py
├── requirements.txt
├── README.md
└── .env.example
```

---

## ⚙️ Technologies Used

- Python
- FastAPI
- Groq API
- Llama 3.3 70B Versatile
- TF-IDF Vectorizer
- Cosine Similarity
- HTML
- CSS
- JavaScript

---

## 📌 API Endpoints

### Health Check

```
GET /health
```

Response

```json
{
  "status": "ok"
}
```

---

### Chat Endpoint

```
POST /chat
```

Example Request

```json
{
  "messages": [
    {
      "role": "user",
      "content": "I want to hire a Python Backend Developer with 2 years of experience."
    }
  ]
}
```

---

## 💡 Retrieval Pipeline

1. User submits hiring requirements.
2. Query is checked for clarification or off-topic intent.
3. TF-IDF Vectorizer converts the query into feature vectors.
4. Cosine Similarity retrieves the Top-5 relevant SHL assessments.
5. Retrieved assessments are passed to Groq Llama 3.3 70B.
6. The LLM generates grounded recommendations.

---

## 🧠 Prompt Design

The LLM is instructed to:

- Recommend only retrieved SHL assessments.
- Never invent assessment names.
- Explain recommendations briefly.
- Keep responses concise.
- Maintain a professional tone.

---

## 📊 Evaluation

The application was evaluated using:

- Retrieval relevance
- Recommendation quality
- Grounded responses
- Clarification handling
- Off-topic detection
- API validation

---

## 🖥️ Local Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/SHL-AI-Assessment-Recommender.git
```

Move into the project

```bash
cd SHL-AI-Assessment-Recommender
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

Run the application

```bash
python -m uvicorn main:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

## 🌐 Deployment

The application is deployed on Railway.

Public API

```
https://YOUR-RAILWAY-URL
```

Swagger Documentation

```
https://YOUR-RAILWAY-URL/docs
```

---

## 🔮 Future Improvements

- Hybrid Retrieval (BM25 + Dense Retrieval)
- Cross-Encoder Re-ranking
- Conversation Memory
- Response Caching
- Better Frontend UI
- Quantitative Evaluation Metrics

---
