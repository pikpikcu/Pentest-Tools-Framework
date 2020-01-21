#/usr/bin/env python
# -*- Coding: UTF-8 -*-
#
# WPSeku: Wordpress Security Scanner
#
# @url: https://github.com/m4ll0k/WPSeku
# @author: Momo Outaadi (M4ll0k)

from lib import wphttp
from lib import wpprint

class wpfile:
	
	chk = wphttp.UCheck() 
	out = wpprint.wpprint()
	
	def __init__(self,agent,proxy,redir,time,url,cookie):
		self.url = url
		self.cookie = cookie
		self.req = wphttp.wphttp(
			agent=agent,proxy=proxy,
			redir=redir,time=time
			)
	def run(self):
		db = open('db/common_file.txt','rb')
		dbfiles = [file.split('\n') for file in db]
		try:
			for file in dbfiles:
				url = wpfile.chk.path(self.url,file[0])
				resp = self.req.send(url,c=self.cookie)
				if resp.status_code == 200 and resp._content != None:
					if resp.url == url:
						wpfile.out.plus('Found {} file under: {}'.format(file[0],resp.url))
		except Exception,e:
			pass