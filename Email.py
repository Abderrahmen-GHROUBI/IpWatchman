"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, message, from_email, to_email, smtp_server, smtp_port, smtp_user, smtp_password):
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

   
    msg.attach(MIMEText(message, 'plain'))

    
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls() 
        server.login(smtp_user, smtp_password)  

       
        server.send_message(msg)


subject = ""
message = ""
from_email = ""
to_email = ""
smtp_server = ""
smtp_port = 587
smtp_user = "votre_adresse_email@gmail.com"
smtp_password = "votre_mot_de_passe"

send_email(subject, message, from_email, to_email, smtp_server, smtp_port, smtp_user, smtp_password)
"""
