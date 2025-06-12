from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from torchvision import models, transforms
import torch
import torch.nn as nn
from PIL import Image
import io
import json

app = FastAPI()

# Allow frontend access (adjust origins as needed)
app.add_middleware(
    CORSMiddleware,
     allow_origins=["http://localhost:5500"],  # You can restrict this to your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load class names
with open("classes.txt", "r") as f:
    class_names = [line.strip() for line in f.readlines()]

# Load model
num_classes = len(class_names)  # 80 classes
model = models.resnet18(weights=None)  # Don't use pretrained ImageNet weights
model.fc = nn.Linear(model.fc.in_features, num_classes)

# Load trained weights
model.load_state_dict(torch.load("food_classifier.pth", map_location=torch.device("cpu")))
model.eval()

# Define preprocessing steps
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

@app.post("/predict/")
async def predict(file: UploadFile = File(...), quantity: int = Form(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image = transform(image).unsqueeze(0)  # Add batch dimension

    with torch.no_grad():
        outputs = model(image)
        _, predicted = outputs.max(1)
        class_name = class_names[predicted.item()]
        

   

    # STEP 2: Load calorie data from JSON
    with open("food_cal.json", "r") as f:
        calorie_data = json.load(f)

    # STEP 3: Set quantity (either user input or predefined average)
    
    # STEP 4: Calculate calories
    if class_name in calorie_data:
        cal_per_100g = calorie_data[class_name]["calories_per_100g"]
        total_calories = (cal_per_100g / 100) * quantity
    else:
        total_calories = None

    # STEP 5: Return response
    return {
        "predicted_class": class_name,
        "quantity_in_grams": quantity,
        "calories": f"{total_calories:.2f} kcal" if total_calories is not None else "Not available"
    }
    

# Load the calorie database
