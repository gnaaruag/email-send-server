from fastapi import FastAPI
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import dotenv_values

config = dotenv_values(".env")

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/send-email")
def send_email():
    sender = config["sender"]
    recipient = config["reciever"]
    # customize subject
    subject = "Email Subject"
    
    body = "test email"
    
    """
    - You can also get the email content from an input file/template engine\ and parametrize it to customize email content.
    - generate an app password from your google account (will work only then)
    """
    
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, config["app_password"])  
        text = msg.as_string()
        server.sendmail(sender, recipient, text)
        server.quit()
        return {"message": "Email sent successfully!"}
    except Exception as e:
        return {"error": str(e)}

