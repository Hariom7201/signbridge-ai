import streamlit as st
from services.camera import live_camera
from services.video import process_video
from services.image import process_image

st.set_page_config(page_title="SignBridge AI", layout="wide")

st.title("🤝 SignBridge AI")
st.caption("Unified Sign Language Translation Platform")

mode = st.radio(
    "Choose Input Mode",
    ["Live Camera", "Upload Video", "Upload Image"]
)

if mode == "Live Camera":
    if st.button("Start Camera"):
        live_camera()

elif mode == "Upload Video":
    video = st.file_uploader("Upload Video", type=["mp4", "avi"])
    if video:
        with open("temp.mp4", "wb") as f:
            f.write(video.read())
        process_video("temp.mp4")

elif mode == "Upload Image":
    img = st.file_uploader("Upload Image", type=["jpg", "png"])
    if img:
        import numpy as np
        file_bytes = np.asarray(bytearray(img.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        process_image(image)
