import smtplib
from email.message import EmailMessage

def send_email(report_path, sender, password, receiver):
    msg = EmailMessage()
    msg["Subject"] = "Automation Report"
    msg["From"] = sender
    msg["To"] = receiver

    msg.set_content("Attached is your automation report.")

    with open(report_path, "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename="report.txt")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)

    print("Email sent!")