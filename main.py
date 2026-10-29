# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

birthday_messages = []

def messages():
    with open("letter_templates/letter_1.txt") as file:
        data1 = file.read()
        birthday_messages.append(data1)
    with open("letter_templates/letter_2.txt") as file:
        data2 = file.read()
        birthday_messages.append(data2)
    with open("letter_templates/letter_3.txt") as file:
        data3 = file.read()
        birthday_messages.append(data3)
    
    message = random.choice(birthday_messages)
    letter = message.replace("[NAME]", name)
    
    return letter

def send_email(letter, recipient):

    with smtplib.SMTP("smtp.gmail.com", 587, timeout=20) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=recipient, msg=f"Subject: Happy Birthday\n\n{letter}")
    print(f"Message sent successfully to {name}")

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
time_now = dt.datetime.now()

current_month  = time_now.month
current_day = time_now.day

for _, person in data.iterrows():
    name = person["name"]
    email = person["email"]
    month = int(person["month"])
    day = int(person["day"])
    
    if current_day == day and current_month == month:
        message_compose = messages()
        send_email(message_compose, email)
        
