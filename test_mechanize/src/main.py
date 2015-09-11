
#!/usr/bin/env python

# Search PyPI, the Python Package Index, and retrieve latest mechanize tarball.

# This is just to demonstrate mechanize: You should use easy_install to do
# this, not this silly script.

import sys
import os
import urlparse

import mechanize


def download_mechanize():
    browser = mechanize.Browser(factory=mechanize.RobustFactory())
    browser.set_handle_robots(False)

    browser.open("http://pypi.python.org/pypi")
    browser.follow_link(text="Package Index", nr=0)
    browser.select_form(name="searchform")
    browser.form["term"] = "mechanize"
    browser.submit()
    browser.follow_link(text_regex="mechanize-?(.*)")
    link = browser.find_link(text_regex=r"\.tar\.gz")

    print link

    filename = os.path.basename(urlparse.urlsplit(link.url)[2])
    if os.path.exists(filename):
        sys.exit("%s already exists, not grabbing" % filename)
    browser.retrieve(link.url, filename)

def download_kml():

    browser = mechanize.Browser(factory=mechanize.RobustFactory())
    browser.set_handle_robots(False)

    '''

    browser.open("https://accounts.google.com/ServiceLogin")
    #browser.follow_link(text="Package Index", nr=0)
    browser.select_form(name="gaia_loginform")
    browser.form["Email"] = "lurie.jo@gmail.com"
    browser.form["Passwd"] = "jo.270185jo"
    browser.submit()
'''
    link = "https://maps.google.fr/locationhistory/b/0/kml?startTime=1424300400000&endTime=1424386800000"
    browser.retrieve(link, "trajet.kml")




def connectTry():

    import urllib
    import urllib2
    import getpass
    import re

    email = raw_input("Enter your Google username: ")
    password = getpass.getpass("Enter your password: ")

    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    urllib2.install_opener(opener)

    # Define URLs
    loing_page_url = 'https://www.google.com/accounts/ServiceLogin'
    authenticate_url = 'https://www.google.com/accounts/ServiceLoginAuth'
    gv_home_page_url = 'https://www.google.com/voice/#inbox'

    # Load sign in page
    login_page_contents = opener.open(loing_page_url).read()

    # Find GALX value
    galx_match_obj = re.search(r'name="GALX"\s*value="([^"]+)"', login_page_contents, re.IGNORECASE)

    galx_value = galx_match_obj.group(1) if galx_match_obj.group(1) is not None else ''

    # Set up login credentials
    login_params = urllib.urlencode( {
       'Email' : email,
       'Passwd' : password,
       'continue' : 'https://www.google.com/voice/account/signin',
       'GALX': galx_value
    })

    # Login
    opener.open(authenticate_url, login_params)

    # Open GV home page
    gv_home_page_contents = opener.open(gv_home_page_url).read()

    # Fine _rnr_se value
    key = re.search('name="_rnr_se".*?value="(.*?)"', gv_home_page_contents)

    if not key:
       logged_in = False
       print 'Failed!'
    else:
       logged_in = True
       key = key.group(1)
       print 'Success!'

if __name__ == "__main__":
    #download_mechanize()
    #download_kml()
    connectTry()
