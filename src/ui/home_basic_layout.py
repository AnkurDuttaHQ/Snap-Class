import streamlit as st

def home_page_style():

    st.markdown("""
    <style>

    /* Home Screen Background */
    .stApp {
        background:
            radial-gradient(
                circle at 15% 20%,
                #5865F2 0%,
                transparent 40%
            ),
            radial-gradient(
                circle at 85% 80%,
                #404EED 0%,
                transparent 40%
            ),
            linear-gradient(
                135deg,
                #101225,
                #171B38,
                #101225
            ) !important;

        color: #FFFFFF;
    }

    /* Headings */
    h1, h2, h3 {
        color: #FFFFFF !important;
    }

    /* Buttons */
    div.stButton > button {
        width: 100%;
        min-height: 55px;
        background: #5865F2;
        color: #FFFFFF !important;
        border: 1px solid #7983F5;
        border-radius: 12px;
        font-size: 16px;
        font-weight: 700;
        transition: all 0.3s ease;
    }

    div.stButton > button:hover {
        background: #404EED;
        transform: translateY(-4px);
        box-shadow: 0 8px 25px rgba(88,101,242,0.4);
    }

    /* Entrance animation */
    .block-container {
        animation: fadeUp 0.8s ease-out;
    }

    @keyframes fadeUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* Hide Streamlit header and footer */
    [data-testid="stHeader"],
    [data-testid="stFooter"],
    [data-testid="stAppDeployButton"],
    [data-testid="stDecoration"],
    #MainMenu {
        display: none !important;
    }

    </style>
    """, unsafe_allow_html=True)