import smtplib


my_email = "ajaysajikumartest@gmail.com"
password = "8LgqjMbZDAd#tM%"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user= my_email, password= password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="ajaysajikumartest@yahoo.com", 
        msg="Subject:Hey there\n\nHope you are having a good day!"
    )
