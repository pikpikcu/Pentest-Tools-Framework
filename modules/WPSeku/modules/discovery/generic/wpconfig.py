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

class wpconfig:
	
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
		try:
			url = wpconfig.chk.path(self.url,'/wp-config.php')
			resp = self.req.send(url,c=self.cookie)
			if resp.status_code == 200 and resp._content != None:
				if resp.url == url:
					if re.search(r'\S+define(\S+,*)',resp._content):
						wpconfig.out.plus('wp-config available under: {}'.format(resp.url))
			self.wpbk()
		except Exception,e:
			pass

	def wpbk(self):
		ext = ['.php~','.backup','.old','.save','.bak','.copy','.tmp',
		       '.txt','.zip','.db','.dat','.tar.gz','.test','.orig']
		try:
			for ex in ext:
				wpc = "/wp-config"+ex 
				url = wpconfig.chk.path(self.url,wpc)
				resp = self.req.send(url,c=self.cookie)
				if resp.status_code == 200 and resp._content != None:
					if resp.url == url:
						wpconfig.out.plus('wp-config backup available under: {}'.format(resp.url))
						exit()
		except Exception,e:
			pass