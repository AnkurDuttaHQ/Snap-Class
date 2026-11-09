
import streamlit as st


def camera_page_style():

    st.markdown("""
    <style>

    /* ==================================
       ROSE QUARTZ CAMERA THEME
    ================================== */

    :root {
        --rose-bg: #FFF1F5;
        --rose-card: #FFFFFF;
        --rose-primary: #E879A5;
        --rose-accent: #DB2777;
        --rose-dark: #831843;
        --rose-text: #24243D;
        --rose-muted: #9D667D;
        --rose-border: #F3B4CB;
        --rose-success: #166534;
        --rose-success-bg: #F0FDF4;
    }


    /* Main background */
    .stApp {
        background: var(--rose-bg) !important;
    }


    /* Camera container */
    .st-key-student_camera {
        background: var(--rose-card) !important;

        border: 2px solid var(--rose-border);
        border-radius: 24px;

        padding: 24px;

        max-width: 950px;
        margin: 25px auto;

        box-shadow:
            0 8px 30px rgba(219, 39, 119, 0.08);

        transition: all 0.3s ease;
    }

    .st-key-student_camera:hover {
        border-color: var(--rose-primary);

        box-shadow:
            0 10px 35px rgba(219, 39, 119, 0.14);
    }


    /* Camera heading */
    .st-key-student_camera
    [data-testid="stWidgetLabel"],
    .st-key-student_camera
    [data-testid="stWidgetLabel"] p {

        color: var(--rose-dark) !important;

        font-size: 21px !important;
        font-weight: 700 !important;

        margin-bottom: 15px;
    }


    /* Camera preview */
    .st-key-student_camera video {

        width: 100%;

        border: 2px solid var(--rose-border);
        border-radius: 18px;

        object-fit: cover;
    }


    /* Captured image */
    .st-key-student_camera img {

        border: 2px solid var(--rose-primary);
        border-radius: 18px;

        width: 100%;
    }


    /* Capture / Clear buttons */
    .st-key-student_camera button {

        background: var(--rose-primary) !important;

        color: #FFFFFF !important;

        border: none !important;
        border-radius: 14px !important;

        min-height: 50px;

        font-size: 16px !important;
        font-weight: 700 !important;

        transition: all 0.3s ease;
    }

    .st-key-student_camera button:hover {

        background: var(--rose-accent) !important;

        color: #FFFFFF !important;

        transform: translateY(-2px);

        box-shadow:
            0 6px 18px rgba(219, 39, 119, 0.22);
    }


    /* Success alert */
    .st-key-student_camera
    [data-testid="stAlert"] {

        background: var(--rose-success-bg) !important;

        border: 1px solid #86EFAC !important;
        border-radius: 14px !important;

        padding: 16px !important;
    }


    /* Success message text */
    .st-key-student_camera
    [data-testid="stAlert"] p {

        color: var(--rose-success) !important;

        font-size: 17px !important;
        font-weight: 600 !important;
    }


    /* Success icon */
    .st-key-student_camera
    [data-testid="stAlert"] svg {

        color: var(--rose-success) !important;
    }


    /* Helper text */
    .st-key-student_camera small {

        color: var(--rose-muted) !important;
    }


    /* Smooth animation */
    .st-key-student_camera {

        animation: roseFade 0.7s ease-out;
    }

    @keyframes roseFade {

        from {
            opacity: 0;
            transform: translateY(15px);
        }

        to {
            opacity: 1;
            transform: translateY(0);
        }
    }


    /* Accessibility */
    @media (prefers-reduced-motion: reduce) {
        .st-key-student_camera {
            animation: none;
            transition: none;
        }
    }

    </style>
    """, unsafe_allow_html=True)
