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

class PrivateIP():
	def __init__(self,url,agent,proxy,redirect):
		self.url = url
		self.printer = printer.Printer() 
		self.http = http.Http(agent=agent,proxy=proxy,redirect=redirect)

	def Run(self):
		info = {
		'name'        : 'PrivateIP',
		'author'      : 'Momo Outaadi (@M4ll0k)',
		'description' : 'Private IP address disclosure'
		}
		try:
			resp = self.http.Send(self.url)
			regex = re.compile('[0-9]+(?:\.[0-9]+){3}')
			ip = regex.findall(resp.content)
			if ip:
				if len(ip) == 1:
					self.printer.plus('Private IP address disclosure: %s'%ip[0])
				else:
					self.printer.plus('Private IP address disclosure: %s'%ip)
		except Exception:
			pass
