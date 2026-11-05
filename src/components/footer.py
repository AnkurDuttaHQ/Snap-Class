
import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime


def footer_layout():

    current_year = datetime.now().year

    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&display=swap"
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

            .footer {{
                width: 100%;
                text-align: center;
                padding: 20px 10px;
                font-family: 'Outfit', sans-serif;
                animation: reveal 0.8s ease both;
            }}

            .divider {{
                width: 65px;
                height: 3px;
                background: linear-gradient(
                    90deg, #EB459E, #A855F7, #EB459E
                );
                border-radius: 20px;
                margin: 0 auto 15px;
            }}

            .footer-text {{
                color: #292536;
                font-size: 15px;
                font-weight: 500;
                margin: 5px 0;
            }}

            .brand {{
                display: inline-block;
                font-size: 18px;
                font-weight: 800;
                background: linear-gradient(
                    90deg, #A83278, #6C3CCB, #A83278
                );
                background-size: 200% auto;
                background-clip: text;
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                transition: background-position 0.5s ease;
            }}

            .brand:hover {{
                background-position: right center;
            }}

            .heart {{
                display: inline-block;
                color: #E83E91;
                animation: heartbeat 1.4s ease-in-out infinite;
            }}

            .copyright {{
                color: #625B70;
                font-size: 12px;
                margin-top: 10px;
                letter-spacing: 0.4px;
            }}

            @keyframes heartbeat {{
                0%, 100% {{ transform: scale(1); }}
                50% {{ transform: scale(1.25); }}
            }}

            @keyframes reveal {{
                from {{
                    opacity: 0;
                    transform: translateY(12px);
                }}
                to {{
                    opacity: 1;
                    transform: translateY(0);
                }}
            }}

            @media (prefers-reduced-motion: reduce) {{
                .footer, .heart {{
                    animation: none !important;
                }}
            }}
        </style>
    </head>

    <body>
        <div class="footer">

            <div class="divider"></div>

            <p class="footer-text">
                Crafted with
                <span class="heart">♥</span>
                by
                <span class="brand">Ankurdev</span>
            </p>

            <p class="copyright">
                © {current_year} SnapClass. All rights reserved.
            </p>

        </div>
    </body>
    </html>
    """

    components.html(
        html_code,
        height=105,
        scrolling=False
    )
