#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import re

class Baidu():
	@staticmethod
	def Run(headers):
		_ = False
		try:
			for item in headers.items():
				_  = re.search(r'yunjiasu-nginx',item[1],re.I) is not None
				_ |= re.search(r'YJS-ID',item[1],re.I) is not None
				_ |= re.search(r'fhl',item[1],re.I) is not None
				if _: 
					return "Yunjiasu Web Application Firewall (Baidu)"
					break
		except Exception,ERROR:
			print ERROR