import streamlit as st
import cv2
from services.gesture import detect_sign
from services.gemini import refine
from services.tts import speak_once

def video_translate():
    st.header("🎥 Video Translation")

    video = st.file_uploader("Upload video", type=["mp4", "avi"])
    if not video:
        return

    tfile = open("temp.mp4", "wb")
    tfile.write(video.read())

    cap = cv2.VideoCapture("temp.mp4")
    stframe = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        sign = detect_sign(frame)
        if sign:
            refined = refine(sign)
            st.caption(refined)
            speak_once(refined)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        stframe.image(frame)
