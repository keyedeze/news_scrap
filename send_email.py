import smtplib, ssl
import os
from dotenv import load_dotenv, find_dotenv


def send_email(message):
    load_dotenv(find_dotenv())

    host = "smtp.gmail.com"
    port = 465
    username = os.getenv("SENDMAIL")
    password = os.getenv("PASSWOR")
    receiver = os.getenv("MYMAIL")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

