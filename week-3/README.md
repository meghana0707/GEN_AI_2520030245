
# Week 3 – LLM Monitoring with MongoDB

## Aim
To extend the provider-agnostic LLM client by monitoring token usage, response latency and estimated API cost, and storing usage details in MongoDB.

## Technologies Used
- Python
- Gemini API
- Ollama
- MongoDB Atlas
- PyMongo
- Requests
- Python-dotenv

## Project Structure
```text
Week3/
├── main.py
├── llm_client.py
├── usage_logger.py
├── test_client.py
├── requirements.txt
└── .env
```

## Implementation
1. Configured Gemini API credentials.
2. Created a MongoDB Atlas database.
3. Connected Python with MongoDB.
4. Implemented a usage logger.
5. Captured input and output token counts.
6. Measured response latency.
7. Calculated estimated API cost.
8. Implemented request timeouts and retry handling.
9. Stored successful and failed request details in MongoDB.

## Installation
```bash
pip install -r requirements.txt
```

## Ollama Setup
```bash
ollama pull llama3.2
ollama run llama3.2
```

## Execution
```bash
python -m unittest test_client.py
python main.py
```

Select a provider:
```text
Choose provider (gemini/ollama):
Enter your question:
```

## Monitoring Details
The application tracks:
- Provider and model name
- Input tokens
- Output tokens
- Total tokens
- Response latency
- Estimated API cost
- Request status
- Number of attempts

## MongoDB Database
Database: `llm_monitoring`

Collection: `api_usage`

## Learning Outcomes
- Learned MongoDB integration.
- Understood token usage monitoring.
- Learned response time measurement.
- Implemented cost estimation.
- Understood timeout and retry mechanisms.

## Conclusion
Successfully implemented LLM monitoring using MongoDB with token tracking, latency measurement, cost estimation and error handling.
