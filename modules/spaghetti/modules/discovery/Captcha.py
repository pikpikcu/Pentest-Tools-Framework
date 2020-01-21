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
from BeautifulSoup import BeautifulSoup

class Captcha():
	def __init__(self,url,agent,proxy,redirect):
		self.url = url
		self.printer  = printer.Printer() 
		self.http = http.Http(agent=agent,proxy=proxy,redirect=redirect)

	def Run(self):
		info = {
		'name'        : 'Captcha',
		'author'      : 'Momo Outaadi (@M4ll0k)',
		'description' : 'CAPTCHA protected form'
		}
		try:
			resp = self.http.Send(self.url)
			soup = BeautifulSoup(resp.content)
			html = str([x for x in soup.findAll('form')])
			if re.search(r'[\S*[re]captcha]*',html,re.I):
				self.printer.plus('CAPTCHA protected form.')
		except Exception as ERROR:
			pass