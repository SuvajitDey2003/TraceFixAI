from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.rag import retrieve_similar_errors
from app.prompts import build_prompt
from groq import Groq
import os

app = FastAPI()

# Load Groq API key
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise RuntimeError("GROQ_API_KEY not found in environment variables")

client = Groq(api_key=api_key)

class ErrorRequest(BaseModel):
    error_log: str

@app.post("/analyze")
def analyze_error(request: ErrorRequest):
    try:
        context = retrieve_similar_errors(request.error_log)
        prompt = build_prompt(request.error_log, context)

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a senior software engineer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )

        return {
            "analysis": response.choices[0].message.content,
            "context_used": context
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
