from fastapi import FastAPI
from pydantic import BaseModel
from gemini_client import get_ai_response

app = FastAPI(title="ChefMate AI API")


# ---------- Request schemas ----------

class TopicRequest(BaseModel):
    topic: str
    level: str  # "Beginner" | "Intermediate" | "Advanced"


class EvaluateRequest(BaseModel):
    topic: str
    student_answer: str


class AskRequest(BaseModel):
    question: str


# ---------- Health check ----------

@app.get("/")
def health_check():
    return {"status": "ChefMate AI API is running"}


# ---------- Routes (same prompts as your Streamlit app) ----------

@app.post("/explain")
def explain_concept(req: TopicRequest):
    prompt = f"""
Explain the topic '{req.topic}' to a {req.level.lower()} learner.

Include:
1. Introduction
2. Ingredients or tools needed (if applicable)
3. Step-by-step explanation
4. Common beginner mistakes
5. Healthy cooking tips
6. End with one review question.
"""
    return {"response": get_ai_response(prompt)}


@app.post("/example")
def real_life_example(req: TopicRequest):
    prompt = f"""
Provide one simple real-life cooking example for the topic '{req.topic}' suitable for a {req.level.lower()} learner.

Include:
- A relatable kitchen scenario
- Why this concept is important
- One common beginner mistake
- One practical tip
"""
    return {"response": get_ai_response(prompt)}


@app.post("/quiz")
def generate_quiz(req: TopicRequest):
    prompt = f"""
Generate 5 multiple-choice questions on '{req.topic}' for a {req.level.lower()} learner.

Each question should have:
- Four options (A, B, C, D)
- Correct answer
- Short explanation
"""
    return {"response": get_ai_response(prompt)}


@app.post("/evaluate")
def evaluate_answer(req: EvaluateRequest):
    if not req.student_answer.strip():
        return {"error": "Please enter your answer first."}

    prompt = f"""
The topic is '{req.topic}'.

Student's answer:
{req.student_answer}

Evaluate the answer.

Provide:
- Positive feedback
- Corrections (if any)
- Suggestions for improvement
- Encourage the learner
"""
    return {"response": get_ai_response(prompt)}


@app.post("/lesson")
def complete_lesson(req: TopicRequest):
    prompt = f"""
Teach '{req.topic}' to a {req.level.lower()} learner.

Structure the lesson as follows:

1. Introduction
2. Explanation
3. Step-by-step guide
4. Real-life example
5. Healthy cooking tips
6. Three practice questions
7. A short quiz
8. Lesson summary
"""
    return {"response": get_ai_response(prompt)}


@app.post("/ask")
def ask_lavanya(req: AskRequest):
    if not req.question.strip():
        return {"error": "Please enter a question."}

    prompt = f"""
Answer the following cooking question as Lavanya, the AI Cooking Tutor.

Question:
{req.question}

Respond in simple English.
Provide practical cooking guidance.
If the question is related to health or medical advice, politely recommend consulting a qualified healthcare professional.
"""
    return {"response": get_ai_response(prompt)}
