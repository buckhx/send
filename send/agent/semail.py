import os
import smtplib
from email.mime.text import MIMEText

DEFAULT_SUBJECT_PREFIX = "[SEND] "

def send(fname, conf):
    contents = open(fname).read()
    msg = MIMEText(contents)
    msg['Subject'] = DEFAULT_SUBJECT_PREFIX + os.path.basename(fname) + "..."
    msg['From'] = conf['from']
    msg['To'] = conf['to']
    server = smtplib.SMTP(conf['server'])
    server.ehlo()
    server.starttls()
    server.ehlo()
    try:
        server.login(conf['from'], conf['internal'])
        server.sendmail(msg['From'], [msg['To']], msg.as_string())
    except smtplib.SMTPAuthenticationError:
        print "[ERROR] Email Authentication"
    server.close()
