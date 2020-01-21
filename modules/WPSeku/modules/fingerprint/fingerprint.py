#/usr/bin/env python
# -*- Coding: UTF-8 -*-
#
# WPSeku: Wordpress Security Scanner
#
# @url: https://github.com/m4ll0k/WPSeku
# @author: Momo Outaadi (M4ll0k)

import waf
import server
import headers

from lib import wphttp
from lib import wpprint

class fingerprint:
	
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
			resp = self.req.send(self.url,c=self.cookie)
			server.wpserver().run(resp.headers)
			waf.wpwaf().run(resp._content)
			headers.wpheaders().run(resp.headers)
			wpprint.wpprint().passs()
		except Exception,e:
			pass