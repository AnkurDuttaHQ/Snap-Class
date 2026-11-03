import streamlit as st
from src.ui.home_basic_layout import home_page_dashboard

def teacher_screen():
    home_page_dashboard()
    st.header("Teacher screen")