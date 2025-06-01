# 🧠 Brain Tumor Classification with Deep Learning

A deep learning-powered web application to detect and classify brain tumors from MRI scans using a custom CNN model. Built with PyTorch and deployed with Streamlit.

[![Live Demo](https://img.shields.io/badge/Live_Demo-Available-green?style=for-the-badge)](https://brainsightai.streamlit.app/)

## 📌 Project Highlights

- 🧠 **4-Class Classification** of brain conditions from MRI:
  - `Glioma Tumor`
  - `Meningioma Tumor`
  - `Pituitary Tumor`
  - `No Tumor Detected`
- 🎯 **High Accuracy**: Custom CNN model achieving ~98% validation accuracy
- 🎛️ **Intuitive Interface**: Streamlit-powered web interface for easy upload and prediction
- ⚡ **Fast Inference**: Optimized for quick predictions (under 1 second)
- 🏥 **Medical Prototype**: Designed as a proof-of-concept for clinical decision support

## 🛠 Tech Stack

### Core Technologies
- `Python 3.9+`
- `PyTorch 2.0`
- `Streamlit 1.25`
- `Torchvision`
- `Pillow (PIL)`

### Model Architecture
```python
# Custom CNN Architecture
Input: 1x64x64 Grayscale MRI
Architecture: Conv2D → ReLU → MaxPool → Dropout → FC → Softmax
Parameters: ~1.2M trainable parameters
```

## 🚀 Deployment

### Cloud Deployment
The application is currently deployed on Streamlit Cloud:
🔗 [Live Demo](https://brainsightai.streamlit.app/)

### Local Installation
```bash
# Clone repository
git clone https://github.com/aymnsk/brain-tumor-classifier.git
cd brain-tumor-classifier

# Install dependencies
pip install -r requirements.txt

# Launch application
streamlit run app.py
```

## 📊 Dataset & Training
- **Source**: Kaggle Brain Tumor Dataset
- **Preprocessing**: Grayscale conversion, normalization, 64x64 resizing
- **Training**: 50 epochs with Adam optimizer
- **Validation Accuracy**: ~98%
- **Model File**: `brain_tumor_model.pth`

## 🌐 Connect With Me

Let's collaborate or chat about AI/ML projects!

[![Instagram](https://img.shields.io/badge/Instagram-@damnn__aymn-E4405F?style=for-the-badge&logo=instagram)](https://www.instagram.com/damnn_aymn/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-aymnsk-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/aymnsk)
[![Twitter/X](https://img.shields.io/badge/Twitter-@Aymn51414199-1DA1F2?style=for-the-badge&logo=x)](https://x.com/Aymn51414199)
[![GitHub](https://img.shields.io/badge/GitHub-aymnsk-181717?style=for-the-badge&logo=github)](https://github.com/aymnsk)

## 📝 Usage Guide
1. Access the web app via the [live demo](https://brainsightai.streamlit.app/) or local installation
2. Upload a brain MRI scan in JPG/PNG format
3. View the model's prediction and confidence scores
4. (Optional) Toggle advanced options for detailed analysis

## 🤝 Contributing
Contributions are welcome! Please open an issue or PR for:
- Model improvements
- UI enhancements
- Additional documentation

## 📜 License
MIT License - See [LICENSE](LICENSE) for details.

---

Created with ❤️ by [Aymn](https://github.com/aymnsk) 
```
