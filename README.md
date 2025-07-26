# 🤖 AI Code Assistant

**AI Code Assistant** is an end-to-end code generation and explanation tool powered by LLMs. It helps developers by autocompleting code, fixing bugs, writing docstrings, and explaining code snippets — all through a friendly frontend and a robust backend using modern ML tooling.

---

## 🚀 Features

- 🔄 **Autocomplete Code Snippets**
- 🧠 **Generate Docstrings**
- 🛠️ **Fix Bugs in Code**
- 💬 **Explain Code in Plain English**
- 💻 **Interactive Streamlit Frontend**
- ⚙️ **FastAPI Backend with Ollama LLM Support**

---

## 🧰 Tech Stack

| Component | Technology |
|----------|------------|
| **Frontend** | Streamlit |
| **Backend** | FastAPI |
| **Model Inference** |  Ollama |
| **LLMs Tested** | GPT-2, CodeLlama, StarCoder (small variants) |
| **Prompt Management** | Custom Templates |
| **Python Version** | 3.10+ |
| **Deployment** | Localhost (Free!) |

---

## 📁 Project Structure

<pre> ``` 
├── backend/
│ ├── main.py # FastAPI app and route handlers
│ ├── ollama_client.py # Sends prompts to Ollama model
│ └──  prompt_templates.py # Task-specific prompt builders
├── frontend/
│ ├── app.py # Streamlit UI for user interaction
│ └── model_handler.py # Helper to dispatch tasks + route prompts
├── requirements.txt # Python dependencies
└── README.md # Project documentation


 ``` </pre>

---

## 🛠️ Setup & Run Locally

1. **Clone the repo**  
   ```bash
   git clone https://github.com/SyedAshrafGufran/ai-code-assistant.git
   cd ai-code-assistant

2. Set up virtual environment
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows


3. Install requirements
   ```bash
   pip install -r requirements.txt

4. Start Ollama server (in another terminal)
   ```bash
   ollama run <your-model-name>   # e.g., ollama run codellama


5. Run FastAPI backend
   ```bash
   uvicorn backend.main:app --reload


6. Run Streamlit frontend
   ```bash
   streamlit run frontend/app.py


## 📌 Notes

- Works best with lighter LLMs (like **GPT-2** or **CodeLlama 7B**).
- Requires **~4GB+ RAM** minimum if running locally.
- Can be integrated with hosted APIs like **Hugging Face Inference API** if desired.

---

## 🧑‍💻 Author

**Syed Ashraf Gufran**  
_Machine Learning & AI Enthusiast_
[LinkedIn](https://www.linkedin.com/in/syed-ashraf-gufran) | [GitHub](https://github.com/SyedAshrafGufran)