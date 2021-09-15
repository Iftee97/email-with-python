import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

print("\n")

# gives access to index.html file
html = Template(Path("index.html").read_text())

email = EmailMessage()
email["from"] = "APC"
email["to"] = "tawsifmasrur@gmail.com"
email["subject"] = "Python Project"

email.set_content(html.substitute({"name": "Tawsif Masur Haque"}), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # smtp.login(email_of_sender, password_of_sender)
    smtp.login("chowdhuryadittya09@gmail.com", "chowdhuryadittya09_09_09")
    smtp.send_message(email)
    print("sent successfully!")
