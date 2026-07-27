import json
import re

# 1. Simple prompt loader
def load_prompt(template_path: str) -> str:
    """Loads a prompt template from a given file path."""
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "Error: Prompt template not found."

# 2. Runtime variable/context injection example
def inject_context(template: str, context_vars: dict) -> str:
    """Injects runtime variables into a prompt template."""
    prompt = template
    for key, value in context_vars.items():
        placeholder = f"{{{{{key}}}}}" # e.g., {{user_name}}
        prompt = prompt.replace(placeholder, str(value))
    return prompt

# 3. Prompt registry lookup example
class PromptRegistry:
    def __init__(self):
        self._registry = {
            "educational_qna": "You are a helpful tutor. Answer the student's question: {{question}}",
            "summary": "Summarize the following text: {{text}}"
        }

    def get_prompt(self, prompt_id: str) -> str:
        """Looks up a prompt template by its ID."""
        return self._registry.get(prompt_id, "Error: Prompt ID not found.")

# 4. JSON output validation example
def validate_json_output(llm_output: str) -> dict:
    """Validates if the LLM output is a valid JSON object."""
    try:
        # Strip potential markdown code blocks
        clean_output = llm_output.strip().strip('```json').strip('```').strip()
        parsed_data = json.loads(clean_output)
        return {"valid": True, "data": parsed_data}
    except json.JSONDecodeError as e:
        return {"valid": False, "error": str(e)}

# 5. Citation validation example
def validate_citations(text: str, source_texts: list) -> bool:
    """Checks if citations [1], [2] in text actually correspond to provided sources."""
    citations_found = set(re.findall(r'\[(\d+)\]', text))
    for citation in citations_found:
        idx = int(citation) - 1
        if idx < 0 or idx >= len(source_texts):
            return False # Invalid citation index
    return True

# 6. Small prompt-security/injection detection example
def detect_prompt_injection(user_input: str) -> bool:
    """Basic detection of common prompt injection patterns."""
    suspicious_patterns = [
        "ignore previous instructions",
        "system prompt",
        "you are now",
        "forget everything",
        "bypass",
    ]
    user_input_lower = user_input.lower()
    for pattern in suspicious_patterns:
        if pattern in user_input_lower:
            return True # Potential injection detected
    return False

if __name__ == "__main__":
    print("Prompt Engineering Utilities Loaded Successfully.")
