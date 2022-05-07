import smtplib
from email.message import EmailMessage
import datetime as dt
import random

MY_EMAIL = "email.sender.py.smpt@gmail.com"
MY_PASSWORD = ""  # Create a sender email for you.

now = dt.datetime.now()
day_week = now.weekday()
if day_week == 1:
    with open("quotes.txt") as file:
        contents = file.readlines()
        quote = random.choice(contents)
        print(quote)

    msg = EmailMessage()
    msg['Subject'] = "Random Quote for your week"
    msg['From'] = "Marcos Gostoso 25"
    msg['To'] = ""  # TYPE A EMAIL TO SEND
    msg.set_content(quote)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.send_message(msg)
        connection.quit()
