import torch
import torchvision.transforms as transforms
from PIL import Image
from model import BrainTumorClassifier

CLASS_NAMES = ['glioma', 'meningioma', 'notumor', 'pituitary']

transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),  # match training
    transforms.Resize((64, 64)),
    transforms.ToTensor(),
])

def load_model(path='brain_tumor_model.pth', device='cpu'):
    model = BrainTumorClassifier()
    model.load_state_dict(torch.load(path, map_location=device))
    model.eval()
    return model

def predict_image(img_path, model, device='cpu'):
    image = Image.open(img_path).convert('L')  # convert to grayscale
    img = transform(image).unsqueeze(0).to(device)
    with torch.no_grad():
        output = model(img)
        _, predicted = torch.max(output, 1)
        confidence = torch.nn.functional.softmax(output, dim=1)[0][predicted.item()].item()
    return CLASS_NAMES[predicted.item()], confidence
