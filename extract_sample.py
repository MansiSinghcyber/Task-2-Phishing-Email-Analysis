from datasets import load_dataset

dataset = load_dataset("Teddyha/phishing_benign_email_dataset")

sample = dataset["train"][0]

with open("phishing_sample.txt", "w") as f:
    f.write(f"From: {sample['spoofed_sender']}\n")
    f.write(f"Subject: {sample['subject']}\n\n")
    f.write(sample["body"])

print("Sample saved as phishing_sample.txt")
