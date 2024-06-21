import os
import smtplib, ssl
from email.mime.text import MIMEText
from typing import List


def send_email(receiver_emails: List[str], html_message: str):

    SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
    SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD")

    if not (SENDER_EMAIL and SENDER_PASSWORD):
        return

    if not receiver_emails:
        return

    server = smtplib.SMTP(host="smtp.gmail.com", port=587)
    server.starttls(context=ssl.create_default_context())
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.sendmail(SENDER_EMAIL, receiver_emails, msg=MIMEText(html_message, "html").as_string())
    server.quit()
