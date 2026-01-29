# services/camera.py
import cv2
import streamlit as st
from .gesture import detect_sign   # ✅ RELATIVE IMPORT
from .tts import speak

def live_camera():
    cap = cv2.VideoCapture(0)
    frame_placeholder = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        caption = detect_sign(frame)
        if caption:
            st.success(f"Caption: {caption}")
            speak(caption)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame)

    cap.release()
