def generate_autocomplete_prompt(code_snippet: str) -> str:
    return f"""
You are a coding assistant. Given the following incomplete code snippet, complete it accurately and concisely:

{code_snippet}

Completed Code:
"""

def generate_docstring_prompt(function_code: str) -> str:
    return f"""
You are a coding assistant. Generate a concise and clear Python docstring for the following function:

{function_code}

Docstring:
"""

def generate_bugfix_prompt(code_with_bug: str) -> str:
    return f"""
You are a Python expert. Find and fix the bugs in the following code:

{code_with_bug}

Corrected Code:
"""

def generate_explanation_prompt(code_snippet: str) -> str:
    return f"""
You are an AI assistant that explains Python code in simple terms:

{code_snippet}

Explanation:
"""

def generate_comment_prompt(code_snippet: str) -> str:
    return f"""
You are an AI coding assistant. Add meaningful inline comments to the following Python code:

{code_snippet}

Code with comments:
"""
