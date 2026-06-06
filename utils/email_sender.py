import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(subject, body):

    sender_email = "sreejagurrala23@gmail.com"

    sender_password = "jluy hxnx phzb qput"

    receiver_email = "sreejagurrala23@gmail.com"

    try:

        message = MIMEMultipart()

        message["From"] = sender_email

        message["To"] = receiver_email

        message["Subject"] = subject

        message.attach(
            MIMEText(
                body,
                "plain"
            )
        )

        server = smtplib.SMTP(
            "smtp.gmail.com",
            587
        )

        server.starttls()

        print(
            "Connecting to Gmail..."
        )

        server.login(
            sender_email,
            sender_password
        )

        server.sendmail(
            sender_email,
            receiver_email,
            message.as_string()
        )

        server.quit()

        print(
            "✅ Email Sent Successfully"
        )

        return True

    except Exception as e:

        print(
            f"❌ Email Error: {e}"
        )

        return False