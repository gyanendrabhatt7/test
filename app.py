import streamlit as st
from PIL import Image
import io
import requests
import cv2
import pytesseract
import numpy as np
import time
import doctr

# Set up OCR model
doctr_models = ["us-federalist", "us-constitution", "india-constitution", "uk-constitution"]
model_choice = st.sidebar.selectbox("Choose an OCR model", options=doctr_models)
model = doctr.models.OCR.create(model_choice)

# Define Streamlit app layout
st.title("OCR with Doctr")
st.header("Upload an image for OCR")

# Allow user to upload image file
file = st.file_uploader("Upload an image file", type=["jpg", "jpeg", "png"])

# If an image file has been uploaded, perform OCR and display results
if file is not None:
    # Load image file
    img = Image.open(file)
    
    # Display image
    st.image(img, caption="Uploaded image", use_column_width=True)
    
    # Perform OCR on image using Doctr
    with st.spinner("Performing OCR..."):
        results = model.predict(img)
        text = "\n".join([result.text for result in results])
    
    # Display OCR results
    st.subheader("OCR Results")
    st.text(text)
