#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Server Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import re
from lib.net import http 
from lib.utils import printer
from lib.net import utils

class AllowMethod():
	def __init__(self,url,agent,proxy,redirect):
		self.url = url 
		self.printer = printer.Printer() 
		self.http = http.Http(agent=agent,proxy=proxy,redirect=redirect)
		self.checher = utils.Checker()

	def Run(self):
		info = {
		'name'        : 'Allow Methods',
		'author'      : 'Momo Outaadi (M4ll0k)',
		'description' : 'Checks for supported HTTP methods'
		}
		dballowmethod = open('data/AllowMethod.txt','rb')
		dbfiles = list([x.split('\n') for x in dballowmethod])
		for x in dbfiles:
			try:
				resp = self.http.Send(url=self.url,method=x[0])
				if re.search(r'allow|public',str(resp.headers.keys()),re.I):
					allow = resp.headers['allow']
					if allow == None: allow += resp.headers['public']
					self.printer.plus('Allowed HTTP Methods: %s'%allow)
					break
			except Exception as ERROR:
				pass