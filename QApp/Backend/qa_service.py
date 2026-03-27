# QApp/Backend/qa_service.py
import os
import requests
 
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://ollama:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen3:1.7b")
 
SYSTEM_PROMPT = """
You are a helpful teaching assistant for data science students.
Answer clearly and briefly.
When the question is about Docker, use simple explanations and examples.
"""
 
def answer_question(question: str) -> str:
    question = question.strip()
    if not question:
        return "Please type a question."
 
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": question,
        "system": SYSTEM_PROMPT,
        "stream": False,
        "think": False
    }
 
    try:
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json=payload,
            timeout=120
        )
        response.raise_for_status()
        data = response.json()
        return data.get("response", "No response returned from the model.")
    except requests.exceptions.RequestException as e:
        return f"Could not reach the local LLM service: {e}"

