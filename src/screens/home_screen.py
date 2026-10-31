import streamlit as st
from src.components.header import header_layout
from src.ui.home_basic_layout import home_page_style

def home_screen():
    header_layout()
    home_page_style()
    st.markdown("""
        <div style="text-align:center; padding:35px 0 25px;">
            <h1 style="font-size:42px;">
                AI Attendance System
            </h1>
            <p style="color:#94A3B8; font-size:18px;">
                Intelligent Attendance. Smarter Education.
            </p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 👨‍🏫 Teacher Portal")
        st.write("Manage classes and monitor student attendance.")

        if st.button("Teacher Login", use_container_width=True):
            st.session_state['login_type'] = "teacher"
            st.rerun()

    with col2:
        st.markdown("### 🎓 Student Portal")
        st.write("View attendance records and attendance percentage.")

        if st.button("Student Login", use_container_width=True):
            st.session_state['login_type'] = "student"
            st.rerun()
