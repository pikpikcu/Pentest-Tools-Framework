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

class ApacheUsers():
	def __init__(self,url,agent,proxy,redirect):
		self.url = url 
		self.printer = printer.Printer() 
		self.http = http.Http(agent=agent,proxy=proxy,redirect=redirect)
		self.cheker = utils.Checker()

	def Run(self):
		info = {
		'name'        : 'ApacheUsers',
		'author'      : 'Momo Outaadi (@M4ll0k)',
		'description' : 'Apache "mod_userdir" User Enumeration'
		}
		try:
			resp = self.http.Send(self.cheker.Path(self.url,'/~bin'))
			if resp.status_code == 200 and resp._content or resp.status_code == 403 and resp._content:
				self.printer.plus('Apache (mod_userdir) enumeration user is possible.')
		except Exception:
			pass
