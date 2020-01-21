#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Server Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

from lib.net import http 
from lib.utils import printer
import re

class ApacheXss():
	def __init__(self,url,agent,proxy,redirect):
		self.url = url
		self.printer = printer.Printer() 
		self.http = http.Http(agent=agent,proxy=proxy,redirect=redirect)
	
	def Run(self):
		info = {
		'name'        : 'ApacheXss',
		'author'      : 'Momo Outaadi (@M4ll0k)',
		'description' : 'Checks whether the web servers has a cross-site scripting vulnerability through the Expect: HTTP header'
		}
		try:
			resp = self.http.Send(url=self.url,headers={'Expect':'<script>alert(xss)</script>'})
			if re.search(r'<script>alert\(xss\)<\/script>',resp.content,re.I):
				self.printer.plus('Apache is vulnerable to XSS via the Expect header')
		except Exception:
			pass
