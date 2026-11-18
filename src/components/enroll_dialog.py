import streamlit as st
from src.database.db import enroll_student_tosubject,create_subject
from src.database.config import supabase



def custom_message(title, message, color="#EF4444"):
    st.markdown(
        f"""
        <div style="
            background: #222222;
            border: 1px solid {color};
            border-left: 5px solid {color};
            border-radius: 10px;
            padding: 14px 16px;
            margin: 12px 0;
        ">
            <div style="color:{color}; font-size:16px; font-weight:700;">
                {title}
            </div>
            <div style="color:#FFFFFF; font-size:13px; margin-top:5px;">
                {message}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

@st.dialog("Enroll in subject")
def enroll_dialog():
    st.write("Enter the subject code provided by your teacher.")

    join_code = st.text_input(
        "Subject code",
        placeholder="Eg. CSE102"
    )

    if st.button("Enroll in", type="primary", width="stretch"):

        if not join_code or not join_code.strip():
            custom_message(
                "Missing subject code",
                "Please enter the subject code provided by your teacher."
            )
            return

        try:
            join_code = join_code.strip().upper()

            # Find the subject
            res = (
                supabase.table("subjects")
                .select("subject_id, subject_code")
                .eq("subject_code", join_code)
                .execute()
            )

            if not res.data:
                custom_message(
                    "Subject not found",
                    "Please check the subject code and try again."
                )
                return

            subject = res.data[0]
            student_id = st.session_state.student_data["student_id"]

            # Check existing enrollment
            check = (
                supabase.table("subject_students")
                .select("subject_id")
                .eq("subject_id", subject["subject_id"])
                .eq("student_id", student_id)
                .execute()
            )

            if check.data:
                custom_message(
                    "Already enrolled",
                    "You are already enrolled in this subject.",
                    "#F59E0B"
                )
                return

            # Enroll student
            enroll_student_tosubject(
                subject["subject_id"],
                student_id
            )

            custom_message(
                "Enrollment successful!",
                "You have successfully joined the subject.",
                "#A3E635"
            )

            import time
            time.sleep(1)
            st.rerun()

        except Exception as e:
            # Keep technical details in the terminal, not the student UI
            print(f"Enrollment error: {e}")

            custom_message(
                "Something went wrong",
                "We couldn't complete your enrollment. Please try again."
            )
