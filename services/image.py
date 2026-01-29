import streamlit as st
import cv2
import numpy as np
from services.gesture import detect_sign
from services.gemini import refine
from services.tts import speak_once

def image_translate():
    st.header("🖼️ Image Translation")

    img = st.file_uploader("Upload Image", type=["jpg", "png"])
    if not img:
        return

    file_bytes = np.asarray(bytearray(img.read()), dtype=np.uint8)
    frame = cv2.imdecode(file_bytes, 1)

    sign = detect_sign(frame)
    refined = refine(sign)

    st.image(frame)
    st.success(refined)
    speak_once(refined)
