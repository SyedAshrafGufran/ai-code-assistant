import streamlit as st
import requests

st.set_page_config(page_title="AI Code Assistant 💻", layout="wide")

st.title("AI Code Assistant 🤖")
st.markdown("Get code autocompletions, docstrings, or explanations using a language model.")

# Sidebar selection
task = st.sidebar.selectbox(
    "Choose Task",
    ["autocomplete", "docstring", "explain", "bugfix", "add_comments"]
)

code_input = st.text_area("✍️ Paste your code here", height=300)

if st.button("⚡ Generate"):
    if not code_input.strip():
        st.warning("Please enter some code.")
    else:
        with st.spinner("Generating response..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/autocomplete/" if task == "autocomplete" else
                    "http://127.0.0.1:8000/generate_docstring/" if task == "docstring" else
                    "http://127.0.0.1:8000/explain_code/" if task == "explain" else
                    "http://127.0.0.1:8000/fix_bug/" if task == "bugfix" else
                    "http://127.0.0.1:8000/add_comments/",
                    json={"prompt": code_input, "task": task}
                )
                result = response.json()

                # Map task to response key
                key_map = {
                    "autocomplete": "suggestion",
                    "docstring": "docstring",
                    "explain": "explanation",
                    "bugfix": "fixed_code",
                    "add_comments": "commented_code"
                }

                output_key = key_map.get(task)
                if output_key in result:
                    st.subheader("📦 Output")
                    st.code(result[output_key], language="python")
                else:
                    st.error(result.get("detail", "Something went wrong."))

            except Exception as e:
                st.error(f"Error: {e}")
