import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64
from src.ui.home_basic_layout import style_base_layout

def header_layout():

    logo_path = Path(__file__).resolve().parents[1] / "Assets" / "logo.jpg"

    with open(logo_path, "rb") as image:
        logo = base64.b64encode(image.read()).decode("utf-8")

    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <link href="https://fonts.googleapis.com/css2?family=Climate+Crisis&family=Outfit:wght@400;500;600;700&display=swap"
              rel="stylesheet">

        <style>
            * {{
                box-sizing: border-box;
            }}

            body {{
                margin: 0;
                padding: 0;
                background: transparent;
            }}

            .snap-header {{
                width: 100%;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                text-align: center;
                padding: 15px 10px 2px;
                animation: reveal 0.8s ease-out both;
            }}

            .snap-logo {{
                width: 115px;
                height: 115px;
                object-fit: contain;
                border-radius: 15px;
                margin-bottom: 28px;
                transition: transform 0.3s ease;
            }}

            .snap-logo:hover {{
                transform: scale(1.06);
            }}

            .snap-title {{
                font-family: 'Climate Crisis', sans-serif;
                font-size: clamp(45px, 6vw, 68px);
                line-height: 1.05;
                letter-spacing: -2px;
                color: #F0F0FF ;
                margin: 0;
                text-align: center;
            }}

            .snap-subtitle {{
                font-family: 'Outfit', sans-serif;
                font-size: 20px;
                font-weight: 500;
                color: #E0E2FF;
                margin-top: 20px;
            }}

            @keyframes reveal {{
                from {{
                    opacity: 0;
                    transform: translateY(20px);
                }}
                to {{
                    opacity: 1;
                    transform: translateY(0);
                }}
            }}

            @media(max-width: 600px) {{
                .snap-logo {{
                    width: 90px;
                    height: 90px;
                }}

                .snap-title {{
                    font-size: 42px;
                }}

                .snap-subtitle {{
                    font-size: 16px;
                }}
            }}
        </style>
    </head>

    <body>
        <div class="snap-header">

            <img class="snap-logo"
                 src="data:image/jpeg;base64,{logo}"
                 alt="SnapClass Logo">

            <h1 class="snap-title">
                SNAP<br>CLASS
            </h1>

            <p class="snap-subtitle">
                Welcome to SnapClass
            </p>

        </div>
    </body>
    </html>
    """

    components.html(
        html_code,
        height=450,
        scrolling=False
    )



def header_layout_dashboard_login_teacher(page_title="Login with your Teacher Credentials"):

    style_base_layout()
    logo_path = Path(__file__).resolve().parents[1] / "Assets" / "logo.jpg"

    with open(logo_path, "rb") as image:
        logo = base64.b64encode(image.read()).decode("utf-8")

    # Centered dashboard header container
    _, main_col, _ = st.columns([1, 8, 1])

    with main_col:

        # =====================================
        # TOP ROW: LOGO + HOME BUTTON
        # =====================================

        logo_col, button_col = st.columns(
            [4,3],
            vertical_alignment="center"
        )

        with logo_col:

            html_logo = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <link href="https://fonts.googleapis.com/css2?family=Climate+Crisis&display=swap"
                      rel="stylesheet">

                <style>
                    * {{
                        box-sizing: border-box;
                    }}

                    body {{
                        margin: 0;
                        padding: 0;
                        background: transparent;
                    }}

                    .brand {{
                        display: flex;
                        align-items: center;
                        justify-content: flex-start;
                        gap: 15px;
                        height: 90px;
                    }}

                    .snap-logo {{
                        width: 85px;
                        height: 85px;
                        object-fit: contain;
                        border-radius: 16px;
                    }}

                    .snap-title {{
                        font-family: 'Climate Crisis', sans-serif;
                        font-size: 35px;
                        line-height: 0.95;
                        letter-spacing: -1px;
                        color: #5865F2;
                        margin: 0;
                    }}

                </style>
            </head>

            <body>
                <div class="brand">

                    <img
                        class="snap-logo"
                        src="data:image/jpeg;base64,{logo}"
                        alt="SnapClass Logo"
                    >

                    <h1 class="snap-title">
                        SNAP<br>CLASS
                    </h1>

                </div>
            </body>
            </html>
            """

            components.html(
                html_logo,
                height=95,
                scrolling=False
            )

        with button_col:

            if st.button(
                "Back Home",
                key="dashboardBack_home",
                type='secondary',
                use_container_width=True,
                shortcut="Ctrl+Backspace"
            ):
                st.session_state["login_type"] = None
                st.rerun()

        # =====================================
        # PAGE HEADING
        # =====================================

        html_heading = f"""
        <!DOCTYPE html>
        <html>
        <head>

            <link href="https://fonts.googleapis.com/css2?family=Climate+Crisis&display=swap"
                  rel="stylesheet">

            <style>
                body {{
                    margin: 0;
                    padding: 0;
                    background: transparent;
                }}

                .page-title {{
                    font-family: 'Climate Crisis', sans-serif;
                    font-size: clamp(27px, 3vw, 38px);
                    line-height: 1.2;
                    font-weight:300px !important;
                    letter-spacing: 1px;
                    color: #24243D;
                    text-align: center;
                    margin: 5px 0 0 0;
                    padding: 0;
                }}
            </style>

        </head>

        <body>
            <h2 class="page-title">{page_title}</h2>
        </body>
        </html>
        """

        components.html(
            html_heading,
            height=65,
            scrolling=False
        )


def header_layout_dashboard_register_teacher(page_title="Register with your Teacher Profile"):

    style_base_layout()
    logo_path = Path(__file__).resolve().parents[1] / "Assets" / "logo.jpg"

    with open(logo_path, "rb") as image:
        logo = base64.b64encode(image.read()).decode("utf-8")

    # Centered dashboard header container
    _, main_col, _ = st.columns([1, 8, 1])

    with main_col:

        # =====================================
        # TOP ROW: LOGO + HOME BUTTON
        # =====================================

        logo_col, button_col = st.columns(
            [4,3],
            vertical_alignment="center"
        )

        with logo_col:

            html_logo = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <link href="https://fonts.googleapis.com/css2?family=Climate+Crisis&display=swap"
                      rel="stylesheet">

                <style>
                    * {{
                        box-sizing: border-box;
                    }}

                    body {{
                        margin: 0;
                        padding: 0;
                        background: transparent;
                    }}

                    .brand {{
                        display: flex;
                        align-items: center;
                        justify-content: flex-start;
                        gap: 15px;
                        height: 90px;
                    }}

                    .snap-logo {{
                        width: 85px;
                        height: 85px;
                        object-fit: contain;
                        border-radius: 16px;
                    }}

                    .snap-title {{
                        font-family: 'Climate Crisis', sans-serif;
                        font-size: 35px;
                        line-height: 0.95;
                        letter-spacing: -1px;
                        color: #5865F2;
                        margin: 0;
                    }}

                </style>
            </head>

            <body>
                <div class="brand">

                    <img
                        class="snap-logo"
                        src="data:image/jpeg;base64,{logo}"
                        alt="SnapClass Logo"
                    >

                    <h1 class="snap-title">
                        SNAP<br>CLASS
                    </h1>

                </div>
            </body>
            </html>
            """

            components.html(
                html_logo,
                height=95,
                scrolling=False
            )

        with button_col:

            if st.button(
                "Back Home",
                key="dashboardBack_home",
                type='secondary',
                use_container_width=True,
                shortcut="Ctrl+Backspace"
            ):
                st.session_state["login_type"] = None
                st.rerun()

        # =====================================
        # PAGE HEADING
        # =====================================

        html_heading = f"""
        <!DOCTYPE html>
        <html>
        <head>

            <link href="https://fonts.googleapis.com/css2?family=Climate+Crisis&display=swap"
                  rel="stylesheet">

            <style>
                body {{
                    margin: 0;
                    padding: 0;
                    background: transparent;
                }}

                .page-title {{
                    font-family: 'Climate Crisis', sans-serif;
                    font-size: clamp(27px, 3vw, 38px);
                    line-height: 1.2;
                    font-weight:300px !important;
                    letter-spacing: 1px;
                    color: #24243D;
                    text-align: center;
                    margin: 5px 0 0 0;
                    padding: 0;
                }}
            </style>

        </head>

        <body>
            <h2 class="page-title">{page_title}</h2>
        </body>
        </html>
        """

        components.html(
            html_heading,
            height=65,
            scrolling=False
        )


def header_layout_dashboard_student_login(page_title="Login with Your Face ID"):

    style_base_layout()
    logo_path = Path(__file__).resolve().parents[1] / "Assets" / "logo.jpg"

    with open(logo_path, "rb") as image:
        logo = base64.b64encode(image.read()).decode("utf-8")

    # Centered dashboard header container
    _, main_col, _ = st.columns([1, 8, 1])

    with main_col:

        # =====================================
        # TOP ROW: LOGO + HOME BUTTON
        # =====================================

        logo_col, button_col = st.columns(
            [4,3],
            vertical_alignment="center"
        )

        with logo_col:

            html_logo = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <link href="https://fonts.googleapis.com/css2?family=Climate+Crisis&display=swap"
                      rel="stylesheet">

                <style>
                    * {{
                        box-sizing: border-box;
                    }}

                    body {{
                        margin: 0;
                        padding: 0;
                        background: transparent;
                    }}

                    .brand {{
                        display: flex;
                        align-items: center;
                        justify-content: flex-start;
                        gap: 15px;
                        height: 90px;
                    }}

                    .snap-logo {{
                        width: 85px;
                        height: 85px;
                        object-fit: contain;
                        border-radius: 16px;
                    }}

                    .snap-title {{
                        font-family: 'Climate Crisis', sans-serif;
                        font-size: 35px;
                        line-height: 0.95;
                        letter-spacing: -1px;
                        color: #5865F2;
                        margin: 0;
                    }}

                </style>
            </head>

            <body>
                <div class="brand">

                    <img
                        class="snap-logo"
                        src="data:image/jpeg;base64,{logo}"
                        alt="SnapClass Logo"
                    >

                    <h1 class="snap-title">
                        SNAP<br>CLASS
                    </h1>

                </div>
            </body>
            </html>
            """

            components.html(
                html_logo,
                height=95,
                scrolling=False
            )

        with button_col:

            if st.button(
                "Back Home",
                key="dashboardBack_home",
                type='secondary',
                use_container_width=True,
                shortcut="Ctrl+Backspace"
            ):
                st.session_state["login_type"] = None
                st.rerun()

        # =====================================
        # PAGE HEADING
        # =====================================

        html_heading = f"""
        <!DOCTYPE html>
        <html>
        <head>

            <link href="https://fonts.googleapis.com/css2?family=Climate+Crisis&display=swap"
                  rel="stylesheet">

            <style>
                body {{
                    margin: 0;
                    padding: 0;
                    background: transparent;
                }}

                .page-title {{
                    font-family: 'Climate Crisis', sans-serif;
                    font-size: clamp(27px, 3vw, 38px);
                    line-height: 1.2;
                    font-weight:300px !important;
                    letter-spacing: 1px;
                    color: #24243D;
                    text-align: center;
                    margin: 5px 0 0 0;
                    padding: 0;
                }}
            </style>

        </head>

        <body>
            <h2 class="page-title">{page_title}</h2>
        </body>
        </html>
        """

        components.html(
            html_heading,
            height=65,
            scrolling=False
        )

