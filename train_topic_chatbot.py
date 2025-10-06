import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from torch.utils.data import Dataset, DataLoader

# 1. Load model
model_name = "microsoft/DialoGPT-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# 2. Custom dataset
class ChatDataset(Dataset):
    def __init__(self, file_path, tokenizer, max_length=128):
        self.examples = []
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.read().split("\n\n")
        for line in lines:
            if line.strip():
                self.examples.append(line.strip())
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.examples)

    def __getitem__(self, idx):
        encodings = self.tokenizer(
            self.examples[idx],
            truncation=True,
            max_length=self.max_length,
            padding="max_length",
            return_tensors="pt"
        )
        input_ids = encodings["input_ids"].squeeze()
        attention_mask = encodings["attention_mask"].squeeze()
        labels = input_ids.clone()
        return {"input_ids": input_ids, "attention_mask": attention_mask, "labels": labels}

dataset = ChatDataset("topic_dataset.txt", tokenizer)
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

# 3. Optimizer
optimizer = torch.optim.AdamW(model.parameters(), lr=5e-5)

# 4. Training loop (small epochs for CPU)
epochs = 3
model.train()
for epoch in range(epochs):
    print(f"Epoch {epoch+1}/{epochs}")
    for batch in dataloader:
        input_ids = batch["input_ids"].to(device)
        attention_mask = batch["attention_mask"].to(device)
        labels = batch["labels"].to(device)

        outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print(f"Loss: {loss.item()}")

# 5. Save model
model.save_pretrained("./topic_model_cpu")
tokenizer.save_pretrained("./topic_model_cpu")
print("✅ Training complete!")
