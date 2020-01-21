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

class Backup():
	def __init__(self,url,agent,proxy,redirect):
		self.url = url
		self.printer = printer.Printer() 
		self.http = http.Http(agent=agent,proxy=proxy,redirect=redirect)
		self.checker = utils.Checker()

	def Run(self):
		info = {
		'name'        : 'Backup',
		'author'      : 'Momo Outaadi (@M4ll0k)',
		'description' : 'Tries to find backed-up files/dirs on server'
		}
		dbbackup = open('data/BackupDirs.txt','rb')
		dbfiles = list([x.split('\n') for x in dbbackup])
		try:
			for x in dbfiles:
				resp = self.http.Send(self.checker.Path(self.url,x[0]))
				if resp.status_code == 200 and resp._content:
					if resp.url == self.checker.Path(self.url,x[0]):
						self.printer.plus('Found Backup: %s'%resp.url)
					else:
						pass
		except Exception as ERROR:
			pass