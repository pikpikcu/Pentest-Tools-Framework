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

class Email():
	def __init__(self,url,agent,proxy,redirect):
		self.url = url
		self.printer = printer.Printer() 
		self.http = http.Http(agent=agent,proxy=proxy,redirect=redirect)

	def Run(self):
		info = {
		'name'        : 'Email',
		'author'      : 'Momo Outaadi (@M4ll0k)',
		'description' : 'Email address disclosure'
		}
		try:
			resp = self.http.Send(self.url)
			email = re.findall('"mailto:(.+?)"',resp.content,re.I)
			if email:
				if len(email) == 1:
					self.printer.plus('Email address disclosure: %s'%email[0])
				else:
					self.printer.plus('Email address disclosure: %s'%email)
		except Exception:
			pass
