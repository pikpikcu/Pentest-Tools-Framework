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
from lib.net import utils
from lib.utils import printer

class ModStatus():
	def __init__(self,url,agent,proxy,redirect):
		self.url = url
		self.printer = printer.Printer() 
		self.http = http.Http(agent=agent,proxy=proxy,redirect=redirect)
		self.checker = utils.Checker()

	def Run(self):
		info = {
		'name'        : 'ModStatus',
		'author'      : 'Momo Outaadi (@M4ll0k)',
		'description' : 'Apache mod_status'
		}
		try:
			for x in ['/server-status/', '/server_status/', '/serverstatus/', '/mod-status/', '/mod_status/', '/modstatus', 'status']:
				resp = self.http.Send(self.checker.Path(self.url,x))
				if resp.status_code == 200 and re.search(r'*Apache Server Status for*',resp.content,re.I):
					self.printer.plus('Apache (mod_status) information disclosure at: %s'%resp.url)
					break
		except Exception:
			pass
