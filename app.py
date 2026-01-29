import streamlit as st
from services.camera import live_camera
from services.video import video_translate
from services.image import image_translate

st.set_page_config(page_title="SignBridge AI", layout="wide")

st.title("🤝 SignBridge AI")
st.subheader("Unified Sign Language Translation Platform")

mode = st.sidebar.radio(
    "Choose Input Mode",
    ["Live Camera", "Video Upload", "Image Upload"]
)

if mode == "Live Camera":
    live_camera()

elif mode == "Video Upload":
    video_translate()

elif mode == "Image Upload":
    image_translate()
