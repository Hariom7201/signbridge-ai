import streamlit as st
import cv2
import tempfile
import time

from gesture_recognition import detect_hand, classify_sign
from gemini_refiner import refine_sentence
from tts import speak

st.set_page_config(page_title="SignBridge AI – Video Mode", layout="centered")

st.title("🎥 SignBridge AI – Video Translation")
st.write("Upload a sign language video to get live captions and voice translation.")

uploaded_video = st.file_uploader(
    "Upload a video (MP4 / AVI)",
    type=["mp4", "avi", "mov"]
)

frame_window = st.image([])
caption_box = st.empty()

if uploaded_video is not None:
    # Save uploaded video temporarily
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(uploaded_video.read())

    cap = cv2.VideoCapture(temp_file.name)

    last_spoken = ""
    fps = cap.get(cv2.CAP_PROP_FPS)
    delay = 1 / fps if fps > 0 else 0.04

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        hand = detect_hand(frame)

        if hand:
            raw = classify_sign(hand)
            refined = refine_sentence(raw)

            if refined:
                caption_box.markdown(
                    f"### 📝 Caption: **{refined}**"
                )

                if refined and refined != last_spoken:
                   speak(refined)
                last_spoken = refined

        frame_window.image(
            cv2.cvtColor(frame, cv2.COLOR_BGR2RGB),
            channels="RGB"
        )

        time.sleep(delay)

    cap.release()
    st.success("✅ Video processing completed")
