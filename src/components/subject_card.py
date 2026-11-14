import streamlit as st
from html import escape


def subject_card(name, code, section, stats=None, footer_callback=None):

    stats = stats or []

    safe_name = escape(str(name))
    safe_code = escape(str(code))
    safe_section = escape(str(section))

    html = f"""
    <style>
        .snap-subject-card {{
            background: linear-gradient(145deg, #FFFFFF, #F8F7FF);
            border: 1px solid #E8E5F5;
            border-left: 7px solid #EB459E;
            border-radius: 20px;
            padding: 24px;
            margin: 12px 0;
            box-shadow: 0 5px 18px rgba(36, 36, 61, 0.07);
            transition: all 0.3s ease;
            font-family: 'Outfit', sans-serif;
        }}

        .snap-subject-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 12px 28px rgba(88, 101, 242, 0.15);
            border-left-color: #5865F2;
        }}

        .subject-card-top {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 18px;
        }}

        .subject-card-icon {{
            width: 48px;
            height: 48px;
            display: flex;
            justify-content: center;
            align-items: center;
            border-radius: 15px;
            background: linear-gradient(135deg, #E8E9FF, #FCE4F1);
            font-size: 24px;
        }}

        .subject-card-badge {{
            background: #EEEFFF;
            color: #5865F2;
            padding: 7px 13px;
            border-radius: 30px;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 1px;
        }}

        .subject-card-name {{
            color: #24243D;
            font-size: 23px;
            font-weight: 750;
            line-height: 1.3;
            margin: 0 0 10px 0;
            overflow-wrap: anywhere;
        }}

        .subject-card-meta {{
            color: #77758C;
            font-size: 13px;
            margin-bottom: 20px;
        }}

        .subject-card-meta span {{
            color: #D653A0;
            font-weight: 700;
        }}

        .subject-card-stats {{
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 12px;
            border-top: 1px solid #EAE7F2;
            padding-top: 17px;
        }}

        .subject-stat {{
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 13px;
            background: #F3F2FC;
            border-radius: 13px;
            min-width: 0;
        }}

        .subject-stat-icon {{
            font-size: 22px;
        }}

        .subject-stat-value {{
            color: #24243D;
            font-size: 19px;
            font-weight: 750;
        }}

        .subject-stat-label {{
            color: #858398;
            font-size: 11px;
            margin-top: 2px;
        }}

        @media(max-width: 500px) {{
            .subject-card-stats {{
                grid-template-columns: 1fr;
            }}

            .subject-card-name {{
                font-size: 19px;
            }}
        }}
    </style>

    <div class="snap-subject-card">

        <div class="subject-card-top">
            <div class="subject-card-icon">📚</div>
            <div class="subject-card-badge">SNAPCLASS</div>
        </div>

        <h3 class="subject-card-name">{safe_name}</h3>

        <div class="subject-card-meta">
            Code: <span>{safe_code}</span>
            &nbsp; | &nbsp;
            Section: <span>{safe_section}</span>
        </div>

        <div class="subject-card-stats">
    """

    for icon, label, value in stats:

        html += f"""
            <div class="subject-stat">
                <div class="subject-stat-icon">{escape(str(icon))}</div>
                <div>
                    <div class="subject-stat-value">{escape(str(value))}</div>
                    <div class="subject-stat-label">{escape(str(label))}</div>
                </div>
            </div>
        """

    html += """
        </div>
    </div>
    """

    st.html(html)

    if footer_callback:
        footer_callback()
