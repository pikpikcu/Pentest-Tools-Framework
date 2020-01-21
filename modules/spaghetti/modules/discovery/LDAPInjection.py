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

class LDAPInjection():
	def __init__(self,url,agent,proxy,redirect):
		self.url = url 
		self.printer = printer.Printer() 
		self.http = http.Http(agent=agent,proxy=proxy,redirect=redirect)
		self.checker = utils.Checker()

	def Run(self):
		info = {
		'name'        : 'LDAP Injection',
		'author'      : 'Momo Outaadi (M4ll0k)',
		'description' : 'It tries to force the web application to return LDAP error messages, in order to discover failures in user input validation.'
		}
		dbldap = open('data/LDAP.txt','rb')
		dbfiles = list([x.split('\n') for x in dbldap])
		try:
			resp = self.http.Send(self.checker.Path(self.url,'#^($!@$)(()))******'))
			for x in dbfiles:
				if re.search(x[0],resp._content,re.I):
					self.printer.plus('LDAP Error: %s'%x[0])
					break
		except Exception as ERROR:
			pass