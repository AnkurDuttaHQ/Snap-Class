import streamlit as st
from src.components.header import header_layout_dashboard
from src.ui.home_basic_layout import home_page_dashboard
def teacher_screen():
    home_page_dashboard()
    header_layout_dashboard()

    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&family=Outfit:wght@400;500;600;700&display=swap');

        .teacher-page-title {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: clamp(20px, 4vw, 48px) !important;
            font-weight: 400 !important;
            line-height: 1.2 !important;
            letter-spacing: -1px !important;
            color: #24243D !important;
            text-align: center !important;
            margin: 15px 0 30px 0 !important;
        }
        </style>
        """, unsafe_allow_html=True)