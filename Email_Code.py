import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, body):
    # Set up the SMTP server
    smtp_server = "smtp.example.com"  # Replace with your SMTP server
    smtp_port = 587  # Replace with the appropriate SMTP port for your server

    try:
        # Create a MIMEText object for the email body
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Establish the SMTP connection and login to the server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")

        # Close the connection
        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")

# Usage example
sender_email = "your_email@example.com"
sender_password = "your_email_password"
receiver_email = "recipient@example.com"
subject = "Test Email"
body = "This is a test email sent from Python."

send_email(sender_email, sender_password, receiver_email, subject, body)
