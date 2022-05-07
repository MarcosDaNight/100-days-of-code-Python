import pandas
from datetime import datetime
import random
from email.message import EmailMessage
import smtplib

MY_EMAIL = "email.sender.py.smpt@gmail.com"
MY_PASSWORD = ""


def generate_msg(recipient_email, sender, content):
    msg = EmailMessage()
    msg['Subject'] = "Birthday wishes!"
    msg['From'] = sender
    msg['To'] = recipient_email
    msg.set_content(content)
    return msg


data = pandas.read_csv("birthdays.csv")
email = data.email[2]
name = data.name[2]
year = data.year[2]
month = data.month[2]
day = data.day[2]

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
today_tuple = (datetime.now().month, datetime.now().day)

if today_tuple in birthdays_dict:
    birthdays_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as file:
        contents = file.read()
        contents = contents.replace("[NAME]", birthdays_person["name"])
        msg = generate_msg("marcos.cosson@ccc.ufcg.edu.br", "Marcos", contents)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.send_message(msg)
            connection.quit()

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name
# from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
