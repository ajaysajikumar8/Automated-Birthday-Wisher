import datetime as dt
import pandas
import random
import smtplib

EMAIL = "ajaysajikumartest@gmail.com"
PASSWORD = "8LgqjMbZDAd#tM%"

current_month = dt.datetime.now().month
current_day = dt.datetime.now().day

today = (current_month, current_day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]) : data_row for (index,data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as file:
        content = file.read()
        content.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL, 
            to_addrs=birthday_person["email"], 
            msg=f"Subject: Happy Birthday\n\n{content}")


