#!/usr/bin/env python

'''
Author      : Jonathan Lurie
Email       : lurie.jo@gmail.com
Version     : 0.1
Licence     : MIT
description : Not writen yet

'''

import csv

def main():
    None


    with open('data/fre-daily-01012015-12312015.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            print ', '.join(row)




if __name__ == '__main__':
    main()
