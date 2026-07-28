# ChefMate AI API 🍳

## Your AI-Powered Cooking Tutor — FastAPI Backend

A FastAPI backend for ChefMate AI, converted from an original Streamlit application. It teaches beginner cooking concepts through structured explanations, real-life examples, quizzes, and personalized feedback — powered by the Gemini API.

**Live API:** [chefmate-ai-api.onrender.com](https://chefmate-ai-api.onrender.com)
**Interactive docs:** [chefmate-ai-api.onrender.com/docs](https://chefmate-ai-api.onrender.com/docs)

---

## Features

* Step-by-step concept explanations tailored to skill level (Beginner / Intermediate / Advanced)
* Real-life cooking examples for any topic
* Auto-generated 5-question quizzes
* AI-evaluated answer feedback
* Full structured lesson sessions (intro → explanation → quiz → summary)
* Open-ended cooking Q&A, with automatic redirection of health/medical questions to a qualified professional

---

## Tech Stack

* **Framework:** FastAPI
* **Language:** Python
* **AI:** Google Gemini API (`google-genai`)
* **Deployment:** Render

---

## API Endpoints

| Endpoint | Description |
|---|---|
| `GET /` | Health check |
| `POST /explain` | Step-by-step concept explanation |
| `POST /example` | Real-life cooking example |
| `POST /quiz` | Generate a 5-question quiz |
| `POST /evaluate` | Evaluate a student's answer |
| `POST /lesson` | Full structured learning session |
| `POST /ask` | Ask any cooking question |

**Example request** (`/explain`):
```json
{
  "topic": "Dal Tadka",
  "level": "Beginner"
}
```

**Example request** (`/evaluate`):
```json
{
  "topic": "Dal Tadka",
  "student_answer": "You add hot spices to unlock flavor before pouring over the lentils."
}
```

**Example request** (`/ask`):
```json
{
  "question": "How do I know when rice is fully cooked?"
}
```

---

## Local Setup

### Clone the repository
```bash
git clone https://github.com/Lavanya3112/chefmate-ai-api.git
cd chefmate-ai-api
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Set up environment variable
Create a `.env` file:
```
GOOGLE_API_KEY=your_actual_gemini_api_key_here
```

### Run the application
```bash
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000/docs` for the interactive API documentation.

---

## Origin

This API is the backend conversion of the original ChefMate AI Streamlit capstone project (Infosys Springboard AI EMPOW(H)ER Program), rebuilt to support future client integrations, including a planned mobile app.

---

## Author

**Lavanya Ajit Dive**
* B.Sc. Data Science Student
* Data Analyst | AI & GenAI Enthusiast | Prompt Engineering
* [LinkedIn](https://linkedin.com/in/lavanyadive) · [GitHub](https://github.com/Lavanya3112)
