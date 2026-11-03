import streamlit as st

def home_page_style():

    st.markdown("""
    <style>
        .stApp{
            background:#5865F2 !important;
        }
    </style>
    """, unsafe_allow_html=True)


def home_page_dashboard():
    st.markdown("""
        <style>
            .stApp{
                background:#E0E3FF !important;
            }
        </style>
        """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Montserrat:ital,wght@0,100..900;1,100..900&family=Outfit:wght@100..900&display=swap');

            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Montserrat:ital,wght@0,100..900;1,100..900&family=Outfit:wght@100..900&display=swap');
            
            *{
                box-sizing:border-box;
            }
            html {
                scroll-behavior: smooth;
            }
            h2 {
                font-family:'Climate Crisis', sans-serif !important;
                line-height: 1.15 !important;
                letter-spacing: -1.5px !important;
                font-weight: 400 !important;
                color:#EOE3FF !imprtant;
            }

            
            /* =================================
            SNAPCLASS BUTTON SYSTEM
            ================================= */

            /* PRIMARY BUTTON — PINK */

            div.stButton > button[kind="primary"] {
                background: #6C63E6 !important;
                color: #FFFFFF !important;
                border: 1px solid #EB459E !important;
                border-radius: 1.2rem !important;

                font-family: 'Montserrat', sans-serif !important;
                font-weight: 700 !important;

                transition: all 0.3s ease !important;
            }

            /* Primary hover */

            div.stButton > button[kind="primary"]:hover {
                background: #554BD1  !important;
                border-color: #D9368D !important;
                color: #FFFFFF !important;

                transform: translateY(-4px) !important;
                box-shadow: 0 10px 25px rgba(235, 69, 158, 0.3) !important;
            }

            /* SECONDARY BUTTON — PURPLE */

            div.stButton > button[kind="secondary"] {
                background: #EB459E !important;
                color: #FFFFFF !important;
                border: 1px solid #6C63E6 !important;
                border-radius: 1.2rem !important;

                font-family: 'Montserrat', sans-serif !important;
                font-weight: 700 !important;

                transition: all 0.3s ease !important;
            }

            /* Secondary hover */

            div.stButton > button[kind="secondary"]:hover {
                background: #D9368D !important;
                border-color: #554BD1 !important;
                color: #FFFFFF !important;

                transform: translateY(-4px) !important;
                box-shadow: 0 10px 25px rgba(108, 99, 230, 0.3) !important;
            }

            /* CLICK EFFECT */

            div.stButton > button:active {
                transform: scale(0.97) !important;
                box-shadow: none !important;
            }

            /* FOCUS EFFECT */

                div.stButton > button:focus-visible {
                outline: 3px solid rgba(235, 69, 158, 0.35) !important;
                outline-offset: 4px !important;

            /* Click animation */

            div.stButton > button:active,
            button[kind="secondary"]:active {
                transform: scale(0.96) !important;
                transition: transform 0.1s ease !important;
            }

            /* Animated shine */

            div.stButton > button::before {
                content: "";
                position: absolute;
                top: 0;
                left: -120%;
                width: 60%;
                height: 100%;
                background: linear-gradient(
                    110deg,
                    transparent,
                    rgba(255,255,255,0.22),
                    transparent
                );
                transform: skewX(-20deg);
                transition: left 0.65s ease;
            }

            div.stButton > button:hover::before {
                left: 150%;
            }

            /* ==============================
            CARDS & CONTAINERS
            ============================== */

            div[data-testid="stVerticalBlockBorderWrapper"] {
                border-radius: 1.3rem !important;
                border: 1px solid rgba(255,255,255,0.08) !important;

                transition:
                    transform 0.3s ease,
                    border-color 0.3s ease,
                    box-shadow 0.3s ease !important;
            }

            div[data-testid="stVerticalBlockBorderWrapper"]:hover {
                transform: translateY(-3px);
                border-color: rgba(235,69,158,0.45) !important;
                box-shadow: 0 12px 30px rgba(0,0,0,0.2);
            }

            /* ==============================
            INPUT FIELDS
            ============================== */

            div[data-baseweb="input"],
            div[data-baseweb="textarea"],
            div[data-baseweb="select"] {
                border-radius: 0.9rem !important;
                transition: all 0.25s ease !important;
            }

            div[data-baseweb="input"]:focus-within,
            div[data-baseweb="textarea"]:focus-within,
            div[data-baseweb="select"]:focus-within {
                border-color: #EB459E !important;
                box-shadow: 0 0 0 3px rgba(235,69,158,0.15) !important;
            }

            /* ==============================
            TABS
            ============================== */

            button[data-baseweb="tab"] {
                font-family: 'Outfit', sans-serif !important;
                font-weight: 600 !important;
                transition: all 0.25s ease !important;
            }

            button[data-baseweb="tab"]:hover {
                color: #EB459E !important;
            }

            button[data-baseweb="tab"][aria-selected="true"] {
                color: #EB459E !important;
            }

            /* ==============================
            EXPANDERS
            ============================== */

            details {
                border-radius: 1rem !important;
                transition: border-color 0.3s ease !important;
            }

            details summary {
                font-family: 'Outfit', sans-serif !important;
                font-weight: 650 !important;
                cursor: pointer;
            }

            /* ==============================
            SCROLLBAR
            ============================== */

            ::-webkit-scrollbar {
                width: 7px;
            }

            ::-webkit-scrollbar-track {
                background: #101010;
            }

            ::-webkit-scrollbar-thumb {
                background: #444;
                border-radius: 20px;
            }

            ::-webkit-scrollbar-thumb:hover {
                background: #EB459E;
            }

            /* ==============================
            SELECTION
            ============================== */

            ::selection {
                background: #EB459E;
                color: white;
            }

            /* ==============================
            ACCESSIBILITY
            ============================== */

            @media (prefers-reduced-motion: reduce) {
                *,
                *::before,
                *::after {
                    animation-duration: 0.01ms !important;
                    transition-duration: 0.01ms !important;
                    scroll-behavior: auto !important;
                }
            }

            
            /* ===== BUTTON DEFAULT STATE ===== */

            div.stButton > button {
                background: #FFFFFF !important;
                color: #252542 !important;
                border: 1px solid rgba(255,255,255,0.3) !important;
                border-radius: 1.2rem !important;

                transition: all 0.3s cubic-bezier(0.2, 0.8, 0.2, 1) !important;
            }

            /* ===== BUTTON HOVER STATE ===== */

            div.stButton > button:hover {
                background: #EB459E !important;
                background-color: #EB459E !important;
                color: #FFFFFF !important;

                border: 1px solid #EB459E !important;

                transform: translateY(-4px) !important;

                box-shadow:
                    0 8px 20px rgba(235, 69, 158, 0.25),
                    0 15px 35px rgba(0, 0, 0, 0.12) !important;
            }

            /* ===== BUTTON CLICK STATE ===== */

            div.stButton > button:active {
                background: #D9368D !important;
                color: #FFFFFF !important;
                transform: scale(0.97) !important;
                box-shadow: none !important;
            }

            /* ===== KEYBOARD FOCUS ===== */

            div.stButton > button:focus-visible {
                outline: 3px solid rgba(235, 69, 158, 0.4) !important;
                outline-offset: 4px !important;
            }

            /* ===== DISABLED BUTTON ===== */

            div.stButton > button:disabled {
                opacity: 0.5 !important;
                cursor: not-allowed !important;
                transform: none !important;
                box-shadow: none !important;
            }
      
        </style>
        """, unsafe_allow_html=True)
