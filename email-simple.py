import smtplib

# to send mails using gmail, turn ON 'less secure app access' from the account you're using to send mail with python
# ... using yahoo mail, profile logo -> account info -> account security -> login -> Generate and manage app passwords -> generate app password: then use the password as the sender_password to send mails using yahoo mail
sender_email = "chowdhuryadittya09@gmail.com"
sender_passwod = "chowdhuryadittya09_09_09"

receiver_email = "tawsifhaque97@yahoo.com"
receiver_password = ""  # not necesssary, unless used to send emails

# for sending mails using gmail, use the smtp location: smtp.gmail.com
# ... yahoo: smtp.mail.yahoo.com
# look up the others if needed
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=sender_email, password=sender_passwod)
    connection.sendmail(
        from_addr=sender_email,
        to_addrs=receiver_email,
        msg="Subject: Hey There!\n\nDear Receiver,\n\nThis mail is a sample mail sent using python code.\nLorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.\n\nBest Wishes,\nSender"
    )
print("\nmail sent successfully\n")
