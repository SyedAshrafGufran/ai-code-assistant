# ollama_client.py
import requests

def query_ollama(prompt: str, model: str = "phi3") -> str:
    """
    Sends a prompt to the local Ollama server and returns the model's response.
    """
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": model, "prompt": prompt, "stream": False},
            timeout=300
        )
        response.raise_for_status()
        return response.json().get("response", "No response from model.")
    except requests.exceptions.RequestException as e:
        return f"Error querying Ollama: {str(e)}"