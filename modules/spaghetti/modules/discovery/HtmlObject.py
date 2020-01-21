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

class HtmlObject():
	def __init__(self,url,agent,proxy,redirect):
		self.url = url
		self.printer = printer.Printer() 
		self.http = http.Http(agent=agent,proxy=proxy,redirect=redirect)

	def Run(self):
		info = {
		'name'        : 'HtmlObject',
		'author'      : 'Momo Outaadi (@M4ll0k)',
		'description' : 'HTML Object'
		}
		try:
			resp = self.http.Send(self.url)
			if re.search(r'<object.*?>.*?<\/object>',resp._content,re.I):
				self.printer.plus('Found HTML Object. Logs the existence of HTML object tags.')
		except Exception:
			pass
