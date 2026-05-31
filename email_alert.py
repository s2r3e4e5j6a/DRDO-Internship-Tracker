import smtplib
sender_email = "sreejagurrala23@gmail.com"
sender_password = "jluyhxnxphzbqput"

receiver_email = "sreejagurrala23@gmail.com"

message = """
Subject: DRDO Internship Report

DRDO Internship Tracker Report

Open Internships:
1. DRDL - Hyderabad
2. MTRDC - Bengaluru
3. SAC - Ahmedabad
4. BARC Training School - Mumbai

Generated Automatically.
"""
server = smtplib.SMTP(
    "smtp.gmail.com",
    587
)

server.starttls()

server.login(
    sender_email,
    sender_password
)

server.sendmail(
    sender_email,
    receiver_email,
    message
)

server.quit()

print("Email Sent Successfully")