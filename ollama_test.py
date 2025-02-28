import requests

def chat_with_ollama(prompt):
    OLLAMA_API_URL = "http://localhost:11434/api/chat"

    payload = {
        "model": "mistral",
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = requests.post(OLLAMA_API_URL, json=payload).json()  # Convert to JSON
        return response["message"]["content"]  # Return final content
    except Exception as e:
        return f"Connection error: {str(e)}"

# Test
print(chat_with_ollama("Summarize this text: Hello world!"))
