from fastapi import FastAPI
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/send-email")
def send_email():
    sender = "gaurang40304@gmail.com"
    recipient = "lumosnox1104@gmail.com"
    subject = "Water Reminder"
    body_options = [
        "Drink water :) \n ily",
        "Daisy Vyas, Water, NOW! \n ily",
        "Paani peelo madam ji 🙏🏻. \n ily"
        "Be a hydro homie \n ily :)",
        "Don't forget to drink water! \n ily",
        "Drink water, you thirsty hoe \n ily",
        "Drink water, ily :) \n ily",
        "Drink up princess \n ily"
        
    ]
    body = random.choice(body_options)
    
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, "rqst uphw fhkt crho")  # Use app-specific password if needed
        text = msg.as_string()
        server.sendmail(sender, recipient, text)
        server.quit()
        return {"message": "Email sent successfully!"}
    except Exception as e:
        return {"error": str(e)}

