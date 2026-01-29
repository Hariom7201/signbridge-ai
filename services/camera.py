import streamlit as st
import cv2
from services.gesture import detect_sign
from services.tts import speak_once

def camera_ui():
    st.subheader("Live Camera Translation")

    camera_on = st.checkbox("Start Camera")

    frame_placeholder = st.empty()
    caption_placeholder = st.empty()

    if camera_on:
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            st.error("Camera not accessible")
            return

        while camera_on:
            ret, frame = cap.read()
            if not ret:
                break

            caption = detect_sign(frame)

            frame_placeholder.image(frame, channels="BGR")
            caption_placeholder.success(f"Caption: {caption}")

            speak_once(caption)

            if not st.session_state.get("camera_active", True):
                break

        cap.release()
