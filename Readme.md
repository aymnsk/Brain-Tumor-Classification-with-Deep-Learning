# 🧠 Brain Tumor Classification with Deep Learning

A deep learning-powered web app to detect brain tumors from MRI scans using a custom CNN model. Built with PyTorch and deployed using Streamlit.

![Demo](https://user-images.githubusercontent.com/your-demo-gif.gif) <!-- Optional: Replace with a gif/screenshot -->

---

## 📌 Project Highlights

- 🧠 Detects **4 types** of brain conditions from MRI:
  - `Glioma`
  - `Meningioma`
  - `No Tumor`
  - `Pituitary`
- 🧪 Trained using a custom CNN built in PyTorch.
- 🎛️ User-friendly interface built with Streamlit.
- 📦 Lightweight & fast, ideal for medical prototype use-cases.

---

## 🚀 Live Demos

| Platform          | Link                                   |
|------------------|----------------------------------------|
| 🌐 Streamlit Cloud | [Launch App](https://your-streamlit-link) |
| 🤗 Hugging Face    | [Try on Spaces](https://huggingface.co/spaces/your-app) |

---

## 🛠 Tech Stack

- `Python`
- `PyTorch`
- `Streamlit`
- `Torchvision`
- `PIL (Pillow)`
- `CNN (Custom architecture)`

---

## 📸 Sample Predictions

| MRI Image | Prediction | Confidence |
|-----------|------------|------------|
| ![img](examples/glioma.jpg) | `Glioma` | `98.5%` |
| ![img](examples/pituitary.jpg) | `Pituitary` | `97.2%` |

---

## 🧪 How to Run Locally

```bash
git clone https://github.com/aymnsk/brain-tumor-classifier.git
cd brain-tumor-classifier
pip install -r requirements.txt
streamlit run app.py
🧠 Model Info
python
Copy
Edit
# Model: CNN
Input: 1x64x64 Grayscale MRI
Conv2D → ReLU → MaxPool → FC → Softmax
Accuracy: ~98% on validation
Model file: brain_tumor_model.pth
Trained on: Kaggle Brain Tumor Dataset

🔗 Connect with Me
💼 LinkedIn

🐦 Twitter / X

📸 Instagram

💻 GitHub

💡 Credits
Created with ❤️ by @aymnsk
Under mentorship and guidance of the open-source & research community.

📃 License
This project is licensed under the MIT License.
