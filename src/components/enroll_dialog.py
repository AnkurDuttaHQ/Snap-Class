import streamlit as st
from src.database.db import create_subject,enroll_student_tosubject
from src.database.config import supabase

@st.dialog("Enroll in subject")
def enroll_dialog():
    st.write("Enter the subject code provided by your teacher")

    join_code = st.text_input("subject code",placeholder="Eg. CSE102")

    if st.button("Enroll in",type="primary",width="stretch"):
        if join_code:
            res = supabase.table("subjects").select("subject_id , name , subject_code").eq("subject_code",join_code).execute()
            if res.data:
                subject = res.data[0]
                student_id = st.session_state.student_data["student_id"]
                check = supabase.table("subject_students").select("*").eq("subject_id",subject["subject_id"]).eq("student_id",student_id).execute()

                if check.data:
                    st.warning("You have already enrolled in this subject")

                else:
                    enroll_student_tosubject(subject["subject_id"],student_id)
                    st.success("You have successfully enrolled")
                    import time
                    time.sleep(1)
                    st.rerun()

        else:
            st.warning("Please Enter a subject code")
