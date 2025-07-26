# backend/main.py
from fastapi import FastAPI, Body
from pydantic import BaseModel
from backend.ollama_client import query_ollama
from backend.prompt_templates import (
    generate_autocomplete_prompt,
    generate_docstring_prompt,
    generate_bugfix_prompt,
    generate_explanation_prompt,
    generate_comment_prompt,
)


app = FastAPI()
class PromptRequest(BaseModel):
    prompt: str
    task: str

@app.get("/")
def root():
    return {"message": "Welcome to the AI Code Assistant! 💻🤖"}

@app.post("/autocomplete/")
def autocomplete(request: PromptRequest):
    prompt = generate_autocomplete_prompt(request.prompt)
    response = query_ollama(prompt)
    return {"suggestion": response}

@app.post("/complete_function/")
def complete_function(request: PromptRequest):
    prompt = generate_autocomplete_prompt(request.prompt)
    response = query_ollama(prompt)
    return {"completion": response}

@app.post("/generate_docstring/")
def generate_docstring(request: PromptRequest):
    prompt = generate_docstring_prompt(request.prompt)
    response = query_ollama(prompt)
    return {"docstring": response}

@app.post("/fix_bug/")
def fix_bug(request: PromptRequest):
    prompt = generate_bugfix_prompt(request.prompt)
    response = query_ollama(prompt)
    return {"fixed_code": response}

@app.post("/explain_code/")
def explain_code(request: PromptRequest):
    prompt = generate_explanation_prompt(request.prompt)
    response = query_ollama(prompt)
    return {"explanation": response}

@app.post("/add_comments/")
def add_comments(request: PromptRequest):
    prompt = generate_comment_prompt(request.prompt)
    response = query_ollama(prompt)
    return {"commented_code": response}
