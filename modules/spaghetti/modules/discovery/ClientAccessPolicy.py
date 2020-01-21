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
import re

class ClientAccessPolicy():
	def __init__(self,url,agent,proxy,redirect):
		self.url = url
		self.printer = printer.Printer() 
		self.http = http.Http(agent=agent,proxy=proxy,redirect=redirect)

	def Run(self):
		info = {
		'name'        : 'ClientAcessPolicy',
		'author'      : 'Momo Outaadi (@M4ll0k)',
		'description' : 'Checks whether a client access file exists, and if it contains a wildcard entry.'
		}
		try:
			resp = self.http.Send(url=self.url,method='GET',payload='/clientacesspolicy.xml')
			if resp.status_code == 200 and resp.content:
				domains = re.findall('domain="(.+?)"',resp.content,re.I)
				new_domain = []
				for x in domains:
					if '.' in x:
						if x not in new_domain:
							new_domain.append(x)
				if new_domain:
					self.printer.plus('/clientacesspolicy.xml found domain: ')
					for x in new_domain:
						print(" - %s" % x)
		except Exception:
			pass
