
# Week 4 – Tokenizer Lab

## Aim
To implement and compare three subword tokenization approaches: Byte Pair Encoding (BPE), WordPiece and SentencePiece using English, Telugu and Hindi text.

## Technologies Used
- Python
- Hugging Face Transformers
- SentencePiece
- Visual Studio Code

## Tokenizers Used

| Tokenizer | Model |
|---|---|
| BPE | GPT-2 |
| WordPiece | Multilingual BERT |
| SentencePiece | XLM-RoBERTa |

## Project Structure
```text
Week4/
├── tokenizer_comparison.py
└── requirements.txt
```

## Implementation
1. Installed the required libraries.
2. Imported AutoTokenizer from Transformers.
3. Loaded the GPT-2 tokenizer.
4. Loaded the Multilingual BERT tokenizer.
5. Loaded the XLM-RoBERTa tokenizer.
6. Provided English, Telugu and Hindi input sentences.
7. Generated tokens and token IDs.
8. Compared token counts for all three languages.

## Installation
```bash
pip install -r requirements.txt
```

## Requirements
```text
transformers
sentencepiece
```

## Execution
```bash
python tokenizer_comparison.py
```

## Expected Output
The program displays:
- Input language
- Input text
- Token pieces
- Token IDs
- Total token count

Results are displayed separately for BPE, WordPiece and SentencePiece.

## Learning Outcomes
- Understood tokenization in LLMs.
- Learned BPE, WordPiece and SentencePiece.
- Compared tokenizers across multiple languages.
- Understood token IDs and token counts.
- Observed differences in multilingual tokenization.

## Conclusion
Successfully compared three pretrained tokenizers using English, Telugu and Hindi text and observed their tokenization differences.
