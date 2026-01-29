import streamlit as st
import tempfile
import cv2
from services.gesture import detect_sign
from services.tts import speak_once

def video_ui():
    st.subheader("Video Translation")

    uploaded = st.file_uploader("Upload Video", type=["mp4", "avi", "mov"])

    if uploaded:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded.read())

        cap = cv2.VideoCapture(tfile.name)

        frame_box = st.empty()
        caption_box = st.empty()

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            caption = detect_sign(frame)

            frame_box.image(frame, channels="BGR")
            caption_box.info(f"Caption: {caption}")

        cap.release()

        if st.button("Speak Last Caption"):
            speak_once(caption)
