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
import re

class Robots():
	def __init__(self,url,agent,proxy,redirect):
		self.url = url
		self.printer = printer.Printer() 
		self.http = http.Http(agent=agent,proxy=proxy,redirect=redirect)
		self.checker = utils.Checker()

	def Run(self):
		info = {
		'name'        : 'Robots',
		'author'      : 'Momo Outaadi (@M4ll0k)',
		'description' : 'Robots.txt'
		}
		try:
			resp = self.http.Send(self.checker.Path(self.url,'robots.txt'))
			if resp.status_code == 200 and resp._content:
				self.printer.plus('Checking robots path:\n')
				path = re.findall(r'Disallow:|Allow: (/\S*/)',resp.content,re.I)
				dpath = []
				for x in path:
					if x != '' and x not in dpath:
						dpath.append(x)
				for x in dpath:
					resp = self.http.Send(self.checker.Path(self.url,x))
					print(' - [%s] %s'%(resp.status_code,resp.url))
				print("")
		except Exception:
			pass
