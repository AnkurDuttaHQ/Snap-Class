import streamlit as st

def apply_global_theme():
    st.markdown("""
        <style>
            
                /* Hide Streamlit Header */
                [data-testid="stHeader"] {
                display: none !important;
                }

                /* Hide Streamlit Footer */
                [data-testid="stFooter"] {
                    display: none !important;
                }

                /* Hide Deploy Button */
                [data-testid="stAppDeployButton"] {
                    display: none !important;
                }

                /* Hide Main Menu */
                #MainMenu {
                    display: none !important;
                }

                /* Remove top spacing */
                .block-container {
                    padding-top: 1rem !important;
                    padding-bottom: 0rem !important;
                }

                /* Full viewport background */
                .stApp {
                    min-height: 100vh;
                    width: 100%;
                }

                /* Hide top decoration */
                [data-testid="stDecoration"] {
                    display: none !important;
                }
                

                .main .block-container {
                max-width: 100% !important;
                padding-left: 3rem;
                padding-right: 3rem;
                }
    
        </style>
        """, unsafe_allow_html=True)
    