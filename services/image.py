# services/image.py
import cv2
import streamlit as st
from .gesture import detect_sign

def process_image(image):
    frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    caption = detect_sign(frame)

    if caption:
        st.success(f"Detected Sign: {caption}")

    st.image(frame)
