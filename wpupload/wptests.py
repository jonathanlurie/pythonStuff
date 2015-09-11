#!/usr/bin/env python

'''
Author      : Jonathan Lurie
Email       : lurie.jo@gmail.com
Version     : 0.1
Licence     : MIT
description : Not writen yet

'''

import sys
import os

from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods import posts


def main():
    client = Client('http://jonathanlurie.fr/xmlrpc.php', 'jonathanlurie', 'jo.270185')

    allPosts = client.call(posts.GetPosts())

    for p in allPosts:
        try:
            print p
        except:
            None



if __name__ == '__main__':
    main()
