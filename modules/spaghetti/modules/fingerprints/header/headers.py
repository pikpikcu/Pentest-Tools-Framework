#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

from lib.utils import printer
import re

class Headers():
	@staticmethod	
	def Run(headers):
		info = []
		fields = ['Access-Control-Allow-Origin', 'Cache-Control', 'Content-MD5','Content-Disposition', 'ETag', 'Expires', 'P3P', 'Proxy-Authenticate', 'Refresh', 'Retry-After', 
		'Status', 'Strict-Transport-Security', 'Trailer', 'Upgrade', 'Warning', 'WWW-Authenticate', 'X-Frame-Options','Public-Key-Pins', 'X-XSS-Protection', 
		'Content-Security-Policy','X-Content-Security-Policy', 'X-WebKit-CSP', 'X-Content-Type-Options']
		try:
			if not re.search(r'X-Frame-Options',str(headers.keys()),re.I):
				info.append('The Anti-Clickjacking X-Frame-Options header is not present.')
			if not re.search(r'Strict-Transport-Security',str(headers.keys()),re.I):
				info.append('Strict-Transport-Security header is not present.')
			if not re.search(r'x-xss-protection',str(headers.keys()),re.I):
				info.append('X-XSS-Protection header is not present.')
			for x in fields:
				if x in headers.keys():
					printer.Printer().plus('Uncommon header \'%s\' found, with contents: %s'%(x,headers[x]))
		except Exception,ERROR:
			print ERROR