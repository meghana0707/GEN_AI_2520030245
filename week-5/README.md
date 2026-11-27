
# Week 5 – Token Economics: Cost and Rate-Limit Budgeting

## Aim
To develop a Python-based budgeting tool that estimates LLM token consumption, API costs and rate-limit requirements before implementing an LLM-powered feature.

## Technologies Used
- Python
- Python-dotenv
- Visual Studio Code
- Environment Variables

## Project Structure
```text
Week5/
├── budget.py
├── test_budget.py
├── requirements.txt
└── .env
```

## Implementation
1. Created a Token Economics project.
2. Configured usage assumptions in the `.env` file.
3. Defined input and output token prices.
4. Calculated daily token consumption.
5. Estimated daily and monthly API costs.
6. Checked Requests Per Minute (RPM).
7. Checked Tokens Per Minute (TPM).
8. Applied a safety margin.
9. Generated a budget report.
10. Tested the calculations using unit tests.

## Installation
```bash
pip install -r requirements.txt
```

## Execution
```bash
python budget.py
```

## Testing
```bash
python -m unittest test_budget.py
```

## Important Concepts
- Input Tokens
- Output Tokens
- Total Tokens
- Requests Per Minute (RPM)
- Tokens Per Minute (TPM)
- API Cost Estimation
- Daily and Monthly Budget
- Safety Margin

## Cost Calculation
Daily Cost:

```text
[(Input Tokens × Input Price) +
 (Output Tokens × Output Price)] / 1,000,000
```

Monthly Cost:

```text
Daily Cost × 30
```

## Expected Output
The program generates a Token Economics Report containing:
- Daily input tokens
- Daily output tokens
- Total daily tokens
- Estimated daily cost
- Estimated monthly cost
- Peak RPM
- Peak TPM
- Budget and capacity checks
- Final recommendation

## Learning Outcomes
- Learned token economics.
- Understood API pricing.
- Calculated token consumption.
- Checked RPM and TPM limits.
- Learned budget planning and safety margins.
- Performed automated testing.

## Conclusion
Successfully developed a token budgeting tool to estimate LLM usage, API costs and rate-limit capacity before building an AI feature.
