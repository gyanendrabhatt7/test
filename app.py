# Import necessary libraries
import streamlit as st
import pytesseract
import cv2
import numpy as np

# Define OCR function
def ocr_core(img):
    """
    This function will handle the core OCR processing of images.
    """
    # Preprocess the image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 3)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Perform OCR using PyTesseract
    text = pytesseract.image_to_string(gray)

    return text

# Define Streamlit app
def app():
    # Set app title
    st.title("OCR with PyTesseract and OpenCV")

    # Create file uploader
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    # Check if file has been uploaded
    if uploaded_file is not None:
        # Convert uploaded file to OpenCV image
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)

        # Perform OCR
        text = ocr_core(img)

        # Display OCR output
        st.write("OCR Output:")
        st.write(text)

# Run app
if __name__ == "__main__":
    app()
