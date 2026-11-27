
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load a small GPT-2 model
model_name = "openai-community/gpt2"

print("Loading model...")

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Input prompt
prompt = input("Enter your prompt: ")

# Convert text into tokens
inputs = tokenizer(prompt, return_tensors="pt")

# Get model predictions
with torch.no_grad():
    outputs = model(**inputs)

# Get logits of the last token position
logits = outputs.logits[0, -1, :]

# Convert logits into probabilities
probabilities = torch.softmax(logits, dim=-1)

# Get top 5 predictions
top_k = torch.topk(probabilities, 5)

print("\nTop 5 Next Token Predictions:")
print("--------------------------------")

for i in range(5):
    token_id = top_k.indices[i].item()
    probability = top_k.values[i].item()

    token = tokenizer.decode([token_id])

    print(f"Token: {repr(token)}")
    print(f"Probability: {probability:.6f}")
    print("--------------------------------")
