
import streamlit as st
from pathlib import Path

from src.components.header import header_layout
from src.ui.home_basic_layout import home_page_style
from src.ui.home_basic_layout import style_base_layout


ASSET_DIR = Path(__file__).resolve().parents[1] / "Assets"


def home_screen():

    # =================================
    # GLOBAL HOME PAGE STYLING
    # =================================

    home_page_style()
    style_base_layout()

    # =================================
    # PREMIUM CARD CSS
    # =================================

    st.markdown("""
    <style>

    /* =================================
       PORTAL CARDS
    ================================= */

    .st-key-student_card,
    .st-key-teacher_card {

        position: relative !important;
        isolation: isolate !important;
        overflow: hidden !important;

        background: #E8E9FF !important;
        border: 1px solid rgba(255,255,255,0.6) !important;
        border-radius: 3rem !important;

        padding: 2rem !important;
        min-height: 450px !important;

        transition:
            transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1),
            box-shadow 0.4s ease,
            border-color 0.4s ease !important;

        animation: cardReveal 0.7s ease both;
    }

    /* CARD HOVER */

    .st-key-student_card:hover,
    .st-key-teacher_card:hover {

        transform: translateY(-10px) scale(1.015) !important;

        border-color: rgba(108,99,230,0.65) !important;

        box-shadow:
            0 22px 45px rgba(35,30,110,0.20),
            0 0 22px rgba(235,69,158,0.16) !important;
    }


    /* =================================
       ANIMATED SHINE EFFECT
    ================================= */

    .st-key-student_card::before,
    .st-key-teacher_card::before {

        content: "";
        position: absolute;

        top: 0;
        left: -130%;

        width: 65%;
        height: 100%;

        background: linear-gradient(
            110deg,
            transparent,
            rgba(255,255,255,0.4),
            transparent
        );

        transform: skewX(-20deg);

        transition: left 0.8s ease;

        pointer-events: none;
        z-index: 3;
    }

    .st-key-student_card:hover::before,
    .st-key-teacher_card:hover::before {
        left: 150%;
    }


    /* =================================
       CARD TITLES
    ================================= */

    .portal-heading {

        font-family: 'Climate Crisis', sans-serif !important;
        font-size: 2rem !important;
        line-height: 1.1 !important;

        color: #24243D !important;

        margin-bottom: 12px !important;

        transition: transform 0.35s ease !important;
    }

    .st-key-student_card:hover .portal-heading,
    .st-key-teacher_card:hover .portal-heading {
        transform: translateX(5px);
    }


    /* =================================
       CARD DESCRIPTION
    ================================= */

    .portal-description {

        font-family: 'Outfit', sans-serif !important;
        font-size: 1rem !important;
        line-height: 1.7 !important;

        color: #555575 !important;

        min-height: 65px;
    }


    /* =================================
       CARD IMAGES
    ================================= */

    .st-key-student_card img,
    .st-key-teacher_card img {

        object-fit: contain !important;

        transition:
            transform 0.5s cubic-bezier(0.2, 0.8, 0.2, 1),
            filter 0.4s ease !important;
    }

    .st-key-student_card:hover img,
    .st-key-teacher_card:hover img {

        transform: scale(1.09) translateY(-5px) !important;

        filter: drop-shadow(
            0 12px 10px rgba(60,60,130,0.15)
        );
    }


    /* =================================
       LOGIN BUTTONS
    ================================= */

    .st-key-student_card div.stButton > button,
    .st-key-teacher_card div.stButton > button {

        background: #5865F2 !important;
        color: #FFFFFF !important;

        border: 1px solid #5865F2 !important;
        border-radius: 3rem !important;

        min-height: 3.5rem !important;

        font-family: 'Outfit', sans-serif !important;
        font-size: 1rem !important;
        font-weight: 600 !important;

        transition: all 0.3s ease !important;
    }

    .st-key-student_card div.stButton > button:hover,
    .st-key-teacher_card div.stButton > button:hover {

        background: #4653D5 !important;
        border-color: #4653D5 !important;

        transform: translateY(-4px) !important;

        box-shadow:
            0 10px 25px rgba(88,101,242,0.3) !important;
    }

    .st-key-student_card div.stButton > button:active,
    .st-key-teacher_card div.stButton > button:active {

        transform: scale(0.97) !important;
        box-shadow: none !important;
    }


    /* =================================
       ENTRANCE ANIMATION
    ================================= */

    @keyframes cardReveal {

        from {
            opacity: 0;
            transform: translateY(25px);
        }

        to {
            opacity: 1;
            transform: translateY(0);
        }
    }


    /* =================================
       RESPONSIVE DESIGN
    ================================= */

    @media(max-width: 768px) {

        .st-key-student_card,
        .st-key-teacher_card {

            padding: 1.5rem !important;
            min-height: 380px !important;
            border-radius: 2rem !important;
        }

        .portal-heading {
            font-size: 1.6rem !important;
        }
    }


    /* =================================
       ACCESSIBILITY
    ================================= */

    @media(prefers-reduced-motion: reduce) {

        .st-key-student_card,
        .st-key-teacher_card,
        .st-key-student_card *,
        .st-key-teacher_card * {

            animation: none !important;
            transition: none !important;
        }
    }

    </style>
    """, unsafe_allow_html=True)


    # =================================
    # HEADER
    # =================================

    header_layout()


    # =================================
    # PORTAL LAYOUT
    # =================================

    col1, col2 = st.columns(2, gap="large")


    # =================================
    # STUDENT CARD
    # =================================

    with col1:

        with st.container(key="student_card"):

            st.markdown("""
                <h2 class="portal-heading">
                    I ' m<br>Student
                </h2>

                <p class="portal-description">
                    View attendance records and
                    monitor your attendance percentage.
                </p>
            """, unsafe_allow_html=True)

            st.image(
                str(ASSET_DIR / "student.png"),
                width=190
            )

            if st.button(
                "Student Portal  ↗",
                key="student_login",
                use_container_width=True,
                type="primary"
            ):

                st.session_state['login_type'] = "student"
                st.rerun()


    # =================================
    # TEACHER CARD
    # =================================

    with col2:

        with st.container(key="teacher_card"):

            st.markdown("""
                <h2 class="portal-heading">
                    I ' m<br>Teacher
                </h2>

                <p class="portal-description">
                    Manage classes and monitor
                    student attendance.
                </p>
            """, unsafe_allow_html=True)

            st.image(
                str(ASSET_DIR / "teacher.png"),
                width=190
            )

            if st.button(
                "Teacher Portal  ↗",
                key="teacher_login",
                use_container_width=True,
                type="primary"
            ):

                st.session_state['login_type'] = "teacher"
                st.rerun()
