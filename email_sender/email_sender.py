import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv

def send_emails():
    sender_email = "youremail@gmail.com"
    sender_password = "password"

    # Open recipient file
    with open('/path/ to /Phishingtool/email_sender/recipients.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if not row or len(row) == 0:
                continue
            recipient_email = row[0]
            subject = "Action Required: Suspicious Activity Detected"
            body = open('/path/ to /Phishingtool/email_sender/templates/fake_email_reset.html').read()

            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'html'))

            try:
                with smtplib.SMTP("smtp.gmail.com", 587) as server:
                    server.starttls()
                    server.login(sender_email, sender_password)
                    server.sendmail(sender_email, recipient_email, msg.as_string())
                    print(f"Email sent to {recipient_email}")
            except Exception as e:
                print(f"Failed to send email to {recipient_email}: {e}")

if __name__ == "__main__":
    send_emails()
