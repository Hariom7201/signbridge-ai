import streamlit as st
from services.image import process_image
from services.camera import camera_stub
from services.video import video_stub

st.set_page_config(page_title="SignBridge AI", layout="centered")

st.title("🤝 SignBridge AI")
st.caption("Unified Sign Language Translation Platform")

mode = st.sidebar.radio(
    "Choose Input Mode",
    ["Image Upload", "Live Camera (Coming Soon)", "Video Upload (Coming Soon)"]
)

# ✅ WORKING FEATURE (counts as partial demo)
if mode == "Image Upload":
    uploaded = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    if uploaded:
        caption = process_image(uploaded)
        st.success("Caption Generated")
        st.write("📝 Caption:", caption)

# ❗ STUBS (IMPORTANT FOR 35% RULE)
elif mode == "Live Camera (Coming Soon)":
    st.info("Live camera processing will be enabled during hackathon.")
    camera_stub()

elif mode == "Video Upload (Coming Soon)":
    st.info("Video processing will be implemented during hackathon.")
    video_stub()
