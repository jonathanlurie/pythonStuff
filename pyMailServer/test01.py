#!/usr/bin/env python

'''
Author      : Jonathan Lurie
Email       : lurie.jo@gmail.com
Version     : 0.1
Licence     : MIT
description : Send a email, based on a suggestion by Andrew Hare on StackOverflow
              http://stackoverflow.com/questions/882712/sending-html-email-using-python

'''

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def main():

    # me == my email address
    # you == recipient's email address
    me = "jonathan@tracklightmag.com"
    you = "lurie.jo@gmail.com"

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Link"
    msg['From'] = me
    msg['To'] = you

    # Create the body of the message (a plain-text and an HTML version).
    text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
    html = """\
    <html>
      <head></head>
      <body>
        <p>Hi!<br>
           How are you?<br>
           Here is the <a href="http://www.python.org">link</a> you wanted.
        </p>
      </body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)



    # Send the message via local SMTP server.
    #s = smtplib.SMTP('auth.smtp.1and1.fr', 587)
    s = smtplib.SMTP("smtp.1and1.com", 587)

    # mendatory if using port 587
    s.login(me, '')

    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(me, you, msg.as_string())
    s.quit()



if __name__ == '__main__':
    main()
