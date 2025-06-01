import os
import torch
import torchvision
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader, random_split
import torch.nn as nn
import torch.optim as optim
from torchvision.models import resnet18, ResNet18_Weights

# Dataset path
data_dir = r"C:\Users\Gamil\Desktop\foodsnap-ai\dataset\Indian Food Images\Indian Food Images"  # adjust if needed
model_save_path = "food_classifier.pth"

# 1. Define transforms (resizing + tensor conversion)
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

# 2. Load dataset
dataset = datasets.ImageFolder(data_dir, transform=transform)
class_names = dataset.classes
num_classes = len(class_names)
print(f"Found {num_classes} food classes.")

# 3. Split dataset (80% train, 20% test)
print("Splitting dataset...")
train_size = int(0.8 * len(dataset))
val_size = len(dataset) - train_size
train_dataset, val_dataset = random_split(dataset, [train_size, val_size])

print("Creating DataLoaders...")
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True, num_workers=0)
val_loader = DataLoader(val_dataset, batch_size=32, num_workers=0)
print("DataLoaders ready.")

print("Model loaded and ready to train.")

# 4. Load pre-trained ResNet18 and customize output layer
weights = ResNet18_Weights.DEFAULT
model = resnet18(weights=weights)
model.fc = nn.Linear(model.fc.in_features, num_classes)  # Replace last layer
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

# 5. Loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)


print("Model loaded and ready to train.")

print("Testing one batch from train_loader...")
for images, labels in train_loader:
    print(f"Batch shape: {images.shape}, Labels: {labels[:5]}")
    break


# 6. Training loop
epochs = 5  # Increase if needed
for epoch in range(epochs):
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0

    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        _, predicted = torch.max(outputs, 1)
        correct += (predicted == labels).sum().item()
        total += labels.size(0)

    accuracy = 100 * correct / total
    print(f"Epoch [{epoch+1}/{epochs}], Loss: {running_loss:.4f}, Accuracy: {accuracy:.2f}%")

# 7. Save the trained model
torch.save(model.state_dict(), model_save_path)
print(f"\n✅ Model trained and saved to '{model_save_path}'")
