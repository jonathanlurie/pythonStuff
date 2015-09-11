#!/usr/bin/env python

'''
Author      : Jonathan Lurie
Email       : lurie.jo@gmail.com
Version     : 0.1
Licence     : MIT
description : Upload jpg images to a wordpress blog.
              First arg is the folder that must contain jpg images

'''

import sys
import os

from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts

import glob

def main():

    if(len(sys.argv)  != 2 ):
        print("ERROR : missing argument. A folder path is needed.")
        exit()

    folder = sys.argv[1]
    allJpgs = sorted(glob.glob(folder + os.sep + "*.[jJ][pP][gG]"))

    if(len(allJpgs) == 0):
        print("INFO : no jpg file were found there.")
        exit()

    client = Client('http://jonathanlurie.fr/xmlrpc.php', 'jonathanlurie', 'jo.270185')

    print("Uploading...\n")

    for f in allJpgs:
        # prepare metadata
        data = {
                'name': f,
                'type': 'image/jpeg',  # mimetype
        }

        # read the binary file and let the XMLRPC library encode it into base64
        with open(f, 'rb') as img:
                data['bits'] = xmlrpc_client.Binary(img.read())

        response = client.call(media.UploadFile(data))
        # response == {
        #       'id': 6,
        #       'file': 'picture.jpg'
        #       'url': 'http://www.example.com/wp-content/uploads/2012/04/16/picture.jpg',
        #       'type': 'image/jpeg',
        # }

        print response['url']

    print("\nDone.")





if __name__ == '__main__':
    main()
