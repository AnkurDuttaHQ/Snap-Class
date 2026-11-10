
import streamlit as st
import numpy as np
import time
import io
from PIL import Image

from src.ui.camera_style import camera_page_style
from src.components.header import header_layout_dashboard_student_login
from src.ui.home_basic_layout import home_page_dashboard, style_base_layout
from src.components.footer import footer_layout_dashboard

from src.pipelines.face_recognisition_model import (
    predict_attendence,
    get_face_embeddings,
    trained_classifier
)

from src.database.db import get_all_students, create_student
from src.pipelines.voice_recognition import load_voice_embeddings


def student_dashboard():
    st.header("Student Dashboard")


def student_screen():

    # Initialize session state
    if "show_registration" not in st.session_state:
        st.session_state.show_registration = False

    if "captured_image" not in st.session_state:
        st.session_state.captured_image = None

    style_base_layout()
    home_page_dashboard()

    # Already logged in
    if "student_data" in st.session_state:
        student_dashboard()
        return

    header_layout_dashboard_student_login()
    camera_page_style()

    # Face capture section
    with st.container(key="student_camera"):

        picture = st.camera_input(
            "Position Your Face Inside the Rectangle",
            key="student_face_capture",
            resolution="720p",
            width="stretch"
        )

        if picture is not None:

            st.session_state.captured_image = picture.getvalue()

            captured_image = st.session_state.get("captured_image")

            if isinstance(captured_image, (bytes, bytearray)):
                image = Image.open(
                    io.BytesIO(bytes(captured_image))
                ).convert("RGB")

            else:
                st.error("Invalid or missing captured image. Please capture your face again.")
                st.session_state.captured_image = None
                st.stop()

            image_array = np.array(image)

            st.success("Photo captured successfully!")

            with st.spinner("Scanning in Progress...."):

                detected, all_ids, no_of_faces = predict_attendence(
                    image_array
                )

                if no_of_faces == 0:

                    st.warning("Face not found.")

                elif no_of_faces > 1:

                    st.warning("Multiple faces found. Please capture again.")

                else:

                    if detected:

                        student_id = list(detected.keys())[0]

                        all_students = get_all_students()

                        student = next(
                            (
                                s for s in all_students
                                if s["student_id"] == student_id
                            ),
                            None
                        )

                        if student:

                            st.session_state.is_logged_in = True
                            st.session_state.user_role = "student"
                            st.session_state.student_data = student

                            st.toast(f"Welcome back {student['name']}!")

                            time.sleep(1)
                            st.rerun()

                    else:

                        st.info(
                            "Face not recognised! "
                            "You might be a new student."
                        )

                        st.session_state.show_registration = True

    # Registration section
    if st.session_state.show_registration:

        with st.container(border=True):

            st.header("Register New Profile")

            new_name = st.text_input(
                "Enter Your name",
                placeholder="E.g. Ankur Dutta"
            )

            st.subheader("Optional: Voice Enrollment")

            st.info(
                "Enroll your voice for optional voice-based attendance."
            )

            audio_data = st.audio_input(
                "Record a short phrase, such as "
                "'I am present, my name is Ankur'."
            )

            if st.button("Create Account", type="primary"):

                if not new_name.strip():

                    st.warning("Please enter your name.")

                elif st.session_state.captured_image is None:

                    st.warning("Please capture your face again.")

                else:

                    
                    with st.spinner("Creating your profile..."):

                        captured_image = st.session_state.get("captured_image")

                        if not isinstance(captured_image, (bytes, bytearray)):
                            st.error("Please capture your face again.")
                            st.stop()

                        image = Image.open(
                            io.BytesIO(bytes(captured_image))
                        ).convert("RGB")

                        image_array = np.array(image)

                        embeddings = get_face_embeddings(image_array)


                        if embeddings is not None and len(embeddings) > 0:

                            face_embd = embeddings[0].tolist()

                            voice_embd = None

                            if audio_data is not None:

                                voice_embd = load_voice_embeddings(
                                    audio_data.getvalue()
                                )

                            response_data = create_student(
                                new_name.strip(),
                                face_embedding=face_embd,
                                voice_embedding=voice_embd
                            )

                            if response_data:

                                trained_classifier()

                                st.session_state.is_logged_in = True
                                st.session_state.user_role = "student"
                                st.session_state.student_data = response_data[0]

                                st.session_state.show_registration = False

                                st.toast(
                                    f"Profile created! Hi {new_name}!"
                                )

                                time.sleep(1)
                                st.rerun()

                            else:

                                st.error(
                                    "Unable to create your profile. "
                                    "Please try again."
                                )

                        else:

                            st.error(
                                "Couldn't capture your facial features "
                                "for registration."
                            )

    footer_layout_dashboard()
