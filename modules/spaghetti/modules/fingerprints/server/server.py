#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

from lib.net import http
import re

class Server():
	""" """
	def __init__(self,url,agent='Mozilla5/0',proxy=None,redirect=False):
		self.url = url
		self.request = http.Http(agent=agent,proxy=proxy,redirect=redirect)

	def Run(self,headers):
		server = None
		try:
			for item in headers.items():
				if re.search(r'server',item[0],re.I):server = item[1]
			if server is None:
				resp = self.request.Send(self.url,method='GET',headers={'Expect':'Spaghetti'})
				for item in resp.headers.items():
					if re.search(r'server',item[0],re.I): server = item[1]
			return server
		except Exception,Error:
			print Error