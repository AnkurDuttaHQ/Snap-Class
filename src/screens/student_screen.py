
import streamlit as st
import numpy as np
from PIL import Image
from src.ui.camera_style import camera_page_style
from src.components.header import header_layout_dashboard_student_login
from src.ui.home_basic_layout import home_page_dashboard, style_base_layout
from src.components.footer import footer_layout_dashboard


def student_screen():

    style_base_layout()
    home_page_dashboard()
    header_layout_dashboard_student_login()
    camera_page_style()
    with st.container(key="student_camera"):

        picture = st.camera_input(
            "Position Your Face Inside the Rectangle",
            key="student_face_capture",
            resolution="720p",
            width="stretch"
        )

        # Check whether an image has been captured
        if picture is not None:

            # Convert image to RGB
            image = Image.open(picture).convert("RGB")

            # Convert to NumPy array
            image_array = np.array(image)

            # Get image bytes
            image_bytes = picture.getvalue()

            st.success("Photo captured successfully!")

            st.write("Image shape:", image_array.shape)

            # Next: Face detection and recognition

    footer_layout_dashboard()
