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

class wpfpd:
	
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
			url = wpfpd.chk.path(self.url,'/wp-includes/rss-functions.php')
			resp = self.req.send(url,c=self.cookie)
			if resp.status_code == 200 and resp._content != None:
				if re.search(r'Fatal error',resp._content):
						wpfpd.out.plus('Full Path Disclosure: {}'.format(resp.url))
		except Exception,e:
			pass