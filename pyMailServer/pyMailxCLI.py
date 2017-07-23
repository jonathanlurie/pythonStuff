#!/usr/bin/env python

'''
Author      : Jonathan Lurie
Email       : lurie.jo@gmail.com
Version     : 0.1
Licence     : MIT
description : send a email using mailx command line tool and system call.
              It is the only way to send a email from a 1and1 server since
              SMTP is not available from within the server.

'''

import os
import os.path


def sendEmail(mailFrom, mailTo,  subject, message, fileToAttach = None, mailReplyTo = None):
    replyTo = mailFrom

    if(mailReplyTo):
        replyTo = mailReplyTo

    # sending a email with attachment
    if(fileToAttach):

        # only if attachment file is found
        if(os.path.isfile(fileToAttach)):
            cmd = "(echo -e '" + message + "'; uuencode " + fileToAttach + " " + fileToAttach + ") | mailx -aFrom:" + mailFrom + " -aReply-To:" + replyTo + " -s '" + subject + "' " + mailTo

        # no excpetion is raised, because we don't really care
        else:
            print("ERROR : attachment file does not exist, email will not be sent")

    # sending mail with no attachment
    else:
        cmd = "echo -e '" + message + "' | mailx -aFrom:" + mailFrom + " -aReply-To:" + replyTo + " -s '" + subject + "' " + mailTo

    #print(cmd)

    os.system(cmd)



if __name__ == '__main__':
    sendEmail("jonathan@tracklightmag.com", \
                "lurie.jo@gmail.com", \
                "this is the subject", \
                "Hello,\nHere is the message.\nBye.", \
                )
