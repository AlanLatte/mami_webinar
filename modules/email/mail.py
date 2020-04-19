import smtplib

smtpObj = smtplib.SMTP("smtp.gmail.com", 587)

smtpObj.starttls()

smtpObj.login("4.leo.makarov@gmail.com", "Ktyz2000ktyz")

smtpObj.sendmail("4.leo.makarov@gmail.com", "4.leo.makarov@gmail.com", "go to bed!")

smtpObj.quit()
