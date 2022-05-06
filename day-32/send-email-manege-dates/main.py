import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = "O PAI TA ENVIANDO EMAIL PELO PYTHON, SIMPLESMENTE!"
msg['From'] = "Marcos Gostoso 25"
msg['To'] = "kleberreudo2017@gmail.com"
msg.set_content("Raa mlk, plmdds, master em python, APENAS!!\n To testando os tipos de email\n eh nois")


my_email = "email.sender.py.smpt@gmail.com"
password = ""
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
    connection.login(user=my_email, password=password)
    connection.send_message(msg)
    connection.quit()

