import streamlit as st
from src.screens.home_screen import home_screen
from src.screens.student_screen import student_screen
from src.screens.teacher_screen import teacher_screen
from src.ui.global_theme import apply_global_theme
from src.components.auto_enroll_dialog import auto_enroll_dialog
apply_global_theme()

def main():
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    match st.session_state['login_type']:
        case "teacher":
            teacher_screen()

        case "student":
            student_screen()
        case None:
            home_screen()


    query_params = st.query_params.get("join-code")
    if query_params:
        if st.session_state.login_type != 'student':
            st.session_state.login_type = 'student'
            st.rerun()
        if st.session_state.get("is_logged_in") and st.session_state.get("user_role") == 'student':
            auto_enroll_dialog(query_params)
main()
            
