#!/usr/bin/env python

'''
Author      : Jonathan Lurie
Email       : lurie.jo@gmail.com
Version     : 0.1
Licence     : MIT
description : Not writen yet

'''



def main():


    ## Open the file with read only permit
    f = open('codeclist.txt')
    ## Read the first line
    line = f.readline()

    ## If the file is not empty keep reading line one at a time
    ## till the file is empty
    while line:
        print line
        line = f.readline()

        try:
            if(line[2] == "E" and line[3] == "V" and line[6] == "S"):
                print line
        except:
            None




    f.close()



if __name__ == '__main__':
    main()
