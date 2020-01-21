#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Server Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

from lib.net import http 
from lib.net import utils
from lib.utils import printer
import re

class CommonDirectory():
	def __init__(self,url,agent,proxy,redirect):
		self.url = url
		self.printer = printer.Printer() 
		self.http = http.Http(agent=agent,proxy=proxy,redirect=redirect)
		self.checker = utils.Checker()

	def Run(self):
		info = {
		'name'        : 'CommonDirectory',
		'author'      : 'Momo Outaadi (@M4ll0k)',
		'description' : 'Common directories'
		}
		dbcommondirs = open('data/CommDirs.txt','rb')
		dbfiles = list([x.split('\n') for x in dbcommondirs])
		for x in dbfiles:
			try:
				resp = self.http.Send(self.checker.Path(self.url,x[0]))
				if resp.status_code == 200 and resp._content:
					self.printer.plus('Directory Found: %s'%resp.url)
					if re.search(r'index of',resp.content,re.I):
						self.printer.plus('Dir \'%s\' listing enabled.'%x[0])
			except Exception:
				pass
