from urllib import response

import mechanize

import os

import datetime

import sys

from time import sleep

browser = mechanize.Browser()

browser.set_handle_robots(False)

cookies = mechanize.CookieJar()

browser.set_cookiejar(cookies)

browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')]

browser.set_handle_refresh(False)

url = 'https://m.facebook.com/login.php'

def openlink(msg4):

    r = browser.open(msg4)

def aclass():

    browser.open(url)

    browser.select_form(nr = 0)

    browser.form['email'] = emailx

    browser.form['pass'] = pwx

    r = browser.submit()

    browser.select_form(nr = 0)

os.system('clear')

print ("""\033[0;92m 
──╔╗╔═══╗╔═══╗╔╗╔═╗╔═══╗╔═══╗╔═╗─╔╗ 
──║║║╔═╗║║╔═╗║║║║╔╝║╔═╗║║╔═╗║║║╚╗║║ 
──║║║║─║║║║─╚╝║╚╝╝─║╚══╗║║─║║║╔╗╚╝║ 
╔╗║║║╚═╝║║║─╔╗║╔╗║─╚══╗║║║─║║║║╚╗║║ 
║╚╝║║╔═╗║║╚═╝║║║║╚╗║╚═╝║║╚═╝║║║─║║║ 
╚══╝╚╝─╚╝╚═══╝╚╝╚═╝╚═══╝╚═══╝╚╝─╚═╝ 

                              
\033[0;91m 
╔══╗─╔═══╗╔═══╗╔═╗─╔╗╔═══╗ 
║╔╗║─║╔═╗║║╔═╗║║║╚╗║║╚╗╔╗║ 
║╚╝╚╗║╚═╝║║║─║║║╔╗╚╝║─║║║║ 
║╔═╗║║╔╗╔╝║╚═╝║║║╚╗║║─║║║║ 
║╚═╝║║║║╚╗║╔═╗║║║─║║║╔╝╚╝║ 
╚═══╝╚╝╚═╝╚╝─╚╝╚╝─╚═╝╚═══╝ 


 > \033[0;92mDEVELOPER     : J4CKS0N BR4ND
 > \033[0;95mFACEBOOK ID   : https://www.facebook.com/muhammad.khudaji
 > \033[0;41mWHATSAPP      : +923023767433
 \033[0;96m> JIG3RX       : J4CKS0N X ST4RC X M4RCUS <3
 > \033[0;97mWARNING       : DONT USE FOR ILLEGAL WORK     
\033[1;32m---------J4CKS0N X M4RCUS X ST4RC 0WNFIR3--------
""")



def poct(comment):

    browser.select_form(nr = 0)

    browser.form['comment_text'] = comment

    r = browser.submit()

print ("[-[ JUST CHILL B4BII3H THIS GAME IS MIN3 J4CKS0N XWD ]-]")

emailx=str(input("➣Enter email : "))

pwx =str(input("➣Enter pswrd : "))

aclass()

msg4=str(input("➣Enter post link : "))

msg5=str(input("➣File link dal lanti : "))

f=open(msg5, 'r')

lines = f.readlines()

f.close()

msg6= int(input("➣Enter TIME : "))

os.system('clear')

sys.stdout.flush()

print('kbaad v1.0')

count = 0

while True:

    for line in lines:

        if len(line) > 3:

            if count != 0:

                sleep(msg6)

            openlink(msg4)

            poct(line)

            print('YOUR P4P4 J4CKS0N XD - ', line)

            count += 1

            if count % 10 == 0:

                sleep(1)

                

                

                
 
