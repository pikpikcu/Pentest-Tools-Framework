#!/use/bin/python

import sys, urllib2, re, time, httplib, random

BAD_RESP = [400,401,404]

def main(path):
    print "[+] Testing:",host.split("/",1)[1]+path
    try:
        dzx = httplib.HTTP(host.split("/",1)[0])
        dzx.putrequest("HEAD", "/"+host.split("/",1)[1]+path)
        dzx.putheader("Host", host.split("/",1)[0])
        dzx.endheaders()
        resp, reason, headers = dzx.getreply()
        return resp, reason, headers.get("Server")
    except(), msg: 
        print "Error :",msg
        pass

def timer():
    now = time.localtime(time.time())
    return time.asctime(now)


print '''		        
'''

dz4ever = {"/index.php?option=com_hdflvplayer&id=1'" : ["Joomla HD FLV SQL ","http://www.exploit-db.com/exploits/35220/"],
"/components/com_hdflvplayer/hdflvplayer/download.php" : ["Joomla HD FLV File Download Vulnerability","http://www.exploit-db.com/exploits/35246/"],
"/backups/" : ["backup Plugin ","http://www.exploit-db.com/exploits/35212/"],
"/wp-content/plugins/sexy-contact-form/includes/fileupload/index.php" : ["Wordpress and Joomla Creative Contact Form Shell Upload Vulnerability","http://www.exploit-db.com/exploits/35057/"],
"/index.php?option=com_formmaker&view=formmaker&id=1'" : ["Joomla Spider Form Maker 3.4 SQL ","http://www.exploit-db.com/exploits/34637/"],
"/index.php?option=com_facegallery&task=imageDownload&img_name=" : ["Joomla Face Gallery 1.0 Multiple Vulnerabilities","http://www.exploit-db.com/exploits/34754/"],
"/index.php?option=com_macgallery&view=download&albumid=" : ["Joomla Mac Gallery 1.5 Arbitrary File Download","http://www.exploit-db.com/exploits/34755/"],
"/index.php?option=com_spidercontacts&contact_id=1'" : ["Joomla Spider Contacts 1.3.6 SQL  ","http://www.exploit-db.com/exploits/34625/"],
"/index.php?option=com_spidercalendar&calendar_id=1" : ["Joomla Spider Calendar 3.2.6 SQL ","http://www.exploit-db.com/exploits/34571/"],
"/components\com_youtubegallery\models\gallery.php" : ["com_youtubegallery  SQL",""],
"/mode=getshouts&jal_lastID=1337133713371337'" : ["Joomla AJAX Shoutbox remote SQL","http://www.exploit-db.com/exploits/32331/"],
"/index.php/weblinks-categories?id=1'" : ["Joomla 3.2.1 sql injection","http://www.exploit-db.com/exploits/31459/"],
"/option=com_community&view=frontpage" : ["JomSocial component 2.6 PHP code execution edzoit","http://www.exploit-db.com/exploits/31435/"],
"/?option=com_komento" : ["Cross-Site Scripting","http://www.exploit-db.com/exploits/31174/"],
"/index.php?option=com_virtuemart&view=user&task=removeAddressST&virtuemart_userinfo_id=16" : ["SQL Injection","http://www.exploit-db.com/exploits/27879/"],
"/index.php?option=com_sectionex&view=category&id=X&Itemid=Y" : ["Joomla com_sectionex v2.5.96 SQL","http://www.exploit-db.com/exploits/27405/"],
"/index.php?option=com_s5clanroster&view=s5clanroster&layout=category&task=category&id=1" : ["Joomla Component com_s5clanroster Sql","http://www.exploit-db.com/exploits/25410/"],
"/index.php/dj-classifieds/ads/0/?limitstart=0&se=1&se_regs[0]=1'" : ["Joomla - DJ Classifieds - Time-Based Blind SQL","http://www.exploit-db.com/exploits/25248/"],
"/plugins/system/remember/remember.php" : ["Joomla 3.0.3 PHP Object Injection Vulnerability","http://www.exploit-db.com/exploits/25087/"],
"/components/com_civicrm/civicrm/packages/OpenFlashChart/php-ofc-library/ofc_upload_image.php?name=" : ["joomla component com_civicrm remode code injection edzoit","http://www.exploit-db.com/exploits/24969/"],
"/?option=com_rsfiles&view=files&layout=agreement&tmpl=component&cid=1'" : ["Joomla Component RSfiles <= (cid) SQL injection Vulnerability","http://www.exploit-db.com/exploits/24851/"],
"/plugins/system/highlight/highlight.php" : ["Joomla 3.0.2(highlight.php)PHP Object Injection Vulnerability","http://www.exploit-db.com/exploits/24551/"],
"/index.php?option=com_collector&view=filelist&tmpl=component&folder=&type=1" : ["Joomla com_collecter shell upload ","http://www.exploit-db.com/exploits/24228/"],
"/?option=com_jooproperty&view=booking&layout=modal&product_id=1" : ["com_jooproperty SQL injection & xss","http://www.exploit-db.com/exploits/23286/"],
"/index.php?option=com_spidercalendar&Itemid=14&date=1" : ["(com_spidercalendar) Blind SQL Injection Vulnerability","http://www.exploit-db.com/exploits/23782/"],
"/index.php?option=com_spidercatalog&product_id=1" : ["com_spidercatalog SQL injection Vulnerability","http://www.exploit-db.com/exploits/22403/"],
"/index.php?option=com_kunena&func=userlist&search=1" : ["Joomla Component com_kunena SQL Injection","http://www.exploit-db.com/exploits/22153/"],
"/index.php?option=com_fss&view=test&prodid=777777.7" : ["Joomla Freestyle Support com_fss sqli","http://www.exploit-db.com/exploits/22097/"],
"/index.php?option=com_tag&task=tag&lang=es&tag=999999.9" : ["Joomla tag Remote Sql Edzoit ","http://www.exploit-db.com/exploits/22098/"],
"/index.php?option=com_icagenda&view=list&layout=event&Itemid=520&id=1" : ["Joomla Component (com_icagenda) Multiple Vulnerabilities",""],
"/index.php?option=com_spidercalendar&date=999999.9" : ["Joomla spider calendar lite Remote Edzoit","http://www.exploit-db.com/exploits/20983/"],
"/index.php?option=com_rokmodule&tmpl=component&type=raw&module=1" : ["Joomla Component RokModule Blind SQLi","http://www.exploit-db.com/exploits/21221/"],
"/index.php?option=com_fireboard&Itemid=0&id=1&catid=0&func=fb_pdf" : ["Joomla com_fireboard - SQLi","http://www.exploit-db.com/exploits/20390/"],
"/index.php?option=com_joomgalaxy&view=categorylist&type=thumbnail&lang=en&catid=100000001-100000001=0" : ["joomgalaxy 1.2.0.4 Multiple Vulnerabilites","http://www.exploit-db.com/exploits/20197/"],
"/index.php?option=com_niceajaxpoll&getpliseid=1" : ["com_niceajaxpoll 1.3.0 SQLI","http://www.exploit-db.com/exploits/20166/"],
"/index.php?option=com_movm&controller=product&task=product&id=999999'" : ["Joomla com_movm SQLi","http://www.exploit-db.com/exploits/20170/"],
"/component/osproperty/?task=agent_register" : ["com_osproperty Unrestricted File Upload","http://www.exploit-db.com/exploits/19829/"],
"/index.php?option=com_user&view=login" : ["com_KSAdvertiser Remote File & Bypass Upload Vulnerability","http://www.exploit-db.com/exploits/19792/"],
"/index.php?option=com_ponygallery&Itemid=1" : ["(com_ponygallery) SQLi","http://www.exploit-db.com/exploits/18741/"],
"/index.php?option=com_bearleague&task=team&tid=8&sid=1&Itemid=1" : ["(com_bearleague) SQL injection Vulnerability ","http://www.exploit-db.com/exploits/18729/"],
"/index.php?option=com_estateagent&Itemid=47&act=object&task=showEO&id=1" : ["(com_estateagent) SQLI","http://www.exploit-db.com/exploits/18728/"]}

if len(sys.argv) != 2:
    print "python joomdz.py www.site.com"
    sys.exit(1)

host = sys.argv[1].replace("http://","").rsplit("/",1)[0]
if host[-1] != "/":
    host = host+"/"
print " Site/Target:",host
print " Searching:",len(dz4ever) 

print " Scanning"
for dz,(poc,edz) in dz4ever.items():
    resp,reason,server = main(dz)
    if resp not in BAD_RESP:
        print ""
        print " Result:",resp, reason
        print " exploit:",poc
        print " exploit-db:",edz
    else:
        print ""
        print " Result:",resp, reason
		
print "\n[-] finish scan bro\n"
