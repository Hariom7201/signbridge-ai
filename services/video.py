# services/video.py
import cv2
import streamlit as st
from .gesture import detect_sign
from . acknowledged import speak

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        caption = detect_sign(frame)
        if caption:
            st.info(f"Caption: {caption}")
            speak(caption)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        st.image(frame)

    cap.release()
