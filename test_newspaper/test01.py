#!/usr/bin/env python

'''
Author      : Jonathan Lurie
Email       : lurie.jo@gmail.com
Version     : 0.1
Licence     : MIT
description : Not writen yet

'''
from newspaper import Article


def main():
    url = u'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones'
    article = Article(url)

    article.download()

    html = article.html
    #print html

    print(article.authors)
    print(article.publish_date)
    print(article.text)
    print(article.top_image)




if __name__ == '__main__':
    main()
