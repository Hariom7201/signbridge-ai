import streamlit as st
from PIL import Image
from services.gesture import detect_sign
from services.tts import speak_once

def image_ui():
    st.subheader("Image Translation")

    uploaded = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

    if uploaded:
        img = Image.open(uploaded)
        st.image(img, caption="Uploaded Image")

        caption = detect_sign(None)
        st.success(f"Caption: {caption}")

        if st.button("Speak Caption"):
            speak_once(caption)
