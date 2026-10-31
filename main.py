# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import datetime as dt
import pandas
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

birthday_messages = []

def messages(names):
    for number in range(1, 4):
        with open(f"letter_templates/letter_{number}.txt") as file:
            birthday_messages.append(file.read())
    
    message = random.choice(birthday_messages)
    letter = message.replace("[NAME]", names)
    
    return letter

def send_email(letter, recipient):

    with smtplib.SMTP("smtp.gmail.com", 587, timeout=20) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=recipient, msg=f"Subject: Happy Birthday\n\n{letter}")
    print(f"Message sent successfully to {recipient}")

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
        message_compose = messages(names)
        send_email(message_compose, email)
        
