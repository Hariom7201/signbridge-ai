import streamlit as st
from services.image import process_image

st.set_page_config(
    page_title="SignBridge AI",
    layout="centered"
)

st.title("🤝 SignBridge AI")
st.caption("Unified Sign Language Translation Platform")

st.sidebar.header("Choose Input Mode")
mode = st.sidebar.radio(
    "",
    ["Image Upload", "Live Camera (Coming Soon)", "Video Upload (Coming Soon)"]
)

if mode == "Image Upload":
    st.subheader("Upload a sign language image")

    uploaded = st.file_uploader(
        "Choose an image file",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded is not None:
        st.image(uploaded, caption="Uploaded Image", use_container_width=True)

        with st.spinner("Processing image..."):
            caption = process_image(uploaded)

        st.success("Caption Generated Successfully")
        st.markdown(f"### 📝 Output:\n**{caption}**")

elif mode == "Live Camera (Coming Soon)":
    st.info("Live camera will be enabled during the hackathon.")

elif mode == "Video Upload (Coming Soon)":
    st.info("Video processing will be enabled during the hackathon.")
