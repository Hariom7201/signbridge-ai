import os
import streamlit as st

IS_CLOUD = os.getenv("STREAMLIT_SERVER_RUNNING") == "true"

mode = st.sidebar.radio(
    "Choose Input Mode",
    ["Live Camera", "Video Upload", "Image Upload"]
)

if mode == "Live Camera":
    if IS_CLOUD:
        st.error("Live Camera works only on local machine.")
    else:
        from services.camera import live_camera
        live_camera()
