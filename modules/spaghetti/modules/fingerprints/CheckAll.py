#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Server Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

from lang import lang
from framework import framework
from header import headers
from cms import cms
from server import server
from waf import waf
from os import os
from lib.net import http
from lib.net import utils
from lib.utils import printer

class CheckAll():
	""" Docstring for CheckAll """
	def __init__(self,url,agent,proxy,redirect):
		self.url = url
		self.printer = printer.Printer()
		self.request = http.Http(agent=agent,proxy=proxy,redirect=redirect)
		self.checker = utils.Checker()

	def Run(self):
		info = {
		'name' : 'CheckAll',
		'author' : 'Momo Outaadi (@M4ll0k)',
		'description' : 'Checking all fingerprints'
		}
		try:
			resp = self.request.Send(self.url)
			serv = server.Server(self.url).Run(resp.headers)
			self.printer.plus('Server: %s'%serv)
			f = ([x for x in waf.Waf(resp.headers)])
			for x in f:
				if x==None:pass
				else:
					self.printer.plus('Firewall: %s'%x);break
			o = ([x for x in os.Os(resp.headers)])
			for x in o:
				if x==None:pass
				else:
					self.printer.plus('Operating System: %s'%x);break
			l = ([x for x in lang.Lang(resp._content,resp.headers)])
			for x in l:
				if x==None:pass
				else:
					self.printer.plus('Language: %s'%x)
			h = ([x for x in framework.Framework(resp.headers)])
			for x in h:
				if x==None:pass
				else:
					self.printer.plus('Web Framework: %s'%x)
			c = ([x for x in cms.Cms(resp._content)])
			for x in c:
				if x==None:pass
				else:
					self.printer.plus('CMS: %s'%x)
			headers.Headers().Run(resp.headers)
		except Exception as Error:
			print Error