#!/usr/bin/env python

'''
Author      : Jonathan Lurie
Email       : lurie.jo@gmail.com
Version     : 0.1
Licence     : MIT
description : Send a email using python. Based on
              https://flenniken.net/blog/send-email-using-python-and-1and1/

'''
import smtplib
from email.mime.text import MIMEText

def sendMailRegular():
    me = "hello@tracklightmag.com"
    you = "lurie.jo@gmail.com"
    password = "jo270185"
    msg = MIMEText("This is a test message body.")
    msg['Subject'] = 'Test message'
    msg['From'] = me
    msg['To'] = you
    session = smtplib.SMTP("smtp.1and1.com", 587)
    session.login(me, password)
    session.sendmail(me, you, msg.as_string())
    session.quit()

def sendMail1and1():
    import os
    mail_to = "lurie.jo@gmail.com"
    mail_from = "hello@tracklightmag.com"
    subject = "test message 1and1 style"
    header = """From: {0}
    To: {1}
    Subject: {2}
    """.format(mail_from, mail_to, subject)
    msg = header + "a test from me"
    sendmail = os.popen("/usr/lib/sendmail -t", "w")
    sendmail.write(msg)
    sendmail.close()

    #echo "Test" | mail -s Test lurie.jo@gmail.com
    #mail -aFrom:jonathan@tracklightmag.com  -s "le sujet du mail" lurie.jo@gmail.com < orderlist/1.txt
    #mail -aFrom:jonathan@tracklightmag.com -aReply-To:hello@tracklightmag.com  -s "le sujet du mail" lurie.jo@gmail.com < orderlist/1.txt

    (cat orderlist/1_message.txt ; uuencode orderlist/1_order.csv orderlist/1_order.csv) | mailx -aFrom:jonathan@tracklightmag.com -aReply-To:hello@tracklightmag.com  -s "le sujet du mail 3" lurie.jo@gmail.com


    cmd = "(cat " + mainTextFile + "; uuencode " + attachementFile + " " + attachementFile + ") | mailx -aFrom:" + mailFrom + " -aReply-To:" + replyTo + " -s '" + subject + "' " + mailTo



if __name__ == '__main__':
    sendMail1and1()
