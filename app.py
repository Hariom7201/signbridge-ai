import streamlit as st

from services.camera import camera_ui
from services.image import image_ui
from services.video import video_ui

st.set_page_config(page_title="SignBridge AI", layout="centered")

st.title("🤝 SignBridge AI")
st.caption("Unified Sign Language Translation Platform")

tab1, tab2, tab3 = st.tabs(["📷 Camera", "🖼️ Image", "🎥 Video"])

with tab1:
    camera_ui()

with tab2:
    image_ui()

with tab3:
    video_ui()
