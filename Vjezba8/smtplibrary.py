import smtplib
import datetime
import smtpd

SERVER = 'localhost'
PORT = 1025

FROM = "ivan.pelivan@test.com"
TO = ["myemailaddress@something.com"]

SUBJECT = "test"

dt = datetime.datetime.now()
TEXT = "Ti si tako loca. @ " + str(dt)

message = """\
Salje: %s
Prima: %s
Predmet: %s

%s
""" % (FROM, ",".join(TO), SUBJECT, TEXT)

server = smtplib.SMTP(SERVER, PORT)
server.sendmail(FROM,TO,message)
server.quit()