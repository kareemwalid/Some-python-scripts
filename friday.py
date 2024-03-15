import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time
from datetime import datetime

def send_email(sender_email,sender_password,receiver_email,subject,message):
    smtp_server = smtplib.SMTP('smtp.gmail.com',587)
    smtp_server.starttls()
    smtp_server.login(sender_email,sender_password)
    email_message = MIMEMultipart()
    email_message['From'] = sender_email
    email_message['To'] = receiver_email
    email_message['Subject'] = subject
    email_message.attach(MIMEText(message,'plain'))
    smtp_server.send_message(email_message)
    smtp_server.quit()
def send_email_content():
    sender_email = 'email@gmail.com'
    sender_password = 'password'
    receiver_email = 'email@gmail.com'
    subject = 'mtnsa4 td3y elnahrda elgom3a :)'
    message = 'yalla ed3y ya kareem w hgylk kman sa3a'
    send_email(sender_email,sender_password,receiver_email,subject,message)
def is_friday():
    return datetime.now().weekday() == 4  
if is_friday():
    schedule.every().hour.do(send_email_content)
while is_friday():
    schedule.run_pending()
    time.sleep(1)
