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
from lib.net import utils

class MultiIndex():
	def __init__(self,url,agent,proxy,redirect):
		self.url = url
		self.printer = printer.Printer() 
		self.http = http.Http(agent=agent,proxy=proxy,redirect=redirect)
		self.checker = utils.Checker()

	def Run(self):
		info = {
		'name'        : 'MultiIndex',
		'author'      : 'Momo Outaadi (M4ll0k)',
		'description' : 'Checks for multiple index files'
		}
		dblmutliindex = open('data/MultiIndex.txt','rb')
		dbfiles = list([x.split('\n') for x in dblmutliindex])
		try:
			for x in dbfiles:
				resp = self.http.Send(self.checker.Path(self.url,x[0]))
				if resp.status_code == 200 and resp._content:
					self.printer.plus('Index page found: %s'%resp.url)
		except Exception as ERROR:
			pass