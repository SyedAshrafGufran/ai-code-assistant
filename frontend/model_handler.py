# model_handler.py

from transformers import pipeline

# Load the code generation pipeline (one-time load)
generator = pipeline("text-generation", model="Salesforce/codegen-350M-mono")  # lightweight and free model

def get_code_completion(prompt: str, task: str) -> str:
    if task not in ["autocomplete", "docstring", "explain", "bugfix", "comment"]:
        return "Unsupported task. Choose from: autocomplete, docstring, explain."

    full_prompt = prompt

    # Modify prompt based on task
    if task == "docstring":
        full_prompt = f'"""Generate a docstring for the following function:\n{prompt}\n"""'
    elif task == "explain":
        full_prompt = f'"""Explain what this code does:\n{prompt}\n"""'
    elif task == "bugfix":
        full_prompt = f'"""Identify and fix bugs in the following code:\n{prompt}\n"""'
    elif task == "comment":
        full_prompt = f'"""Add comments to the following code:\n{prompt}\n"""'
    elif task == "autocomplete":
        full_prompt = f'"""Complete the following code snippet:\n{prompt}\n"""'

    # Generate response
    output = generator(full_prompt, max_new_tokens=100, do_sample=True, temperature=0.7)
    return output[0]['generated_text'].strip()
