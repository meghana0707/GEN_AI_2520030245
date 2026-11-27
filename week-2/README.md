
# Week 2 – Provider-Agnostic LLM Client

## Aim
To build a provider-agnostic LLM client that supports both a hosted Gemini API and a locally running Ollama model through a common interface.

## Technologies Used
- Python
- Gemini API
- Ollama
- Llama 3.2
- Requests
- Python-dotenv
- Pytest

## Project Structure
```text
Week2/
├── main.py
├── llm_client.py
├── test_client.py
├── requirements.txt
└── .env
```

## Implementation
1. Installed Ollama on the local system.
2. Downloaded the Llama 3.2 model.
3. Created a common LLMProvider interface.
4. Implemented GeminiProvider for cloud-based responses.
5. Implemented OllamaProvider for local responses.
6. Created an LLMClient to handle both providers.
7. Added testing using a fake provider.

## Installation
```bash
ollama pull llama3.2
pip install -r requirements.txt
```

## Execution
```bash
python main.py
```

Select the provider:
```text
Choose provider (gemini/ollama):
Enter your question:
```

## Testing
```bash
python -m unittest test_client.py
```

## Expected Output
The selected provider generates an AI response based on the user's question.

## Learning Outcomes
- Understood provider-agnostic architecture.
- Learned cloud and local LLM integration.
- Worked with abstract classes and interfaces.
- Learned basic unit testing.

## Conclusion
Successfully developed a common LLM client supporting Gemini and Ollama using Python.
