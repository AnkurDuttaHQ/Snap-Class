
import streamlit as st
import segno
import io
import smtplib

from urllib.parse import quote
from email.message import EmailMessage
from email.utils import parseaddr


@st.dialog("Share Subject Invitation", width=900)
def share_subject_dialog(subject_name, subject_code):

    # --------------------------------
    # APPLICATION URL
    # --------------------------------

    app_domain = "http://localhost:8501"

    join_url = (
        f"{app_domain.rstrip('/')}/?join-code="
        f"{quote(str(subject_code))}"
    )

    # --------------------------------
    # INVITATION MESSAGE
    # --------------------------------

    message = f"""Hello!

You are invited to join my SnapClass subject.

Subject: {subject_name}
Subject Code: {subject_code}

Join SnapClass here:
{join_url}

You can also scan the attached QR code to join.

Regards,
SnapClass
"""

    # --------------------------------
    # WHATSAPP LINK
    # --------------------------------

    whatsapp_url = (
        f"https://wa.me/?text={quote(message)}"
    )

    # --------------------------------
    # GENERATE QR CODE
    # --------------------------------

    qr = segno.make(join_url)

    qr_buffer = io.BytesIO()

    qr.save(
        qr_buffer,
        kind="png",
        scale=5,
        border=2
    )

    qr_bytes = qr_buffer.getvalue()

    # --------------------------------
    # COMPACT RESPONSIVE STYLING
    # --------------------------------

    st.html("""
    <style>

        div[data-testid="stDialog"] [role="dialog"] {
            padding: 1.2rem !important;
            max-width: 900px !important;
        }

        div[data-testid="stDialog"] h3 {
            font-size: 17px !important;
            margin-bottom: 9px !important;
            color: #24243D !important;
        }

        div[data-testid="stDialog"] h2 {
            font-size: 20px !important;
        }

        div[data-testid="stDialog"] pre {
            padding: 9px 11px !important;
            font-size: 12px !important;
            border-radius: 9px !important;
        }

        div[data-testid="stDialog"] button {
            min-height: 37px !important;
            border-radius: 9px !important;
            font-size: 13px !important;
        }

        div[data-testid="stDialog"] textarea {
            min-height: 65px !important;
            font-size: 13px !important;
            border-radius: 9px !important;
        }

        .snap-qr-card {
            background: #F8F7FC;
            border: 1px solid #ECE9F5;
            border-radius: 15px;
            padding: 15px 8px;
            text-align: center;
        }

        .snap-qr-caption {
            font-size: 11px;
            color: #858398;
            margin-top: 8px;
        }

    </style>
    """)

    # --------------------------------
    # MAIN LAYOUT
    # --------------------------------

    col1, col2 = st.columns(
        [1.4, 0.6],
        gap="medium",
        vertical_alignment="center"
    )

    # --------------------------------
    # LEFT SECTION
    # --------------------------------

    with col1:

        st.markdown("### Copy Invitation")

        st.code(
            join_url,
            language="text"
        )

        st.code(
            str(subject_code),
            language="text"
        )

        st.info(
            f"Invite students to join {subject_name}."
        )

        # --------------------------------
        # WHATSAPP SHARING
        # --------------------------------

        st.markdown("### 🟢 WhatsApp Invitation")

        st.download_button(
            label="📥 Download QR Code",
            data=qr_bytes,
            file_name=f"{subject_code}_QR.png",
            mime="image/png",
            width="stretch",
            key=f"download_qr_{subject_code}"
        )

        st.link_button(
            "🟢 Open WhatsApp",
            whatsapp_url,
            width="stretch"
        )

        st.caption(
            "Download the QR image first, then open WhatsApp, "
            "attach the image and send the invitation."
        )

        st.divider()

        # --------------------------------
        # EMAIL WITH QR ATTACHMENT
        # --------------------------------

        st.markdown("### 📧 Email with QR Code")

        with st.form(
            key=f"snapclass_email_form_{subject_code}"
        ):

            recipient_emails = st.text_area(
                "Student Email Addresses",
                placeholder=(
                    "student1@gmail.com, student2@gmail.com"
                ),
                help="Separate multiple email addresses with commas.",
                height=65
            )

            send_email = st.form_submit_button(
                "Send Invitation",
                type="primary",
                width="stretch"
            )

            if send_email:

                # Validate email addresses
                recipients = [
                    email.strip()
                    for email in recipient_emails.split(",")
                    if email.strip()
                ]

                valid_recipients = []

                for email in recipients:

                    parsed_email = parseaddr(email)[1]

                    if (
                        parsed_email == email
                        and "@" in email
                        and "." in email.rsplit("@", 1)[-1]
                    ):
                        valid_recipients.append(email)

                if not valid_recipients:

                    st.error(
                        "Please enter valid student email addresses."
                    )

                else:

                    try:

                        sender = st.secrets["email"]["sender"]

                        app_password = (
                            st.secrets["email"]["app_password"]
                        )

                        sent_count = 0

                        with st.spinner(
                            "Sending invitations..."
                        ):

                            with smtplib.SMTP_SSL(
                                "smtp.gmail.com",
                                465,
                                timeout=30
                            ) as smtp:

                                smtp.login(
                                    sender,
                                    app_password
                                )

                                for recipient in valid_recipients:

                                    email_msg = EmailMessage()

                                    email_msg["Subject"] = (
                                        f"Join SnapClass - {subject_name}"
                                    )

                                    email_msg["From"] = sender
                                    email_msg["To"] = recipient

                                    email_msg.set_content(message)

                                    # Attach QR image
                                    email_msg.add_attachment(
                                        qr_bytes,
                                        maintype="image",
                                        subtype="png",
                                        filename=f"{subject_code}_QR.png"
                                    )

                                    smtp.send_message(email_msg)

                                    sent_count += 1

                        st.success(
                            f"Invitation successfully sent to "
                            f"{sent_count} student(s)!"
                        )

                    except Exception as e:

                        st.error(
                            f"Email sending failed: {str(e)}"
                        )

    # --------------------------------
    # RIGHT SECTION - QR CODE
    # --------------------------------

    with col2:

        st.markdown("### Scan to join")

        st.html("""
        <style>
            .snap-qr-caption {
                font-size: 11px;
                color: #858398;
                text-align: center;
                margin-top: 8px;
            }
        </style>
        """)

        with st.container(
            border=True,
            key="snapclass_qr_preview"
        ):

            st.image(
                qr_bytes,
                width=140
            )

            st.markdown(
                '<p class="snap-qr-caption">'
                'Scan to join the subject'
                '</p>',
                unsafe_allow_html=True
            )

        st.caption(
            f"Subject: {subject_code}"
        )
