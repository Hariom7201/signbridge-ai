import streamlit as st
import cv2
import numpy as np
from gesture_recognition import detect_hand, classify_sign
from gemini_refiner import refine_sentence
from tts import speak

st.set_page_config(page_title="SignBridge AI", layout="centered")

st.title("🤝 SignBridge AI")
st.write("Real-Time Sign Language Translation System")

# Camera input (STREAMLIT SAFE)
image = st.camera_input("Start Camera")

if image is not None:
    # Convert image to OpenCV format
    bytes_data = image.getvalue()
    np_img = np.frombuffer(bytes_data, np.uint8)
    frame = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    hand = detect_hand(frame)

    if hand:
        raw = classify_sign(hand)
        refined = refine_sentence(raw)
        st.session_state["text"] = refined
        st.success(f"Detected: {refined}")
    else:
        st.warning("No hand detected")

# Speak button
if st.button("🔊 Speak"):
    if "text" in st.session_state:
        speak(st.session_state["text"])
