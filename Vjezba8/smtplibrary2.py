import smtplib
import datetime
import smtpd

content = 'Dobar dan profesore!!! Ivan Pelivan se javlja pomocu Pythona' 

mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()
mail.starttls()
mail.login('email', 'password')

mail.sendmail('pelivaniv@gmail.com', 'anteprojic@gmail.com', content)

mail.close()