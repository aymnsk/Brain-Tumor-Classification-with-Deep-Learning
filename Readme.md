Here's the cleaned-up version of your README without live predictions and demos:

```markdown
# 🧠 Brain Tumor Classification with Deep Learning

A deep learning-powered web app to detect brain tumors from MRI scans using a custom CNN model. Built with PyTorch and deployed using Streamlit.

---

## 📌 Project Highlights

- 🧠 Detects **4 types** of brain conditions from MRI:
  - `Glioma`
  - `Meningioma`
  - `No Tumor`
  - `Pituitary`
- 🧪 Trained using a custom CNN built in PyTorch
- 🎛️ User-friendly interface built with Streamlit
- 📦 Lightweight & fast, ideal for medical prototype use-cases

---

## 🛠 Tech Stack

- `Python`
- `PyTorch`
- `Streamlit`
- `Torchvision`
- `PIL (Pillow)`
- `CNN (Custom architecture)`

---

## 🧪 How to Run Locally

```bash
git clone https://github.com/aymnsk/brain-tumor-classifier.git
cd brain-tumor-classifier
pip install -r requirements.txt
streamlit run app.py
```

---

## 🧠 Model Info

```python
# Model: CNN
Input: 1x64x64 Grayscale MRI
Conv2D → ReLU → MaxPool → FC → Softmax
Accuracy: ~98% on validation
Model file: brain_tumor_model.pth
Trained on: Kaggle Brain Tumor Dataset
```

---

## 🔗 Connect with Me
💼 LinkedIn  
🐦 Twitter / X  
📸 Instagram  
💻 GitHub  

---

## 💡 Credits
Created with ❤️ by @aymnsk  
Under mentorship and guidance of the open-source & research community.

---

## 📃 License
This project is licensed under the MIT License.
```
