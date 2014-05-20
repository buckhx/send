import smtplib
from email.mime.text import MIMEText

DEFAULT_SUBJECT_PREFIX = "[SEND] "

def send(msg, conf):
    msg = MIMEText(msg)
    msg['Subject'] = DEFAULT_SUBJECT_PREFIX + str(msg[0:31]) + "..."
    msg['From'] = conf['from']
    msg['To'] = conf['to']
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(conf['from'], conf['pass'])
    server = smtplib.SMTP(conf['server'])
    server.sendmail(msg['From'], [msg['To']], msg.as_string())
    server.close()
