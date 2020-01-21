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

class Cookie():
	def __init__(self,url,agent,proxy,redirect):
		self.url = url
		self.printer = printer.Printer() 
		self.http = http.Http(agent=agent,proxy=proxy,redirect=redirect)

	def Run(self):
		info = {
		'name'        : 'Cookie',
		'author'      : 'Momo Outaadi (@M4ll0k)',
		'description' : 'Cookies Security'
		}
		try:
			resp = self.http.Send(self.url)
			if resp.headers['set-cookie']:
				if re.search(r'(domain=\S*)',resp.headers['set-cookie'],re.I):
					self.printer.plus('Cookies are accessible by all subdomains. See https://www.owasp.org/index.php/Testing_for_cookies_attributes_(OTG-SESS-002) for details.')
				if not re.search(r'(httponly)',resp.headers['set-cookie'],re.I):
					self.printer.plus('Cookies created without HTTPOnly Flag. See https://www.owasp.org/index.php/Testing_for_cookies_attributes_(OTG-SESS-002) for details.')
				if not re.search(r'(secure)',resp.headers['set-cookie'],re.I):
					self.printer.plus('Cookies created without Secure Flag. See https://www.owasp.org/index.php/Testing_for_cookies_attributes_(OTG-SESS-002) for details.')
		except Exception:
			pass
