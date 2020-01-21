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

class Backdoors():
	def __init__(self,url,agent,proxy,redirect):
		self.url = url
		self.printer = printer.Printer() 
		self.http = http.Http(agent=agent,proxy=proxy,redirect=redirect)
		self.checker = utils.Checker()

	def Run(self):
		info = {
		'name'        : 'Backdoors',
		'author'      : 'Momo Outaadi (@M4ll0k)',
		'description' : 'Tries to find common backdoors on the server'
		}
		dbbackdoors = open('data/Backdoors.txt','rb')
		dbfile = list([x.split('\n') for x in dbbackdoors])
		for  x in dbfile:
			try:				
				resp = self.http.Send(self.checker.Path(self.url,x[0]))
				if resp.status_code == 200 and resp._content:
					self.printer.plus('Found Backdoor: %s'%resp.url)
					break
			except Exception:
				pass
