import random
import smtplib
import pandas
import datetime as dt

now = dt.datetime.now()
file = pandas.read_csv("birthdays.csv")
today = (now.month, now.day)
birthdays = {(data["month"], data["day"]): data for (index, data) in file.iterrows()}
if today in birthdays:
    person = birthdays[today]
    rand_file = random.randint(1, 3)
    with open(f"letter_templates/letter_{rand_file}.txt", "r") as data_file:
        letter = data_file.read()

        letter = letter.replace("[NAME]", person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:

        my_email = "test@gmail.com"
        password = "test124"
        smtp.starttls()
        smtp.login(my_email, password)
        smtp.sendmail(
            from_addr=my_email,
            to_addrs="my_email@gmail.com",
            msg=f"Subject:Happy Birthday \n\n{letter}"
        )
