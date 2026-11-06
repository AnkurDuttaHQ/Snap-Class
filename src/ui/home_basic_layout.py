
import streamlit as st

def home_page_style():

    st.markdown("""
    <style>

        .stApp {
            background: #5865F2 !important;
        }

        /* WHITE HOME SCREEN TYPOGRAPHY */

        .stApp h1,
        .stApp h2,
        .stApp h3,
        .stApp h4,
        .stApp p,
        .stApp label,
        .stApp [data-testid="stCaptionContainer"] {
            color:#FFFFFF !important;
        }

        /* PORTAL CARD TYPOGRAPHY */

        .stApp .st-key-student_card h2,
        .stApp .st-key-teacher_card h2 {
            color: #24243D !important;
        }

        .stApp .st-key-student_card .portal-description,
        .stApp .st-key-teacher_card .portal-description {
            color: #555575 !important;
        }

    </style>
    """, unsafe_allow_html=True)


# ============================================
# DASHBOARD STYLE
# Light lavender background + Dark typography
# ============================================

def home_page_dashboard():

    st.markdown("""
    <style>

        .stApp {
            background: #E0E3FF !important;
        }

        /* DARK DASHBOARD TYPOGRAPHY */

        .stApp h1,
        .stApp h2,
        .stApp h3,
        .stApp h4,
        .stApp h5,
        .stApp h6 {
            color: #24243D !important;
        }

        .stApp [data-testid="stMarkdownContainer"] p {
            color: #292536 !important;
        }

        .stApp label,
        .stApp [data-testid="stCaptionContainer"] {
            color: #292536 !important;
        }

        /* INPUT TEXT */

        .stApp input,
        .stApp textarea {
            color: #24243D !important;
        }

    </style>
    """, unsafe_allow_html=True)


# ============================================
# GLOBAL BASE LAYOUT
# Shared fonts, buttons, cards and components
# No page-specific text colors here
# ============================================

def style_base_layout():

    st.markdown("""
    <style>

        /* =================================
           FONT IMPORTS
        ================================= */

        @import url(
            'https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Montserrat:ital,wght@0,100..900;1,100..900&family=Outfit:wght@100..900&display=swap'
        );

        * {
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        /* GLOBAL HEADING FONT */

        .stApp h1,
        .stApp h2 {
            font-family: 'Climate Crisis', sans-serif !important;
            line-height: 1.15 !important;
            letter-spacing: -1.5px !important;
            font-weight: 400 !important;
        }

        /* =================================
           SNAPCLASS BUTTON SYSTEM
        ================================= */

        /* PRIMARY — PURPLE */
        div.stButton > button[kind='primary'] {
            background : #6C63E6 !important;
            border: 1px solid #6C63E6 !important;
            border-radius: 1.2rem !important;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 700 !important;
            position: relative;
            overflow: visible !important;
            transition: all 0.3s ease !important;
        }

        div.stButton > button[kind="primary"]:hover {
            background: #554BD1 !important;
            border-color: #554BD1 !important;
            color: #FFFFFF !important;
            transform: translateY(-4px) !important;
            box-shadow: 0 10px 25px rgba(108, 99, 230, 0.3) !important;
        }

        /* SECONDARY — PINK */
        div.stButton > button[kind="secondary"] {
            background: #EB459E !important;
            color: #FFFFFF !important;
            border: 0.5px solid #EB459E !important;
            border-radius: 1.2 rem !important;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 500 !important;
            position: relative;
            overflow: visible !important;
            transition: all 0.3s ease !important;
        }

        div.stButton > button[kind="secondary"]:hover {
            background: #D9368D !important;
            border-color: #D9368D !important;
            color: #FFFFFF !important;
            transform: translateY(-4px) !important;
            box-shadow: 0 10px 25px rgba(235, 69, 158, 0.3) !important;
        }

        /* BUTTON LABEL */
        div.stButton > button p,
        div.stButton > button span {
            color: inherit !important;
            visibility: visible !important;
            opacity: 1 !important;
        }

        /* DEFAULT BUTTON */
        div.stButton > button:not([kind="primary"]):not([kind="secondary"]) {
            background: #FFFFFF !important;
            color: #252542 !important;
            border: 1px solid rgba(255,255,255,0.3) !important;
            border-radius: 1.2rem !important;
            transition: all 0.3s ease !important;
        }

        /* DEFAULT HOVER */
        div.stButton > button:not([kind="primary"]):not([kind="secondary"]):hover {
            background: #EB459E !important;
            color: #FFFFFF !important;
            border-color: #EB459E !important;
        }

        /* FOCUS */
        div.stButton > button:focus-visible {
            outline: 3px solid rgba(235, 69, 158, 0.35) !important;
            outline-offset: 4px !important;
        }

        /* DISABLED */
        div.stButton > button:disabled {
            opacity: 0.5 !important;
            cursor: not-allowed !important;
            transform: none !important;
            box-shadow: none !important;
        }

        /* =================================
           CARDS & CONTAINERS
        ================================= */

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

        /* =================================
           INPUT FIELDS
        ================================= */

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

            box-shadow:
                0 0 0 3px rgba(235,69,158,0.15) !important;
        }

        /* =================================
           TABS
        ================================= */

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

        /* =================================
           EXPANDERS
        ================================= */

        details {

            border-radius: 1rem !important;

            transition: border-color 0.3s ease !important;
        }

        details summary {

            font-family: 'Outfit', sans-serif !important;
            font-weight: 650 !important;

            cursor: pointer;
        }

        /* =================================
           SCROLLBAR
        ================================= */

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

        /* =================================
           TEXT SELECTION
        ================================= */

        ::selection {

            background: #EB459E;
            color: white;
        }

        /* =================================
           ACCESSIBILITY
        ================================= */

        @media (prefers-reduced-motion: reduce) {

            *,
            *::before,
            *::after {

                animation-duration: 0.01ms !important;
                transition-duration: 0.01ms !important;

                scroll-behavior: auto !important;
            }
        }

        /* SNAPCLASS DASHBOARD HOME BUTTON */

        .st-key-dashboardBack_home button {
            background: #6C63E6 !important;
            color: #FFFFFF !important;
            border: 1px solid #6C63E6 !important;
            border-radius: 1.2rem !important;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 700 !important;
        }

        /* BUTTON TEXT */
        .st-key-dashboardBack_home button span,
        .st-key-dashboardBack_home button p {
            color: #FFFFFF !important;
        }

        /* HOVER */
        .st-key-dashboardBack_home button:hover {
            background: #554BD1 !important;
            border-color: #554BD1 !important;
        }

    </style>
    """, unsafe_allow_html=True)
