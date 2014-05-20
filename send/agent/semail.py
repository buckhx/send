import smtplib
from email.mime.text import MIMEText

DEFAULT_SUBJECT_PREFIX = "[SEND] "

def send(message, conf):
    msg = MIMEText(message)
    msg['Subject'] = DEFAULT_SUBJECT_PREFIX + message[0:31] + "..."
    msg['From'] = conf['from']
    msg['To'] = conf['to']
    server = smtplib.SMTP(conf['server'])
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(conf['from'], conf['internal'])
    server.sendmail(msg['From'], [msg['To']], msg.as_string())
    server.close()
