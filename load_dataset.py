from datasets import load_dataset

dataset = load_dataset("Teddyha/phishing_benign_email_dataset")

print(dataset)

print("\nFirst phishing sample:\n")
print(dataset["train"][0])
