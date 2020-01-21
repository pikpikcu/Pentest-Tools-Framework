#/usr/bin/env python
# -*- Coding: UTF-8 -*-
#
# WPSeku: Wordpress Security Scanner
#
# @url: https://github.com/m4ll0k/WPSeku
# @author: Momo Outaadi (M4ll0k)

from lib import wphttp
from lib import wpprint

class wplogin:
	
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
			url = wplogin.chk.path(self.url,'/wp-login.php')
			resp = self.req.send(url,c=self.cookie)
			if resp.status_code == 200:
				if resp.url == url:
					wplogin.out.plus('wp-login not detect protection under: {}'.format(resp.url))
			elif resp.status_code == 404:
				if resp.url == url:
					wplogin.out.plus('wp-login detect protection under: {}'.format(resp.url))
		except Exception,e:
			pass