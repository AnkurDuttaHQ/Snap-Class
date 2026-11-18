import streamlit as st
from src.database.db import enroll_student_tosubject,create_subject
from src.database.config import supabase


@st.dialog(" Quick Enrollment")

def auto_enroll_dialog(subject_code):
    student_id = st.session_state.student_data["student_id"]

    try:
        # Find subject using subject code
        res = (
            supabase.table("subjects")
            .select("subject_id, subject_name, subject_code")
            .eq("subject_code", subject_code.strip().upper())
            .execute()
        )

        if not res.data:
            st.error("Subject code not found.")

            if st.button("Close"):
                st.query_params.clear()
                st.rerun()

            return

        subject = res.data[0]
        subject_id = subject["subject_id"]

        # Check existing enrollment
        check = (
            supabase.table("subject_students")
            .select("subject_id")
            .eq("subject_id", subject_id)
            .eq("student_id", student_id)
            .execute()
        )

        if check.data:
            st.info("You have already enrolled in this subject!")

            if st.button("Got it"):
                st.query_params.clear()
                st.rerun()

            return

        st.markdown(
            f"Would you like to enroll in **{subject['subject_name']}**?"
        )

        col1, col2 = st.columns(2)

        with col1:
            if st.button("No Thanks", width="stretch"):
                st.query_params.clear()
                st.rerun()

        with col2:
            if st.button(
                "Yes Enroll",
                type="primary",
                width="stretch"
            ):
                enroll_student_tosubject(
                    subject_id,
                    student_id
                )

                st.toast("Joined successfully!")
                st.query_params.clear()

                import time
                time.sleep(1)
                st.rerun()

    except Exception as e:
        print(f"Auto enrollment error: {e}")
        st.error(
            "We couldn't complete your enrollment. Please try again."
        )
