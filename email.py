# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

print("\n")

email = EmailMessage()
email["from"] = "APC"  # name of sender
email["to"] = "tawsifmasrur@gmail.com"  # email of the receiver
email["subject"] = "Python Project"  # subject of email

email.set_content(
    "Dear Tawsif,\n\nThis email is just one that I sent using Python code as a project trial run.\n\nBest Wishes,\nTawsif")  # email content

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # smtp.login(email_of_sender, password_of_sender)
    smtp.login("chowdhuryadittya09@gmail.com", "chowdhuryadittya09_09_09")
    smtp.send_message(email)
    print("sent successfully!")
