import streamlit as st
import cv2
from services.gesture import detect_sign
from services.gemini import refine
from services.tts import speak_once

def live_camera():
    st.header("📷 Live Camera Mode")

    frame_placeholder = st.empty()
    cap = cv2.VideoCapture(0)

    last_spoken = ""

    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Camera not accessible")
            break

        sign = detect_sign(frame)

        if sign:
            refined = refine(sign)
            st.success(refined)

            if refined != last_spoken:
                speak_once(refined)
                last_spoken = refined

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame)
