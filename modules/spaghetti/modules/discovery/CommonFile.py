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

class CommonFile():
	def __init__(self,url,agent,proxy,redirect):
		self.url = url 
		self.printer = printer.Printer() 
		self.http = http.Http(agent=agent,proxy=proxy,redirect=redirect)
		self.checker = utils.Checker()

	def Run(self):
		info = {
		'name'        : 'CommonFile',
		'author'      : 'Momo Outaadi (@M4ll0k)',
		'description' : 'Common files'
		}
		dbcommondirs = open('data/CommFiles.txt','rb')
		dbfiles = list([x.split('\n') for x in dbcommondirs])
		for x in dbfiles:
			try:
				resp = self.http.Send(self.checker.Path(self.url,x[0]))
				if resp.status_code == 200 and resp._content:
					self.printer.plus('Files Found: %s'%resp.url)
			except Exception:
				pass
