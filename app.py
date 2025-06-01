import streamlit as st
from predict import predict_image
from model import BrainTumorClassifier
import torch

@st.cache_resource
def load_model():
    model = BrainTumorClassifier()
    model.load_state_dict(torch.load("brain_tumor_model.pth", map_location=torch.device('cpu')))
    model.eval()
    return model

model = load_model()

st.title("Brain Tumor Classification")

uploaded_file = st.file_uploader("Upload MRI Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    temp_image_path = "temp_img.jpg"
    with open(temp_image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    prediction, confidence = predict_image(temp_image_path, model)

    # CHANGE: use_container_width=True instead of deprecated use_column_width
    st.image(temp_image_path, caption="Uploaded Image", use_container_width=True)
    # st.image(..., )

    st.markdown(f"### Prediction: {prediction}")
    st.markdown(f"### Confidence: {confidence * 100:.2f}%")
