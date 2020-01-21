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

class AdminInterfaces():
	def __init__(self,url,agent,proxy,redirect):
		self.url = url
		self.printer = printer.Printer() 
		self.http = http.Http(agent=agent,proxy=proxy,redirect=redirect)
		self.check = utils.Checker()

	def Run(self):
		info = {
		'name':'Common administration interfaces',
		'author':'Momo Outaadi (M4ll0k)',
		'description':'Access to administration interfaces panel'
		}
		dbadmin = open('data/AdminPanels.txt','rb')
		dbfiles = list([x.split('\n') for x in dbadmin])
		for x in dbfiles:
			try:
				resp = self.http.Send(self.check.Path(self.url,x[0]))
				if resp._content and resp.status_code == 200:
					if resp.url == self.check.Path(self.url,x[0]):
						self.printer.plus('Admin interface: %s'%(resp.url))
						break
					else: 
						pass
			except Exception as ERROR:
				pass