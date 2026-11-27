
# Week 6 – Golden Question Set and Baseline Evaluation

## Aim
To create a golden question set containing questions, expected answers, keywords and reference sources, and evaluate an LLM's responses using a baseline evaluation.

## Technologies Used
- Python
- Ollama
- Llama 3.2
- JSON
- Requests
- CSV
- Visual Studio Code

## Project Structure
```text
Week6/
├── main.py
├── golden_set.json
└── requirements.txt
```

## Implementation
1. Installed and configured Ollama.
2. Downloaded the Llama 3.2 model.
3. Created a golden question set in JSON format.
4. Added questions, expected answers, keywords and source links.
5. Loaded the questions from the JSON file.
6. Sent each question to the local LLM.
7. Collected the generated responses.
8. Evaluated responses using keyword coverage.
9. Classified the results as PASS, REVIEW or ERROR.
10. Generated a baseline evaluation summary.
11. Exported evaluation results into a CSV file.

## Golden Question Set
The `golden_set.json` file contains 30 questions covering topics such as:
- Tokenization
- BPE and WordPiece
- SentencePiece
- Input and Output Tokens
- Token Economics
- Context Windows
- Rate Limits
- Autoregressive Generation
- Greedy Decoding and Sampling
- Embeddings
- Positional Encoding
- Transformers

Each question contains:
- Question ID
- Question
- Expected Answer
- Keywords
- Source URL

## Installation
```bash
pip install -r requirements.txt
```

## Ollama Setup
```bash
ollama pull llama3.2
```

## Execution
```bash
python main.py
```

## Expected Output
The program generates a baseline evaluation summary containing:
- Release Version: v0.1
- Model Name
- Total Questions
- Successful Responses
- Passed Questions
- Questions for Review
- Failed Requests
- Average Keyword Coverage
- Evaluation Date

## Output File
The program automatically generates:

```text
baseline_results.csv
```

This file stores the question evaluation results.

## Learning Outcomes
- Learned golden dataset creation.
- Understood baseline evaluation.
- Worked with JSON and CSV files.
- Learned keyword-based evaluation.
- Evaluated LLM-generated answers.
- Understood model performance measurement.

## Conclusion
Successfully created a golden question set and performed the first baseline evaluation using the Llama 3.2 model. Generated evaluation results in CSV format and created release v0.1.
